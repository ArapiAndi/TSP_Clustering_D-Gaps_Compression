import operator

# implanted functions
from src.Clustering import do_clustering
from src.CompressionsPostingList import compression_posting_list
from src.CreateDictionary import create_dictionary
from src.Remapping import tsp_medoids_mapping, get_remapping_dictionary
from src.TSP import call_TSP

RADIUS = [.98, .97, .95]

if __name__ == '__main__':
    d, n = create_dictionary()

    # order the postings list of the dictionary in increasing order
    d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=False))

    # apply the VB, Elias Gamma, Elias Delta Encoding of the posting lists
    print("\n\n| Without TSP |")
    compression_posting_list(d)

    # apply TSP-Clustering producing the new inducted number of documents by the similarity
    for r in RADIUS:
        medoids, clusters = do_clustering(d, n, r)
        print("\n With radius: ", RADIUS, " the number of medoids are: ", len(medoids))
        mapping = tsp_medoids_mapping(medoids, clusters, n)

        # get rempped dictionary with posting list sorted, gap motivation
        new_d = get_remapping_dictionary(d, mapping)

        # apply the VB, Elias Gamma, Elias Delta Encoding of the TSP mapping posting lists
        print("\n\n| WITH TSP , RADIUS", r, " |")
        compression_posting_list(new_d)
