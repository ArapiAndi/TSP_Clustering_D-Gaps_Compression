# Compression of Posting Lists  with Clustering and TSP



```
Arapi Andi
Venice,
October 27, 2020
```

### Introduction
The purpose of this project is to describe the results obtained using a docID assignment technique that combines 
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
For practical reasons I used the dataset locally, so in order to execute the program,
it is necessary to place them in the path 'data/documents/' in format '.dat' . The value of the **radius** can
as well be changed, specifically at **row 11** in _main.py_. I save the result of computation in the path 'data/result.txt'
 with information about the radius, number of medoids and performance of compression.
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

