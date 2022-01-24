# Build multilayer perception (MLP) neural network models by using PyTorch
As discussed in class, neural network classifiers generalize logistic regression by
introducing one or more hidden layers. Learning of both models may use a
(batch or stochastic) gradient descent algorithm by minimizing the cross entropy loss. It requires that the step size parameter be specified. Try out a
few values and choose one that leads to stable convergence. You may also decrease gradually during the learning process to enhance convergence. A common
criterion used for early stopping is when the improvement between iterations
does not exceed a small threshold or when the number of iterations has reached
a prespecified maximum. Since the solution found may depend on the initial
weight values chosen randomly, you may repeat each setting multiple times and
report the average classification accuracy.

## Binary Classifcation Data Sets
For 4 binary classifcation data sets, you are required to
construct a set of single hidden layer neural network models. The number
of hidden units H should be determined using cross validation. The generalization performance of the model is estimated for each candidate value. 
This is done by randomly sampling 80% of the training
instances to train a classifier and then testing it on the remaining 20%. Hence,
given 4 datasets, you are required to perform 4 such random data splits in order
to find the most suitable H for 4 data sets, respectively.
Subsequently, given any binary data set Di
, you are requied to train a neural
network classifier with Hi
hidden units in a single layer, which is trained from
scratch using all the training instances available.

## Multi-class Data Sets
For the multi-class data set, you are required to construct a set of two hidden
layers neural network models. The number of hidden units for first layer L1
is choosen from {15, 25, 50}, while the number of hidden units for second layer
L2 is choosen from {5, 10, 20}. Like the single layer NNMs above, the best
combination of hidden numbers for each layer is decided by cross validation
(randomly sampling 80% of the training instances to train a classifier and then
testing it on the remaining 20%).
