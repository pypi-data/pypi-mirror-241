from collections import OrderedDict, defaultdict, abc as container_abcs
import torch
from copy import deepcopy
from itertools import chain
import warnings
import functools
import math

from typing import Callable, Dict, List, Tuple

import torch.utils.hooks as hooks
from torch.utils.hooks import RemovableHandle
from torch._utils import is_compiling
from collections import defaultdict
from copy import deepcopy
from itertools import chain

from langtorch.session import Session
from langtorch import TextTensor, TextModule
import torch
from torch.optim import Optimizer
from torch._six import container_abcs


class TextOptimizer(Optimizer):
    def __init__(self, params, defaults):
        super(TextOptimizer, self).__init__(params, defaults)

    def step(self, closure=None):
        """Performs a single optimization step.

        Args:
            closure (callable, optional): A closure that reevaluates the model
            and returns the loss.
        """
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            for param in group['params']:
                if not isinstance(param, TextTensor):
                    raise ValueError("Optimizer parameters must be of type TextTensor")
                if param.grad is None:
                    continue
                grad = param.grad.data
                if grad.is_sparse:
                    raise RuntimeError('TextTensorOptimizer does not support sparse gradients')

                # Perform the optimization step to update 'param.data'
                # This is where the custom optimization logic would go
                # For demonstration, let's just subtract a fraction of the gradient
                param.data.add_(-group['lr'], grad)

        return loss

    def add_param_group(self, param_group):
        """Add a parameter group to the Optimizer's param_groups.

        This would be overridden only if we need to enforce specific types within param groups.
        """
        if not isinstance(param_group, dict):
            raise TypeError("param_group must be a dict")

        params = param_group['params']
        if isinstance(params, TextTensor):
            param_group['params'] = [params]
        elif isinstance(params, set):
            raise TypeError("parameter group cannot be a set")
        else:
            param_group['params'] = list(params)

        for param in param_group['params']:
            if not isinstance(param, TextTensor):
                raise ValueError("Optimizer parameters must be of type TextTensor")
            if not param.is_leaf:
                raise ValueError("can't optimize a non-leaf TextTensor")

        self.param_groups.append(param_group)

# Example usage:

optimizer = TextOptimizer(textmodule, defaults={'lr': 1e-3})

# Then in your training loop:
optimizer.zero_grad()
# ... compute your loss ...
loss.backward()
optimizer.step()
