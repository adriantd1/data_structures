class Node:	
	def __init__(self, value):
		self.value = value
		self.lChild = None
		self.rChild = None

class BinaryTree:	
	# Input: a node
	# Output: None
	# Instantiate the root of the Binary Tree as the input node
	def __init__(self,node):
		self.root = node
	
	# Input: a node to insert
	# Output: None
	# Insert the node "node" in the binary tree. The value of "node" does not have to
	# be distinct. If the tree already has a node with value "value", the new 
	# node will be inserted as its left child and the tree will be balanced accordingly
	def insert(self, node):
		cur = root
		while True:
			if node.value == cur.value:
				# If node.value = cur.value, assign cur.lChild = node
				node.lChild = cur.lChild
				cur.lChild = node
				return
			if node.value > cur.value:
				# insert on right subtree
				if cur.rChild == None:
					cur.rChild = node
					return
				else:
					cur = cur.rChild
			else:
				# insert on left subtree
				if cur.lChild == None:
					cur.lChild = node
					return
				else:
					cur = cur.lChild
	
	# Input: a value
	# Output: True if the tree contains a node with the value. False otherwise
	# Verifies if the tree has a node with the value "val"
	def find(self, val):
		cur = self.root
		while cur != None:
			if cur.value == val:
				return True
			elif cur.value > val:
				# search left subtree
				cur = cur.lChild
			else:
				# search right subtree
				cur = cur.rChild
		# No node of value "val" was found
		return False
		
	# Input: a value to delete
	# Output: None if the tree contains a node of value "val", error message otherwise
	# Search for the first instance of a node with value "val" and deletes it. If there
	# is no such node, output an error message
	def delete(self,val):
		# local functions to help finding the leftmost and rightmost child of a node
		def leftMost(node, parent):
			if node.lChild == None:
				return (node, parent)
			else:
				return leftMost(node.lChild, node)
		def rightMost(node, parent):
			if node.rChild == None:
				return (node, parent)
			else:
				return rightMost(node.rChild, parent)
				
		if not self.find(val):
			print("There is no node with this value in the tree")
			return
		
		cur = self.root
		# marker for the parent of cur
		parent = cur
		# loop to find the node to remove
		while True:
			if cur.value == val:
				break
			elif cur.value > val:
				parent = cur
				cur = cur.lChild
			else:
				parent = cur
				cur = cur.rChild
		if cur.lChild == None and cur.rChild == None:
			# if cur is a leaf
			if cur.value> parent.value:
				parent.rChild = None
			else:
				parent.lChild = None
		elif cur.lChild == None or cur.rChild == None:
			# if cur has one child
			if cur.rChild == None:
				if cur.value > parent.value:
					parent.rChild = cur.lChild
				else:
					parent.lChild = cur.lChild
			else:
				if cur.value > parent.value:
					parent.rChild = cur.rChild
				else:
					parent.lChild = cur.rChild
		else:
			# cur has two children
			parent = cur
			succ = cur.rChild
			while succ.lChild != None:
				parent = succ
				succ = succ.lChild
			cur.value = succ.value
			if parent.lChild == succ:
				parent.lChild = succ.rChild
			else:
				parent.rChild = succ.rChild
	
	# Input: the root
	# Output the values of the node of the tree in increasing order
	# Recursively traverse the tree and print the valu of its nodes
	def inOrderTraversal(self, node):
		if node == None:
			return
		else:
			self.inOrderTraversal(node.lChild)
			print(node.value, end=" ")
			self.inOrderTraversal(node.rChild)
	
	# Input: the root
	# Output: the size of the tree
	def size(self, node):
		if node == None:
			return 0
		else:
			return 1 + self.size(node.lChild) + self.size(node.rChild)

	# Input: A node
	# Output: the height of "node"
	# Height of leaves is 0
	def height(self, node):
		if node == None:
			return -1
		else:
			return 1 + max(tree.height(node.lChild), tree.height(node.rChild))
	
	
	
			
			