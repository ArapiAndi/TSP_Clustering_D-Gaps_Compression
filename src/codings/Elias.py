import math
import numpy as np


def Unary(x):
    u = np.ones(x + 1)
    u[x] = 0
    s = ""
    for elem in u:
        s = s + str(int(elem))
    return s


def Binary(x, l=1):
    s = '{0:0%db}' % l
    return s.format(x)


def elias_generic(lencoding, x):
    if x == 0:
        return '0'

    l = 1 + int(math.log2(x))
    a = x - 2 ** (int(math.log2(x)))

    k = int(math.log2(x))

    return lencoding(l) + Binary(a, k)


def Elias_Delta(x):
    off = Binary(x)[1:]
    return Elias_Gamma(len(off)) + off


def Elias_Gamma(x):
    off = Binary(x)[1:]
    return Unary(len(off)) + off


