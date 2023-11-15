import re
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.fx import Graph, GraphModule

import onnx
import onnx_graphsurgeon as gs
import onnxruntime.tools.symbolic_shape_infer as onnxrt_symbolic_shape_inference

import _operator
from .pytorch_layers import *


class OnnxPytorchParser:
    def __init__(self, model, fuse=False, dynamic_batch=False):
        super(OnnxPytorchParser, self).__init__()
        self.model = model
        self.onnx_model = onnx.load(model)

        self.onnx_model = onnxrt_symbolic_shape_inference.SymbolicShapeInference.infer_shapes(self.onnx_model, auto_merge=True)        
        self.graph = gs.import_onnx(self.onnx_model)
        self.graph.fold_constants().cleanup().toposort()
        self.pytorch_graph = Graph()
        self.pytorch_graph_module = GraphModule(torch.nn.Module(), self.pytorch_graph)
        self.env = {}
        self._illegal_char_regex = re.compile("[^0-9a-zA-Z_]+")

    def convert(self):
        self.gen_pytorch_graph_module()
        return self.pytorch_graph_module

    def create_arg(self, a):
        if isinstance(a, torch.nn.Parameter):
            for n, p in self.pytorch_graph_module.named_parameters():
                if a is p:
                    return self.create_node("get_attr", n, (), {})
        elif isinstance(a, torch.Tensor):
            for n_, p_ in self.pytorch_graph_module.named_buffers():
                if a is p_:
                    return self.create_node("get_attr", n_, (), {})
        elif isinstance(a, torch.nn.Module):
            for n_, p_ in self.pytorch_graph_module.named_modules():
                if a is p_:
                    return self.create_node("get_attr", n_, (), {})
        # For NamedTuple instances that appear literally as args, we emit
        # a node to construct the NamedTuple and use that Node as the argument.
        if isinstance(a, tuple) and hasattr(a, "_fields"):
            args = tuple(self.create_arg(elem) for elem in a)
            return self.create_node("call_function", a.__class__, args, {})

        qualname = None
        if isinstance(a, (torch.Tensor)):
            if not qualname:
                i = 0
                while True:
                    qualname = f"_tensor_constant{i}"
                    if not hasattr(self.pytorch_graph_module, qualname):
                        break
                    i += 1
                setattr(self.pytorch_graph_module, qualname, a)

            return self.pytorch_graph.create_node("get_attr", qualname, (), {})

    def process_inputs(self, inputs):
        inputs = list(inputs)
        for idx in range(len(inputs)):
            input = self.create_arg(inputs[idx])
            if input:
                inputs[idx] = input

        inputs = tuple(inputs)
        
        return inputs

    def gen_pytorch_graph_module(self):
        for input in self.graph.inputs:
            node = self.pytorch_graph.placeholder(
                self._illegal_char_regex.sub("_", input.name)
            )
            self.env[input.name] = node

        for onnx_node in self.graph.nodes:
            if onnx_node.op == "Conv":
                module = Conv.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "LayerNormalization":
                module = LayerNorm.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node                
            elif onnx_node.op == "Relu":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    F.relu,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Add":
                inputs = Arithmetic.from_onnx(onnx_node, self.env)
                inputs = self.process_inputs(inputs)
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.add,
                    inputs,
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Sub":
                inputs = Arithmetic.from_onnx(onnx_node, self.env)
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.sub,
                    inputs,
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node                
            elif onnx_node.op == "Div":
                inputs = Arithmetic.from_onnx(onnx_node, self.env)
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.div,
                    inputs,
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Mul":
                inputs = Arithmetic.from_onnx(onnx_node, self.env)
                inputs = self.process_inputs(inputs)
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.mul,
                    inputs,
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "MatMul":
                inputs = Arithmetic.from_onnx(onnx_node, self.env)
                inputs = self.process_inputs(inputs)
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.matmul,
                    inputs,
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node         
            elif onnx_node.op == "Gelu":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    F.gelu,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node                          
            elif onnx_node.op == "GlobalAveragePool":
                module = Pool.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "MaxPool":
                module = Pool.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "AveragePool":
                module = Pool.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Flatten":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.flatten,
                    (self.env[onnx_node.inputs[0].name],),
                    {"start_dim": onnx_node.attrs["axis"]},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Concat":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.cat,
                    ([self.env[input_node.name] for input_node in onnx_node.inputs],),
                    {"dim": onnx_node.attrs["axis"]},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Reshape":
                node = self.pytorch_graph.create_node(
                    "call_method",
                    "reshape",
                    (
                        self.env[onnx_node.inputs[0].name],
                        onnx_node.inputs[1].values.tolist(),
                    ),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Transpose":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.permute,
                    (
                        self.env[onnx_node.inputs[0].name],
                        onnx_node.attrs["perm"],
                    ),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Split":
                node = self.pytorch_graph.create_node(
                    "call_function",
                    torch.chunk,
                    (
                        self.env[onnx_node.inputs[0].name],
                        len(onnx_node.inputs[1].values.tolist()),
                    ),
                    {"dim": onnx_node.attrs["axis"]},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
                for i, output in enumerate(onnx_node.outputs):
                    node = self.pytorch_graph.create_node(
                        "call_function",
                        _operator.getitem,
                        (
                            self.env[onnx_node.outputs[0].name],
                            i,
                        ),
                        {},
                        output.name,
                    )
                    self.env[output.name] = node
            elif onnx_node.op == "Slice":
                inputs = Slice.from_onnx(onnx_node, self.env)
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    _operator.getitem,
                    (
                        self.env[onnx_node.inputs[0].name],
                        inputs,
                    ),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Gemm":
                module = Linear.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "BatchNormalization":
                module = BatchNorm.from_onnx(onnx_node)
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node                
            elif onnx_node.op == "Softmax":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    F.softmax,
                    (self.env[onnx_node.inputs[0].name],),
                    {"dim": -1},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Sigmoid":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    F.sigmoid,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "HardSwish":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    F.hardswish,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node    
            elif onnx_node.op == "LeakyRelu":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    F.hardswish,
                    (self.env[onnx_node.inputs[0].name], onnx_node.attrs['alpha']),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node         
            elif onnx_node.op == "Resize":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    F.interpolate,
                    (self.env[onnx_node.inputs[0].name],),
                    {'scale_factor': onnx_node.inputs[2].values.tolist()[2:], 'mode': onnx_node.attrs['mode']},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node                                        
            elif onnx_node.op == "ReduceMean":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_method",
                    "mean",
                    (self.env[onnx_node.inputs[0].name],),
                    {
                        "dim": onnx_node.attrs["axes"],
                        "keepdim": bool(onnx_node.attrs.get("keepdims", 1)),
                    },
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Shape":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    getattr,
                    (self.env[onnx_node.inputs[0].name], "shape"),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "Gather":
                node = self.pytorch_graph_module.graph.create_node(
                    "call_function",
                    _operator.getitem,
                    (
                        self.env[onnx_node.inputs[0].name],
                        int(onnx_node.inputs[1].values),
                    ),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[onnx_node.outputs[0].name] = node
            elif onnx_node.op == "QuantizeLinear":
                dequant_node = onnx_node.o(0)
                assert(dequant_node.op == "DequantizeLinear")

                module = Observer(float(onnx_node.inputs[1].values), float(onnx_node.inputs[2].values))
                self.pytorch_graph_module.add_submodule(onnx_node.outputs[0].name, module)
                node = self.pytorch_graph.create_node(
                    "call_module",
                    onnx_node.outputs[0].name,
                    (self.env[onnx_node.inputs[0].name],),
                    {},
                    onnx_node.outputs[0].name,
                )
                self.env[dequant_node.outputs[0].name] = node
            elif onnx_node.op == "DequantizeLinear":
                pass                          
            else:
                raise NotImplementedError(
                    "Operator {} is not supported.".format(onnx_node.op)
                )

        for output in self.graph.outputs:
            node = self.pytorch_graph.output(self.env[output.name])
            self.env[output.name] = node

        self.pytorch_graph_module.graph.lint()
        self.pytorch_graph_module.recompile()
