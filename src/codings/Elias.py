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

    return len(lencoding(l) + Binary(a, k))


def Elias_Delta(x):
    return elias_generic(Elias_Gamma, x)


def Elias_Gamma(x):
    return elias_generic(Unary, x)


def Elias_coding(dictionary, isGamma=True):
    if isGamma:
        coding = Elias_Gamma
    else:
        coding = Elias_Delta

    compressed_posting = []
    for term in dictionary:
        values = 0
        for posting in dictionary[term]:
            values += coding(posting)
        compressed_posting.append(values / 8)
    return round(sum(compressed_posting) / len(compressed_posting), 2)
