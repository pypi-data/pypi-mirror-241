"""Functional interface"""
from typing import Callable, List, Optional, Tuple, Union
import math
import warnings
import langtorch
from .session import Session
import torch

TextTensor = langtorch.TextTensor
Text = langtorch.Text


def mean(input: TextTensor, method = "Look at the following texts entries. Construct one 'mean' texts that averages their content into one semantically-rich texts of a similar length and style to individual entries:\n\n", dim: Optional[Union[int, List[int]]], keepdim: bool=False, dtype: Optional=Text, model = 'default') -> TextTensor:
    input = input.join("\n---\n", dim=dim, keepdim=keepdim)
    input = method*input
    session = Session()
    if model == 'default':
        output = langtorch.tt.Activation('gpt3.5-turbo')(input)
    else:
        output = langtorch.tt.Activation(model = model)(input)
    return output
