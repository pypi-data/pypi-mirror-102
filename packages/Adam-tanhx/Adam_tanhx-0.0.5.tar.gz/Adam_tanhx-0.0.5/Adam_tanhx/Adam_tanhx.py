import math
import torch
from torch.optim.optimizer import Optimizer
import torch.nn.functional as F
import numpy as np
import torch.nn as nn


# import torch.optim as Optimizer
class Adam_tanhx(Optimizer):
    r"""Implements Adam_tanh_w algorithm. It is modified from the pytorch implementation of Adam.
    Arguments:
        params (iterable): iterable of parameters to optimize or dicts defining
            parameter groups
        lr (float, optional): learning rate (default: 1e-3)
        betas (Tuple[float, float], optional): coefficients used for computing
            running averages of gradient and its square (default: (0.9, 0.999))
        eps (float, optional): term added to the denominator to improve
            numerical stability (default: 1e-8)
        weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
    """
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), gama=0.5,eps=1e-8, weight_decay=1e-2):
        self.gama=gama
        if not 0.0 <= lr:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if not 0.0 <= eps:
            raise ValueError("Invalid epsilon value: {}".format(eps))
        if not 0.0 <= betas[0] < 1.0:
            raise ValueError("Invalid beta parameter at index 0: {}".format(betas[0]))
        if not 0.0 <= betas[1] < 1.0:
            raise ValueError("Invalid beta parameter at index 1: {}".format(betas[1]))
        defaults = dict(lr=lr, betas=betas, eps=eps, weight_decay=weight_decay)
        super(Adam_tanhx, self).__init__(params, defaults)

    def __setstate__(self, state):
        super(Adam_tanhx, self).__setstate__(state)

    @torch.no_grad()
    def step(self, closure=None):
        """Performs a single optimization step.
        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue

                # Perform stepweight decay
                p.mul_(1 - group['lr'] * group['weight_decay'])

                grad = p.grad.data
                if grad.is_sparse:
                    raise RuntimeError('Adam_tanhx does not support sparse gradients, please consider SparseAdam instead')

                state = self.state[p]

                # State initialization
                if len(state) == 0:
                    state['step'] = 0
                    # Exponential moving average of gradient values
                    state['exp_avg'] = torch.zeros_like(p.data)
                    # Exponential moving average of squared gradient values
                    state['exp_avg_sq'] = torch.zeros_like(p.data)
                    # Previous gradient
                    state['previous_grad'] = torch.zeros_like(p.data)

                exp_avg, exp_avg_sq, previous_grad = state['exp_avg'], state['exp_avg_sq'], state['previous_grad']
                beta1, beta2 = group['betas']

                state['step'] += 1

                # Decay the first and second moment running average coefficient
                exp_avg.mul_(beta1).add_(grad,alpha = (1 - beta1))
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad,value = 1 - beta2)
                denom = exp_avg_sq.sqrt().add_(group['eps'])

                bias_correction1 = 1 - beta1 ** state['step']
                bias_correction2 = 1 - beta2 ** state['step']

                # compute fai
                fai = abs(previous_grad - grad)
                fai = self.gama * torch.tanh(fai) + (1-self.gama)
                state['previous_grad'] = grad.clone()

                # update momentum with fai
                exp_avg1 = exp_avg * fai

                step_size = group['lr'] * math.sqrt(bias_correction2) / bias_correction1

                p.data.addcdiv_(exp_avg1, denom,value = -step_size)

        return loss

def description():
    print("There is an optimizer  with better performance than Adam in CIFAR-10 and CIFAR-100 dataset.")
    print("Its name:Adam_tanhx ")
    print(" ")
    print("use methods:")
    print("pip install Adam_tanhx")
    print("import Adam_tanhx")
    print("optimizer = Adam_tanx.Adam_tanhx(net.parameters())")