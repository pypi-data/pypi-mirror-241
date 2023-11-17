import torch
from ...tensors import CodeTensor
from ...tensors import TextTensor
from .textmodule import TextModule


class CodeModule(TextModule):
    def __init__(self, content = "", activation=None, key=None):
        super().__init__(content, activation, key)
        if not isinstance(content, CodeTensor):
            raise ValueError("Expected a CodeTensor for initialization.")

    def forward(self, input_text_tensor):
        return self.content.eval(input_text_tensor)