import numpy
from tsp_solver.greedy import solve_tsp
from src.Clustering import distance_jaccard



def tsp_medoids(termsID_medoid, n):
    termsID_medoid = [m[0] for m in termsID_medoid]
    graph_matrix = numpy.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            graph_matrix[i][j] = distance_jaccard(termsID_medoid[i], termsID_medoid[j])
    return solve_tsp(graph_matrix)


def get_docs_ids_mapping(n, path, medoids, clusters):
    mapping_doc_id = [0 for i in range(n)]
    new_doc_id = 1
    for i in path:
        medoid, cluster_id, doc_id = medoids[i]
        mapping_doc_id[doc_id] = new_doc_id
        new_doc_id += 1
        for cluster in clusters[cluster_id]:
            mapping_doc_id[cluster] = new_doc_id
            new_doc_id += 1
    return mapping_doc_id


# permit to obtain the mapping, documents with same similarities
def tsp_medoids_ordering(medoids, n, clusters=None):
    ordered_medoids = tsp_medoids(medoids, n)  # apply TSP
    print(ordered_medoids)
    # mapping_doc_ids = get_docs_ids_mapping(n, path, medoids, clusters)
    # return mapping_doc_ids
