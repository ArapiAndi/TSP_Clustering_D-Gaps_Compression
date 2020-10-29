from src.TSP import call_TSP


def get_mapping_docID(tsp_medoids_order, medoids, clusters, n):
    mapping_doc_id = [0 for i in range(n)]
    new_doc_id = 0

    for i in tsp_medoids_order:
        doc_id, _, cluster_id = medoids[i]
        mapping_doc_id[doc_id] = new_doc_id
        new_doc_id += 1
        for cluster in clusters[cluster_id]:
            mapping_doc_id[cluster] = new_doc_id
            new_doc_id += 1
    return mapping_doc_id


# permit to obtain the mapping, documents with same similarities
def tsp_medoids_mapping(medoids, clusters, n):
    ordered_medoids = call_TSP(medoids)
    # print("TSP medoids order: ", ordered_medoids)
    mapping = get_mapping_docID(ordered_medoids, medoids, clusters, n)
    return mapping


def get_remapping_dictionary(dictionary, mapping):
    new_dictionary = {}
    for term in dictionary:
        new_posting = []
        for posting in dictionary[term]:
            new_posting.append(mapping[posting - 1])
        new_dictionary[term] = sorted(new_posting)
    return new_dictionary
