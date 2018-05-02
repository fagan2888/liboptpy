import numpy as np

class _StepSize(object):
    def __init__(self):
        pass
    def get_stepsize(self, h, x):
        raise NotImplementedError("Method to get current step size has to be implemented!")
        
    def assign_function(self, f, grad):
        pass
    
class ConstantStepSize(_StepSize):
    def __init__(self, stepsize):
        self.stepsize = stepsize
    
    def get_stepsize(self, h, x):
        return self.stepsize
    
class Backtracking(_StepSize):
    def __init__(self, rule_type, **kwargs):
        self.rule = rule_type
        self.par = kwargs
    
    def assign_function(self, f, grad):
        self.f = f
        self.grad = grad
    
    def get_stepsize(self, h, x):
        alpha = self.par["alpha0"]
        if self.rule == "Armijo":
            rho = self.par["rho"]
            beta = self.par["beta"]
            while self.f(x + alpha * h) >= self.f(x) + beta * alpha * self.grad(x).dot(h) or \
                 np.isnan(self.f(x + alpha * h)):
                alpha *= rho
                if alpha < 1e-16:
                    break
            return alpha
        elif self.rule == "Wolf":
            pass
        elif self.rule == "Goldstein":
            pass
        elif self.rule == "Wolf strong":
            pass