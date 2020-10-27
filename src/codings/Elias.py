import math

def Unary(x):
    return (x - 1) * '0' + '1'


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
    return elias_generic(Elias_Gamma, x)


def Elias_Gamma(x):
    return elias_generic(Unary, x)



