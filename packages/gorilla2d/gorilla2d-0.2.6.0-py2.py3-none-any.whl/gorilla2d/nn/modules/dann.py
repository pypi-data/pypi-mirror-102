# Copyright (c) Gorilla-Lab. All rights reserved.
import torch
import torch.nn as nn
from torch.autograd import Function


class GradReverse(Function):
    """
    Extension of grad reverse layer
    """
    @staticmethod
    def forward(ctx, x, constant):
        ctx.constant = constant
        return x.view_as(x)

    @staticmethod
    def backward(ctx, grad_output):
        grad_output = grad_output.neg() * ctx.constant
        return grad_output, None

    @staticmethod
    def grad_reverse(x, constant):
        return GradReverse.apply(x, constant)
