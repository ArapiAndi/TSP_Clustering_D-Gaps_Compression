import math


def d_gap(postings):
    i = 1
    d_gap_postings = [postings[0]]
    for current in postings[1:]:
        d_gap_postings.append(current - d_gap_postings[i - 1])
        i += 1
    return d_gap_postings


def VB_coding(dictionary):
    compressed_posting = []
    for term in dictionary:
        values = 0
        for posting in d_gap(dictionary[term]):
            values += (int(math.log2(posting)) / 7)
        compressed_posting.append(values / 8)
    return round(sum(compressed_posting) / len(compressed_posting), 2)


COMPRESSIONS = {"VB": VB_coding}


def compression_posting_list(dictionary):
    for methods in COMPRESSIONS:
        print("Compression of posting list with ", methods)
        print(COMPRESSIONS[methods](dictionary))
