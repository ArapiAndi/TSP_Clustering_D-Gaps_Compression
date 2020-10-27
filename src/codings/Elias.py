import math
import numpy as np


def Unary(x):
    u = np.ones(x + 1)
    u[x] = 0
    s = ""
    for elem in u:
        s = s + str(int(elem))
    return s


def offset(x):
    for i in range(len(x)):
        if x[i] == '1':
            x = x[1:]
            break
        x = x[1:]
    return x


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
    b = Binary(x)
    return Elias_Gamma(len(offset(b))) + offset(b)


def Elias_Gamma(x):
    off = offset(Binary(x))
    return Unary(len(off)) + off



