# Compression of D-gaps Posting Lists with Clustering and TSP method

```
Arapi Andi
27/10/2020, Italy (Venice)
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
The program is implemented in Python 3.7 and the perquisites are have installed the following package:

* ortools.constraint\_solver
* numpy 1.18+


### How to use
For practical reasons I used the dataset locally, so in order to execute different documents in the program,
it is necessary to place them in the path 'data/documents/' in '.dat' form . The value of the **radius** can
as well be changed, specifically at **row 11** in _main.py_. I save the computational results in the path 'data/result.txt'
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
per posting is reported in the following table: 


|Encoding |AVG. Byte|
|-----|--------|
|VB |73.76|
|Elias Gamma |112.49|
|Elias Delta |86.24|

With Radius=0.99 I have 15 medoids with the following characteristics:

|Encoding |AVG. Byte|Performance|
|-----|--------|--------------|
|VB |72.69|1.45%|
|Elias Gamma |103.41|8.07%|
|Elias Delta | 81.24| 5.79%|

With Radius=0.96 I have x medoids with the following characteristics:

|Encoding |AVG. Byte|Performance|
|-----|--------|--------------|
|VB |72.59| 1.58% |
|Elias Gamma |103.35 | 8.12% |
|Elias Delta | 81.18 | 5.86% |
  
<br></br>  
**Compression power** for measuring the compression power of the docID assignment topic of this document, the average 
number of bits per d-gap is computed using Variable Byte, Elias Gamma and Elias Delta encodings first with
and then without using the compression algorithm. Table 1 presents the average number of bits per d-gap when the 
compression algorithm is not used. The best one is by far the Varaible Length encoding.
Table 2 and 3 show the average number of bits per d-gap when the compression algorithm is used with the radius parameter
 of the clustering algorithm
respectively set to 0.99 and 0.98. The lower this hyper-parameter is,
the better the results are and it is possible to notice that the best improvements
are always given when Elias Gamma and Elias Delta code are used. Indeed bit-level codes
<br></br> <br></br> 

**Radius hyperparameter** implies reductions a lower variance and and
better results in terms of compression power but on the other hand leads to an
increase of the computational time for both clustering and TSP, since an higher
number of clusters is obtained.



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

