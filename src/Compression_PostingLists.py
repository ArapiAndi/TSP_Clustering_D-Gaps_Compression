from src.codings.Elias import Elias_coding
from src.codings.VariableLength import VB_coding

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
