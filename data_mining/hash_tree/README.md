# Hash Tree

Suppose we have 31 candidate item sets of length 3:

{1 2 3}, {1 4 5}, {1 2 4}, {1 2 5}, {1 5 9}, {1 3 6},

{2 3 4}, {2 5 9}

{3 4 5}, {3 5 6}, {3 5 9}, {3 8 9}, {3 2 6}

{4 5 7}, {4 1 8}, {4 7 8}, {4 6 7}

{6 1 3}, {6 3 4}, {6 8 9}, {6 2 1}, {6 4 3}, {6 7 9}

{8 2 4}, {8 9 1}, {8 3 6}, {8 3 7}, {8 4 7}, {8 5 1}, {8 3 1}, {8 6 2}

Please write a program to generate a hash tree with max leaf size 3, output the 
nested list (or nested dict) of the hash tree hierarchically and draw the structure of 
the hash tree (you can write program to draw this hash tree or just manually draw it 
according to the nested list you output). 
