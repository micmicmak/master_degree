import numpy as np

class Node():
	def __init__(self, set, depth):
		# Initialize Node
		self.set = [set]
		self.children = {}
		self.depth = depth
		
	def addCandidate(self, set):
		'''
		Add candidates into set no matter the number of them exceeds the max. leaf size
		Check the length of set
		If the length exceeds max. leaf size, split the node
		'''
		self.set.append(set)
		if len(self.set) > 3:
			self.splitNode()

	def splitNode(self):
		# Link to the next list when the list = 3
		if self.depth == 3:
			self.linkNext()
			return
		for candidate in self.set:
			# Hash the corresponding digit of candidate
			code = candidate[self.depth] % 3
			if code in self.children: # check whether has this child node
				self.children[code].addCandidate(candidate)
			else:
				self.children[code] = Node(candidate, self.depth+1)
		# Clear the node
		self.set = []
		# Split the node of children if the length exceeds max. leaf size
		for child in self.children.values():
			if len(child.set) > 3:
				child.splitNode()

	def linkNext(self):
		#　Handle the case when the 3-level node has more than 3 candidates
		curSet = self.set
		next = self.set[2:]
		self.set = self.set[0:2]
		self.set.append(next)

class Tree():
	def __init__(self, set):
		self.root = Node(set, 0)

	def insertNode(self, set):
		# Check which node should be inserted
		depth = 0
		cur = self.root
		# Loop through the nodes and find the bottom node, with correct child in hash
		while len(cur.children) > 0:
			code = set[depth] % 3
			if code in cur.children:
				cur = cur.children[code]
				depth += 1
			else:
				cur.children[code] = Node(set, depth+1)
				return
		# Add the candidate in current node
		cur.addCandidate(set)

	def printTree(self, node = Node):
		if not node.set:
			# print output for normal nodes, which number of candidates <= max. leaf size
			if not node.children:
				return
			else:
				res = []
				for item in node.children.values():
					res += [self.printTree(item)]
		else:
			# Adjust the output format of linked list following the requirements in important notes
			s = ""
			if len(node.set) > 2:
				if np.array(node.set[2]).shape == (2, 3):
					tmp = node.set[2]
					node.set = node.set[0:2]
					s += "a link list a' (a': "
					for i in range(len(tmp)):
						if i < len(tmp) - 1:
							s += str(tmp[i]) + "->"
						else:
							s += str(tmp[i]) + ")"
					node.set.append(s)
			return node.set
		return res

# Input candidates
input = [[1, 2, 3], [1, 4, 5], [1, 2, 4], [1, 2, 5],
		[1, 5, 9], [1, 3, 6], [2, 3, 4], [2, 5, 9],
		[3, 4, 5], [3, 5, 6], [3, 5, 9], [3, 8, 9],
		[3, 2, 6], [4, 5, 7], [4, 1, 8], [4, 7, 8],
		[4, 6, 7], [6, 1, 3], [6, 3, 4], [6, 8, 9],
		[6, 2, 1], [6, 4, 3], [6, 7, 9], [8, 2, 4],
		[8, 9, 1], [8, 3, 6], [8, 3, 7], [8, 4, 7],
		[8, 5, 1], [8, 3, 1], [8, 6, 2]]
# Sort within single candidate
for i in input:
	i.sort()
# Delete duplicated candidates
a = np.array(input)
input_cleaned = np.unique(a, axis = 0).tolist()

if __name__ == "__main__":
	obj = Tree(input_cleaned[0])
	for i in range(1, len(input_cleaned)):
		obj.insertNode(input_cleaned[i])
	print(obj.printTree(obj.root))