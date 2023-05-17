import sys
import time
import math
import numpy as np

def func1_op(x, y):
    op = np.power(x, 2) + np.power(y, 2) + 25*(np.power(np.sin(x), 2) + np.power(np.sin(y), 2))

    return op

def func2_op(x, y):
    op = -(y + 47) * np.sin(np.sqrt(np.abs(y + (0.5 * y) + 47))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

    return op

def get_func(a):
    #[name, lb, ub]
    param = { 0: ["func1_op", -5, 5],
              1: ["func1_op", -2, 2],
              2: ["func2_op", -512, 512],
              3: ["func2_op", 400, 512]
            }
    
    return param.get(a, "nothing")