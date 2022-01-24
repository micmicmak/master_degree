# Implementation of Adaboost
Dataset consists of 10 data and 2 labels.

| # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| - | - | - | - | - | - | - | - | - | - | - |
| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| y | 1 | 1 | -1 | -1 | -1 | 1 | 1 | -1 | -1 | 1 |

We assume the weak classifier is produced by x < v or x > v where v is the threshold and makes
the classifier get the best accuracy on the dataset. You should implement the AdaBoost algorithm
to learn a strong classifier.
