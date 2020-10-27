import math

from src.codings.Elias import Elias_Gamma, Elias_Delta

DIM_INT = 32
DIM_VB = 7


def d_gap(postings):
    i = 1
    d_gap_postings = [postings[0]]
    for current in postings[1:]:
        gap = current - d_gap_postings[i - 1]
        d_gap_postings.append(gap)
        i += 1
    return d_gap_postings


def Elias_coding(dictionary, isGamma=True):
    if isGamma:
        coding = Elias_Gamma
    else:
        coding = Elias_Delta

    compressed_posting = []
    for term in dictionary:
        values = 0
        for posting in d_gap(dictionary[term]):
            values += len(coding(posting)) / DIM_INT
        compressed_posting.append(values)
    return round(sum(compressed_posting) / len(compressed_posting), 2)


def VB_coding(dictionary):
    compressed_posting = []
    for term in dictionary:
        values = 0
        for posting in d_gap(dictionary[term]):
            values += math.ceil(math.log2(posting + 1)) / DIM_VB
        compressed_posting.append(values)
    return round(sum(compressed_posting) / len(compressed_posting), 2)


COMPRESSIONS = {"VB": VB_coding, "Elias_Gamma": Elias_coding, "Elias_Delta": Elias_coding}


def compression_posting_list(dictionary):
    val = []
    print("Compression of posting list with: ", COMPRESSIONS.keys())
    for methods in COMPRESSIONS:
        if methods == "Elias_Delta":
            val.append(COMPRESSIONS[methods](dictionary, False))
        else:
            val.append(COMPRESSIONS[methods](dictionary))
    return val
