# Questions
### Q1. Given the following network, obtain the degree and clustering coefficient for each node.
![Alt text](./network.jpg?raw=true "network")

### Q2. In this question, you have to compare a real-world graph data set with the random graph using NetworkX.
(a) Wikipedia vote network dataset: It contains 7,115 nodes and 103,689 (directed) edges. The dataset
can be downloaded from http://snap.stanford.edu/data/wiki-Vote.html.

(i) Use the function nx.read edgelist() to load the dataset Wiki-Vote.txt.

(ii) Output the following information related to degree:

- average degree, average in-degree, average out-degree;
- degree distribution (plot both the degree and frequency in linear scale);
- degree distribution (plot both the degree and frequency in log scale);
- density (E/N2), where E is the number of edges, and N is the number of nodes;

(iii) Find the largest strongly connected component (giant component), and output the number of
nodes in it;

(iv) Output the following information about this giant component related to distance and clustering:
- distribution of path length
- average path length;
- distribution of clustering coefficient;
- average clustering coefficient.

(b) Random graph:
(i) Using the NetworkX function binomial graph, generate a random graph G1000,0.01.
- There are four arguments in binomial graph: (i) n: the number of nodes; (ii) p: probability
for edge creation; (iii) seed: seed for random number generator; (iv) directed: if True return
a directed graph.
- In this task, please set n = 1000, p = 0.01, seed=5008, directed=True.

(ii) Show the random graph obtained.

(iii) Repeat steps (ii)-(iv) in part (a).

(iv) Discuss the similarities and differences with the results obtained in part (a).

