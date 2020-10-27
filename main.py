import operator

# implanted functions
from src.Clustering import do_clustering
from src.CompressionsPostingList import compression_posting_list
from src.CreateDictionary import create_dictionary
from src.TSP import tsp_medoids_ordering

RADIUS = [.99]

if __name__ == '__main__':
    d, n = create_dictionary()

    # order the postings list of the dictionary in increasing order
    d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=False))

    # apply the VB, Elias Gamma, Elias Delta Encoding of the posting lists
    # compression_posting_list(d)

    # apply TSP-Clustering producing the new inducted number of documents by the similarity
    for r in RADIUS:
        medoids, clusters = do_clustering(d, n, r)
        print(tsp_medoids_ordering(medoids, n))

    # apply the VB, Elias Gamma, Elias Delta Encoding of the posting lists

    # extract the avg. of bytes and improvement
