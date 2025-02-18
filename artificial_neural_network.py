import numpy as np

# defining sigmoid function.
def sigmoid_func(x, derivative=False):
    if derivative:
        # derivative
        return x * (1 - x)
    #sigmoid function.
    return 1 / (1 + np.exp(-x))