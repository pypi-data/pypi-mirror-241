from typing import Optional, Union, List
from ...tensors import TextTensor, ChatTensor
import langtorch.utils
from langtorch import ctx
import torch
from .textmodule import TextModule
import torch
from torch.nn.modules.loss import _Loss, _Reduction

session = ctx

class _TextLoss(TextModule):
    reduction: str

    def __init__(self, prompt: str, activation=None, key="loss", reduce=None, reduction: str = 'None') -> None:
        super().__init__(prompt, activation=activation, key=key)
        if reduce is not None:
            self.reduction: str = _Reduction.legacy_get_string(True, reduce)
        else:
            self.reduction = reduction

class CompareAnswersLoss(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input: TextTensor, target: TextTensor, prompt: TextTensor):
        ctx.save_for_backward(input, target)
        assert input.shape == target.shape, f"Input and target must have the same shape. Got {input.shape} and {target.shape} instead."
        loss = prompt * input.add_key_("input") * target.add_key_('target') # Example loss computation
        return loss

    @staticmethod
    def backward(ctx, grad_output):
        input, target = ctx.saved_tensors
        grad_input = grad_target = None

        if ctx.needs_input_grad[0]:
            # Compute gradient for input
            grad_input = grad_output * (input.content - target.content).sign()

        if ctx.needs_input_grad[1]:
            # Compute gradient for target
            grad_target = -grad_input

        # The gradients for non-tensors arguments must be None.
        return grad_input, grad_target

class TextLoss(_TextLoss):
    def __init__(self, prompt: TextTensor, activation=None, key="loss", reduction: str = 'None'):
        super(TextLoss, self).__init__(activation=activation, key=key, prompt=prompt, reduction=reduction)

    def forward(self, input: TextTensor, target: TextTensor):
        loss = CompareAnswersLoss.apply(input, target, self.prompt)
        if self.reduction == 'none':
            return loss
        elif self.reduction == 'mean':
            return loss.mean()
        elif self.reduction == 'sum':
            return loss.sum()
        else:
            raise ValueError(f"Unknown reduction: {self.reduction}")
