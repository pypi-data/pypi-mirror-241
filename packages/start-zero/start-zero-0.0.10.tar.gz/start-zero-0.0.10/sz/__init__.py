import numpy as np

from sz.accelerate.cuda import CUDA
from sz.core.config import Config
from sz.core.tensor import Tensor
from sz.core.numericaldiff import NumericalDiff
from sz.ds.queue import PriorityQueue
from sz.ds.stack import Stack

from sz.functions.ft0 import sum_to, broadcast_to, sum, average, matmul, transpose, reshape, linear
from sz.functions.ft0 import SumTo, BroadcastTo, Sum, MatMul, Transpose, Reshape, Linear
from sz.functions.ft1 import setup_tensor
from sz.functions.ft1 import add, sub, mul, div, power, neg, mod
from sz.functions.ft1 import Add, Sub, Mul, Div, Power, Neg, Mod
from sz.functions.ft2 import sin, cos, tan, tanh
from sz.functions.ft2 import Sin, Cos, Tan, Tanh
from sz.functions.ft3 import exp, lg, ln
from sz.functions.ft3 import Exp, Lg, Ln
from sz.functions.ft4 import sigmoid, relu, softmax, log_softmax, leaky_relu, step
from sz.functions.ft4 import Sigmoid, ReLU, Softmax, LogSoftmax, LeakyReLU
from sz.functions.ft5 import mean_squared_error, softmax_cross_entropy, sigmoid_cross_entropy, binary_cross_entropy
from sz.functions.ft5 import MeanSquaredError, SoftmaxCrossEntropy
from sz.functions.ft6 import max, min, clip, batch_norm
from sz.functions.ft6 import Max, Min, Clip, BatchNorm
from sz.functions.ft7 import accuracy, dropout, embed_id

setup_tensor()


def is_tensor(obj):
    """
    判断对象是不是Tensor对象
    :param obj: 要判断的对象
    :return: True：是Tensor对象；False：不是Tensor对象
    """
    return isinstance(obj, Tensor)


def as_nparray(obj):
    """
    将对象转化为numpy的数组
    为什么需要转化：
    x = np.array(0.5)
    y = np.array([0.5])
    x = x + 1
    y = y + 1
    print(np.isscalar(x))  # True
    print(np.isscalar(y))  # False
    ----------
    a = np.array(10)
    b = np.array([4])
    c = 10
    print(np.isscalar(a), np.isscalar(b), np.isscalar(c))  # False False True
    :param obj: 要转化的对象
    :return: 转化后的对象
    """
    if np.isscalar(obj):
        return np.array(obj)
    return obj


def to_tensor(obj):
    """
    将对象转化为Tensor对象
    :param obj: 要转化的对象
    :return: 转化后的对象
    """
    obj = as_nparray(obj)
    if not is_tensor(obj):
        obj = Tensor(obj)
    return obj


def clear_tensors(*tensors):
    for tensor in tensors:
        tensor.clear_tensor()
