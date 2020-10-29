# Compression of Posting Lists  with Clustering and TSP



```
Arapi Andi
Venice,
October 27, 2020
```

### Introduction
The purpose of this project is to using a docID assignment technique that combines 
clustering and TSP in order to compress the posting lists of an inverted index. The compression technique can be 
summarized in four steps:
1.  Transform each document into a set of termIDs
2.  Reorder the collection according to the document length 
(in reverse order) and scan linearly  the  collection  of  document  to  cluster  them  using  the  Stream  Clustering
algorithm 1
3.  Exploit TSP to order clusters. The heuristics computes a pairwise distance between every pairs of medoids 2 using
 Jaccard distance, and then finds the shortest pathtraversing the medoids in the graph;
4.  Suboptimal cycle found is finally broken at some point, and docIDs assigned lin-early cluster by cluster, using the
  TSP-induced order.  Within each cluster docIDsare assigned with respect to the insertion order (document length order)


### Getting Started
The program is implemented in Python 3.7 and the perquisites are have installed the follow package:

* ortools.constraint\_solver
* numpy 1.18+


### How to use
For practical reasons I used the dataset locally, so in order to execute different documents in the program,
it is necessary to place them in the path 'data/documents/' in '.dat' forma . The value of the **radius** can
as well be changed, specifically at **row 11** in _main.py_. I save the result of computation in the path 'data/result.txt'
 with information about the radius, number of medoids and performance of compression.

### Results
This section presents the results in terms of compression power of the docID
assignment technique based on clustering and TSP. The compression power
have been determined relatively to the docID assignment order used by the
SPIMI indexing algorithm, i.e. when the docIDs are assigned in the same order
in which the documents are stored in the files. 

All the tests have been performed using the document collection available at path 'data/documents' with the follow characteristic:
```
Total no. of documents: 23.810
Total no. of terms: 48.948
Total no. of postings: 1.813873
```

 
Given the posting lists I use  Variable Length, Elias Gamma and Delta for the compression of gaps, the average of byte 
per posting is reported in the follow table: 


|Coding |AVG. Byte|
|-----|--------|
|VB |73.76|
|Elias Gamma |112.49|
|Elias Delta |86.24|

With Radius=0.99 I have 15 medoids with the follow characteristics:

|Coding |AVG. Byte|Performance|
|-----|--------|--------------|
|VB |72.69|1.45%|
|Elias Gamma |103.41|8.07%|
|Elias Delta | 81.24| 5.79%|

With Radius=0.96 I have x medoids with the follow characteristics:

|Coding |AVG. Byte|Performance|
|-----|--------|--------------|
|VB |72.59| 1.58% |
|Elias Gamma |103.35 | 8.12% |
|Elias Delta | 81.18 | 5.86% |

### Conclusions

Small radius increases number of clusters which reduce space occupied by postings but increase the computational time for the clustering and TSP which is a 
NP-HARD problem, I have summarize as follow the property. 

```
|Pro|
- Simple method
- Efficent
```
```
|Cons|
- Converges to a local minimum of the error function
- Sensitive to initialization
- TSP is very heavy time consuming
```

### Future Implementation

The future improvement will be:

* **Clustering**: apply different type of distance.
* **Find Optimal Radius**: create model of a better optimization problem.
* **Efficiency TSP**: biggest problem, that reduce computation, we must have better
hardware or using parallelization to reduce.

