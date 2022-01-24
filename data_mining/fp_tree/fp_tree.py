import numpy as np

def powerset(s):
    # Generate all possible subsets of a set
    if len(s) <= 1:
        yield s
        yield []
    else:
        for item in powerset(s[1:]):
            yield [s[0]]+item
            yield item

def Load_data(filename, threshold):
    # Read file and clean data
    with open(filename, newline = '') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    Transaction = []
    ItemSupport = {}
    linkDict = {}
    # Iterate each row of csv file
    for i in range(0, len(content)):
        # Filter the last entry of each row which is a '' and sort by alphabetical order
        row_cleaned = sorted(content[i].split(",")[0:-1]) 
        for item in row_cleaned:
            # Insert items in support summary
            if item not in ItemSupport.keys():
                ItemSupport[item] = 1
            else:
                ItemSupport[item] += 1
        Transaction.append(row_cleaned)
    # Deduce the ordered frequent items
    infreqList = []
    for key, value in ItemSupport.items():
        if value < threshold:
            infreqList.append(key)
    for tran in Transaction:
        for item in tran:
            if item in infreqList:
                # Delete infrequent items in each row
                tran.remove(item)
                # Delete infrequent items in support summary
                del ItemSupport[item] 
            else:
                if item not in linkDict.keys():
                    linkDict[item] = LinkList()
    return Transaction, ItemSupport, linkDict

class Node():
    def __init__(self, item = 0):
        # initialize Node
        self.item = item
        self.count = 1
        self.children = {}
        self.parent = None
    
    def addCount(self):
        # Use for adding count within Node
        self.count += 1

    def addChild(self, item):
        # Add child node if it does not exist in children, and link to the next node
        if item not in self.children.keys():
            self.children[item] = Node(item)
            self.children[item].parent = self
            linkDict[item].linkNext(self.children[item])           
        else:
            # Add count if child exists
            self.children[item].addCount()
        
        
class fpTree():
    def __init__(self):
        self.root = Node()

    def insertCand(self, trans):
        # build the tree from top to bottom
        cur = self.root
        for tran in trans:
            cur.addChild(tran)
            cur = cur.children[tran]
    
    def tracePath(self, key, node, summary):
        '''
        Trace the path from bottom (leaf) to top (root)
        Filter the empty result in powerset
        Add the matched subset into summary; if existed, add the count in corresponding key of summary
        '''
        itemList = []
        count_sum = node.count
        while node != self.root:
            itemList.append(node.item)
            node = node.parent
        for i in powerset(sorted(itemList)):
            i = tuple(i)
            if len(i) < 1:
                continue
            elif len(i) == 1 and i != (key,):
                continue
            elif i in summary:
                summary[i] += count_sum
            else:
                summary[i] = count_sum
        return summary

class LinkNode:
    def __init__(self, node):
        self.node = node
        self.next = None
    
class LinkList:
    def __init__(self):
        self.next = None
    
    def linkNext(self, node):
        while self.next != None:
            self = self.next
        self.next = LinkNode(node)

if __name__ == "__main__":
    filename = './DataSetA.csv'
    threshold = 2500
    Transaction, ItemSupport, linkDict = Load_data(filename, threshold)
    Tree = fpTree()
    for candidate in Transaction:
        Tree.insertCand(candidate)
    sum = 0
    resultDict = {}
    for key, linkList in linkDict.items():
        summary = {}
        while linkList.next != None:
            linkList = linkList.next
            if not linkList.node:
                continue
            summary = Tree.tracePath(key, linkList.node, summary)
        for key in summary:
            # Filter the result by threshold
            if summary[key] < threshold:
                continue
            else:
                # Store the filtered result in a new dictionary
                resultDict[key] = summary[key]
                sum += 1
    # Sort the new dictionary in descending order of support count
    resultDict_sorted = dict(sorted(resultDict.items(), key = lambda item: item[1], reverse = True))
    for result in resultDict_sorted:
        # Print the result with required format
        print('{item}: {support}'.format(item = result, support = resultDict_sorted[result]))
    print('There are', sum, 'frequent itemsets with support >= 2500 in dataset.')