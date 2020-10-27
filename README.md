# Report: Project Information Retrivial



```
Arapi Andi
Venice,
October 27, 2020
```



## Contents

- 1 Requirments
   - 1.1 Clustering Document to Compress Inverted Index
- 2 Designing Solution
   - 2.1 Create Dictionary System
   - 2.2 Clustering System
   - 2.3 TSP
   - 2.4 Compression System
   - 2.5 Analysis
- 3 Results
   - 3.1 First Test
   - 3.2 Second Test
   - 3.3 Conclusions
      -


# Chapter 1

# Requirments

Given aDictionarywhere:

- Keys: are terms in document collection
- Velues: are posting list of term

Apply the posting list d-gap compression to reduce the space occupied with a more
efficent compression re-defining the docID by the similairity of documents avoiding to
have large docID distance.

### 1.1 Clustering Document to Compress Inverted Index

## dex

Aim: Permut the DocID to increase the frequency of small d-gaps.
Clusteringis the process of grouping a set of objects into a class of similar objects.
Similarity is defined by theJaccard Distancewhere is:

```
jaccarddistance(A, B) = 1−
```
#### |A∩B|

#### |A∪B|

The Algorithm steps are:

1. Createdictionary from a collection of Documents
2. Trasformeach Document into a set of termIDs (as Points)
3. Reordercollection of docIDs-termIDs in order of length
4. Scan linearily andClusteringthem using Jaccard Distance
5. Apply TSPusing Jaccard Distance to the medoids
6. Assignsnew DocID using TSP-induced Order
7. Apply d-gaps compressionto the posting list

# Chapter 2

# Designing Solution

The System is implemented inPythonlanguage and the principal files are:

- creatdictionary.py: contains the functions of the Create Dictionary System.
- clustering.py: contains the functions of the Clustering System.
- compression.py: contains the the functions of the Compression System.
- anlaysis.py: permit to calculate compression and plot results as Analysis System.

### 2.1 Create Dictionary System

Is implemented in createdictionary.py and the principal steps are:

1. Create dictionary from a document set with SPIMI method.


#### 2.2. CLUSTERING SYSTEM 5

2. Save dictionary in two file txt, lexicon and posting.

The principale function are:

- createindex(dictionary): given the dictionary, save in two files .txt, lexicon and
    posting list.
- readindex(): from posting.txt and lexicon.txt permit to create a dictionary.
- SPIMIindexer(documentscollection): given documents collection permit to crate
    a dicitionary in lexicographic ordering with keys terms and values posting list,
    return dictionary and number of documents.

### 2.2 Clustering System

Is implemented in clusters.py and the principal steps are:

1. Create doc-termsID set and ordered by length.
2. Find the Medoids and Clusters using Jaccard Distance saving it respectively a in
    Lists of clusters and medoids.


#### 6 CHAPTER 2. DESIGNING SOLUTION

The principale functions are:

- getdocssettermsid(dictionary, n): given a dictionary and number of documents,
    create a set of docs with termID (postion ordering) and return the list of doc-
    termsIDsortedby length.
- streamcluster(sortedcollection, radius): given sorted doc-termsID and radius (as
    dissimilarity accepted), return Medoids List and Clustering Dictionary.
- findmedoids(medoids, doctermsID): given set of medoids and a specific doc-
    termsID, using the jaccard distance return the minimum distance and medoid
    (which have this distance).

### 2.3 TSP

We have importated library from Suboptimal Travelling Salesman Problem (TSP) solver,
in particular the function:

- tspsolver.greedy: greedy solution of TSP in Python.

To use the function we have:

1. Create adjacene matrix with jaccard distance weights.
2. Apply TSP solution to the matrix.


#### 2.4. COMPRESSION SYSTEM 7

The principals functions are:

- tspmedoids(medoids, n): given set medoids, transform in adjacence matrix and
    apply TSP to find the minimal path.

### 2.4 Compression System

Is implemented in the file compression.py and the steps are:

1. Create the mapping given Path TSP, List of Medoids and Dictionary of Clusters.
2. Given Dictionary, Mapping and d-gap, we create the compressed posting list and
    we save in file.


#### 8 CHAPTER 2. DESIGNING SOLUTION

The principal functions are:

- getdocidordering(path, medoids, clusters): permit to create the maping List
    lenght as maximum docID where elements are the new docID in the same cluster.
- computedgaps(docid1, docid2, dgap): permit to apply gap compression.
- reassigndocsid(dictionary, mapping, dgap): permit to obtain the posting lists of
    dictionary, apply mapping by similarity and compute compression.

### 2.5 Analysis

```
Figure 2.1: Analysis System
```
In the file analysis.py we have implement the follow functions:

- memorypostinglists(dictionary): for each posting list we calculate the memory
    request in bits for save the specific docID and dividing by 8 for find the Bytes.
- plotdistribution(y): given memory occupied by compressed Clustering TSP post-
    ing list we plot the distribution respect standard d-gap compression difference.


# Chapter 3

# Results

### 3.1 First Test

The Documents collection have the follow characteristics:

```
Documents Terms Postings
23.820 47.320 1.810.
```
```
After Computation we have the following results:
```
- STD D-Gap Compression:

```
Execution Time D-Gap Compressed
13.565 sec 1024 -64.45%
```
- Clustering TSP Compression:

#### 9


#### 10 CHAPTER 3. RESULTS

```
Execution Time Radius D-Gap Medoids Compressed
34,20 sec 0,98 1024 19 -43.34%
```
- Clustering TSP Compression Sorted:

```
Execution Time Radius D-Gap Medoids Compressed
22.467 sec 0,98 1024 272 -11.58%
```

#### 3.2. SECOND TEST 11

### 3.2 Second Test

The Documents collection have the follow characteristics:

```
Documents Terms Postings
605.757 240.142 46.935.
```
```
After Computation we have the following results:
```
- STD D-Gap Compression:

```
Execution Time D-Gap Compressed
291.389 sec 65536 -74.46%
```
- Clustering TSP Compression:


#### 12 CHAPTER 3. RESULTS

```
Execution Time Radius D-Gap Medoids Compressed
1564.647 sec 0,99 65536 29 -47.41%
```
### 3.3 Conclusions

Radius≈1 is better beacuse find find closer Clusters and with jaccard distance we put
closer DocId with index.
Pro:

- Very simple method
- Efficent

Cons :

- Converges to a local minimum of the error function
- Sensitive to initialization
- Only finds “spherical” clusters


