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


def Elias_Delta(x):
    off = Binary(x)[1:]
    length = len(off)
    return Elias_Gamma(length) + off


def Elias_Gamma(x):
    off = Binary(x)[1:]
    length = len(off)
    return Unary(length) + off
