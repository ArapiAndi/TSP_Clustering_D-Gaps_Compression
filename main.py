import operator
import sys
import time

# implanted functions
from src.Clustering import do_clustering
from src.Compression_PostingLists import compression_posting_list
from src.CreateDictionary import create_dictionary
from src.Remapping import tsp_medoids_mapping, get_remapping_dictionary

RADIUS = [.99]

if __name__ == '__main__':

    print("Wait! The results will saved after execution in \'data/results/result.txt\'....")

    f = open("data/results/result.txt", 'w')
    sys.stdout = f

    # read dictionary
    d, n = create_dictionary()

    print("\n\n")

    # order the postings list of the dictionary in increasing order
    d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=False))

    # apply the VB, Elias Gamma, Elias Delta Encoding of the posting lists
    c1 = compression_posting_list(d)
    print("|Without TSP|", c1)

    # apply TSP-Clustering producing the new inducted number of documents by the similarity
    for r in RADIUS:
        start_time = time.time()
        medoids, clusters = do_clustering(d, n, r)
        print("\n With radius: ", RADIUS, " the number of medoids are: ", len(medoids))
        mapping = tsp_medoids_mapping(medoids, clusters, n)

        # get rempped dictionary with posting list sorted, gap motivation
        new_d = get_remapping_dictionary(d, mapping)

        # apply the VB, Elias Gamma, Elias Delta Encoding of the TSP mapping posting lists

        c2 = compression_posting_list(new_d)

        print("|With TSP|", c2)

        print("Finish: ", "%s seconds" % round(time.time() - start_time, 2))
    f.close()
