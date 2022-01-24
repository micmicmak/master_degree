# R-tree and NN search

We will continue to use the POI dataset D used in EXCELL and quad-tree.

**Task 1** R-tree implementation.

(1) Write a program to create an R-tree index for point data in-memory. The 
fan-out of the tree should be d (i.e., a non-leaf node can have a maximum of d
MBRs/subtrees), and each leaf node can contain a maximum of n points (i.e., the 
bucket size is n), where both d and n are user-given parameters.

(2) Provide a concise outline of the algorithm you implement, with sufficient 
plain English comments such that your code can be easily understood by other people.

(3) Using the program developed in Task 1 to create an R-tree index for the 
POI dataset D, and report the following statistics for n=128 and 256 and d = 2 and 5
(i.e., 4 cases):

a. the height of your R-tree index.

b. the numbers of non-leaf and leaf nodes.

c. space utilisation for leaf nodes(i.e., the number and percentage of buckets 
in the following utilisation ranges: less than 20%, 20~80%, more than 80%). 

d. sub-tree overlapping among the non-leaf nodes (i.e., the total number of 
MBR pairs which belong to the same non-leaf node and overlap).

**Task 2** NN search.

(1) Write a program that can find the nearest neighbour of a given query point based 
on the R-tree implemented in Task 1 using the algorithm with the three pruning rules 
discussed in this course. We use L2 distance in this task.

a) Input: a query point q.

b) Output: a point p in D that is the nearest neighbour of q.

(2) Please describe concisely the algorithm you implement in your program, with 
sufficient plain English comments such that your code can be easily understood by other 
people.

(3) Run the nearest neighbour program you implemented above, and report, for 
n=128 and 156, d = 2 and 5, and 10 random query points, the following statistics for each 
experiment (there are a total of 2x2x10=40 sets of experiments):

a. The nearest neighbour result p and its L2 distance to q.

b. The number of R*-tree nodes visited. 

c. The number of points where the actual distance to q is calculated.

d. The number of MBRs that have been pruned out using each of the three 
pruning rules. 
