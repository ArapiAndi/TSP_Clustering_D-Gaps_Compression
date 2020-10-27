import math


def d_gap(postings):
    i = 1
    d_gap_postings = [postings[0]]
    for current in postings[1:]:
        gap = current - d_gap_postings[i - 1]
        d_gap_postings.append(gap)
        i += 1
    return d_gap_postings


def VB_coding(dictionary):
    compressed_posting = []
    for term in dictionary:
        values = 0
        for posting in d_gap(dictionary[term]):
            values += math.ceil(math.log2(posting + 1)) / 7
        compressed_posting.append(values / 8)
    return round(sum(compressed_posting) / len(compressed_posting), 2)
