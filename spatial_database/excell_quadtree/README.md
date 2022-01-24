# Questions

You are given a simplified real-world database D of points-of-interests (POIs), such as 
restaurants, schools, shops, and bus stops. After removing all sensitive information, each record
contains only an ID and a location represented as (x, y) for its longitude and latitude values. In 
this assignment, you are asked to conduct an experimental study on the performance of spatial 
indexing methods on the given dataset and report your findings.

In this assignment, an index is defined in the form of a list of (r, b) pairs, where r is a rectangle 
and b is a pointer to a bucket that holds all points in D inside r. Rectangle r is called the index 
cell. A search is done by first locating all necessary r rectangles according to the query, and then 
checking the points in each relevant rectangle. The capacity of each bucket is fixed at 256 (that is, 
a bucket can hold no more than 256 points).

We will only process window queries.

This assignment only considers a simplified scenario where all the data are loaded into memory. 
That is, no disk-based operations will be considered.

**Task 1** Write a program to compute and report the MBR for the POI dataset D.

**Task 2** Create an in-memory index for D. The index cells are obtained following 
EXCELL idea. The number of cells must be n x n, where n is the minimum integer that ensures 
no bucket exceeds its capacity. That is, we have the equal-sized internals for the x-axis and y-axis.

(1) Write a program to create an EXCELL index. Report the value of n, and the 
numbers of the cells which contain 0, 1-25, 26-239, 240-255 and 256 points respectively.

(2) Write a program to perform window queries based on the index you created in 
the previous step (to return the number of points inside a query window). 

(3) Generate 10 random window queries, run your search program, and report the 
number of points inside each query window, the number of index cells and the number of 
points searched for each query respectively. 

**Task 3** Create an in-memory index for D as in Task 2, but this time the index cells are 
obtained following the quad-tree decompaction. Let m be the minimum level of decompaction 
required such that no bucket exceeds its capacity.

(1) Write a program to create an index based on quad-tree decompaction. Report 
the value of m, and as in Task 2, the numbers of the cells which contain 0, 1-25, 26-239, 
240-255 and 256 points respectively.

(2) As in Task 2, write a program to perform window queries based on the index 
you created in the previous step (to return the number of points inside a query window). 

(3) Use the same 10 window queries used in Task 2, run your search program, and 
report the number of points inside each query window, the number of index cells and the 
number of points searched for each query respectively.

### Notes for notebooks
'A1_cwmakah_20801333_code.ipynb' is the major source code.

'A1_cwmakah_20801333_Task4_experiment.ipynb' is only for experiment in Task 4.
It tests the time to add 100 random points into EXCELL and quad-tree respectively.
The result is at the bottom of notebook.

For both .ipynb files, please use Jupyter Notebook to open and run from the top to the bottom (or run whole notebook).

And please ensure the dataset 'AllPOI Simplified.csv' is under the same directory.
