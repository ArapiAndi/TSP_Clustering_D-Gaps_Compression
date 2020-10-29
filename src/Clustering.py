"""
Structure of data:

docId_terms -> [(termsID,docID),....,(termsID,docID)]

medodis -> [(docID, termsID,clusterID),.....,(docID, termsId,clusterID)]

clusters -> [[docId,...,docID],.....,[docId,...,docID]]


"""

ROUND = 5  # float numbers round


def distance_jaccard(doc1, doc2):
    if doc1 and doc2:
        intersection_docs = list(set(doc1) & set(doc2))
        return round(1-len(intersection_docs) / (len(doc1 + doc2)), ROUND)
    else:
        return 1


def find_medoids(medoids, doc_terms):
    if not medoids:  # no clusters yet
        return 1, []
    doc_id, terms_id, cluster_id = medoids[0]  # given
    distance, k = distance_jaccard(terms_id, doc_terms), cluster_id
    for doc_id, terms_id, cluster_id in medoids[1:]:  # permit to select the minimum from all distance
        new_distance = distance_jaccard(terms_id, doc_terms)
        if new_distance < distance:
            distance = new_distance
            k = cluster_id
    return distance, k


def stream_cluster(docID_TermsID, radius):
    k = 0  # number of cluster

    medoids = []  # list of (doc-termsID,docID, clusterID)
    clusters = {}  # contain the dictionary with clusterID (0<=clusterID<=k) and values are list docs-termsID

    for doc in docID_TermsID:
        doc_terms_id, doc_id = doc
        distance, cluster_id = find_medoids(medoids, doc_terms_id)  # calculate the distance
        if distance <= radius:
            clusters[cluster_id].append(doc_id)  # add to cluster
        else:
            medoids.append((doc_id, doc_terms_id, k))  # create new cluster and medoid
            clusters[k] = []
            k += 1  # increment numbers of cluster
    return medoids, clusters


# return list of (doc-termsID,doc-ID)
def get_docs_set_terms_id(dictionary, n, is_reverse=True):
    list_of_terms_ids = [[] for i in range(n)]  # list of docs
    term_id = 0  # term-ID saved in the doc-terms vectors
    for term in dictionary:
        for doc_id in dictionary[term]:  # posting lists saved in the term
            list_of_terms_ids[doc_id - 1].append(term_id)  # add termID in the doc set
        term_id += 1
    docs_terms = [(list_of_terms_ids[doc_id], doc_id) for doc_id in range(n)]  # insert the docID
    if is_reverse:
        docs_terms.sort(key=lambda x: len(x[0]), reverse=is_reverse)  # ordering in reverse order length
    return docs_terms


def do_clustering(documents, n, radius):
    # create the hyper-points
    docID_Terms = get_docs_set_terms_id(documents, n)
    # check number of elements
    assert (len(docID_Terms) == n)
    return stream_cluster(docID_Terms, radius)
