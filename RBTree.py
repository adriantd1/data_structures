import BinaryTree as bt

class RBNode:
	def __init__(self, value):
		self.value = value
		self.lChild = None
		self.rChild = None
		self.parent = None
		self.color = "r"
	
class RBTree(bt.BinaryTree):
	# Instantiate the root of the RBTree as the input node and sets its color to black
	def __init__(self,value):
		self.root = RBNode(value)
		self.root.parent = self.root
		self.root.color = "b"
	
	# Rotate left on the given node
	def rotateLeft(self,node):
		if node == self.root:
			succ = self.root.rChild
			self.root.rChild = succ.lChild
			if succ.lChild != None:
				succ.lChild.parent = self.root
			succ.lChild = self.root
			self.root.parent = succ
			self.root = succ
			succ.parent = None
			return
		p = node.parent
		succ = node.rChild
		if succ == None:
			return
		if p.lChild == node:
			p.lChild = succ
		else:
			p.rChild = succ
		succ.parent = p
		node.parent = succ
		node.rChild = succ.lChild
		if node.rChild != None:
			node.rChild.parent = node
		succ.lChild = node
		if self.root == node:
			self.node = succ
	
	# Rotate right on the given node
	def rotateRight(self, node):
		if node == self.root:
			succ = self.root.lChild
			self.root.lChild = succ.rChild
			if succ.rChild != None:
				succ.rChild.parent = self.root
			succ.rChild = self.root
			self.root.parent = succ
			self.root = succ
			succ.parent = None
			return
		p = node.parent
		succ = node.lChild
		if succ == None:
			return
		if p.lChild == node:
			p.lChild = succ
		else:
			p.rChild = succ
		succ.parent = p
		node.parent = succ
		node.lChild = succ.rChild
		if node.lChild != None:
			node.lChild.parent = node
		succ.rChild = node
		if self.root == node:
			self.node = succ
	
	# Verify for any violation following the insertion of a node in the RBTree
	# and retruns a number corresponding to the violation or 0 is there is none
	def insertCheck(self, node):
		if node == None:
			return 0
		if node.color == "r":
			if node == self.root:
				return 1
			elif node.parent.color == "r":
				if node.parent.parent.lChild == node.parent:
					uncle = node.parent.parent.rChild
				else:
					uncle = node.parent.parent.lChild
				if uncle != None and uncle.color == "r":
					return 2
				else:
					if node.parent.lChild == node and node.parent.parent.rChild == node.parent:
						# if node is on the inside of the subtree rooted at node.parent.parent
						return 3
					elif node.parent.rChild == node and node.parent.parent.lChild == node.parent:
						# if node is on the inside of the subtree rooted at node.parent.parent
						return 3
					else:
						# if node is on the outside of the subtree rooted at node.parent.parent
						return 4
			else:
				return 0
				
	def insert(self, value):
		node = RBNode(value)
		cur = self.root
		while True:
			if node.value == cur.value:
				# If node.value = cur.value, assign cur.lChild = node
				node.lChild = cur.lChild
				node.lChild.parent = node
				cur.lChild = node
				node.parent = cur
				break
			if node.value > cur.value:
				# insert on right subtree
				if cur.rChild == None:
					cur.rChild = node
					node.parent = cur
					break
				else:
					cur = cur.rChild
			else:
				# insert on left subtree
				if cur.lChild == None:
					cur.lChild = node
					node.parent = cur
					break
				else:
					cur = cur.lChild
		
		cur = node
		case = self.insertCheck(cur)
		while True:
			if case == 0:
				break
			elif case == 1:
				self.root.color = "b"
				break
			elif case == 2:
				if cur.parent.parent.lChild == cur.parent:
					uncle = cur.parent.parent.rChild
				else:
					uncle = cur.parent.parent.lChild
				cur.parent.color = "b"
				if uncle != None:
					uncle.color = "b"
				cur.parent.parent.color = "r"
				cur = cur.parent.parent
				case = self.insertCheck(cur)
			elif case == 3:
				if cur.parent.parent.lChild == cur.parent:
					self.rotateLeft(cur.parent)
					cur = cur.lChild
				else:
					self.rotateRight(cur.parent)
					cur = cur.rChild
				case = self.insertCheck(cur)
			else:
				if cur.parent.lChild == cur:
					self.rotateRight(cur.parent.parent)
					cur.parent.color = "b"
					cur.parent.rChild.color= "r"
				else:
					self.rotateLeft(cur.parent.parent)
					cur.parent.color = "b"
					cur.parent.lChild.color= "r"
				cur = cur.parent
				case = self.insertCheck(cur.parent)
				
	# Helper function checking for violations following deletion
	def deleteCheck(self, node):
		cur = node
		if node == self.root:
			return 0
		# check for which case it is
		elif cur.parent.lChild == cur:
			if cur.parent.rChild != None and cur.parent.rChild.color == "r":
				return 1
			elif cur.parent.rChild != None and ((cur.parent.rChild.lChild == None or cur.parent.rChild.lChild.color == "b") and (cur.parent.rChild.rChild == None or cur.parent.rChild.rChild.color == "b")):
				return 2
		elif cur.parent.lChild != None and cur.parent.lChild.color == "r":
			return 1
		elif cur.parent.lChild != None and ((cur.parent.lChild.lChild == None or cur.parent.lChild.lChild.color == "b") and (cur.parent.lChild.rChild == None or cur.parent.lChild.rChild.color == "b")):
			return 2
		else:
			if cur.parent.lChild == cur:
				sibling = cur.parent.rChild
				if sibling == None:
					return 5
				if (sibling.lChild != None and sibling.lChild.color == "r") and (sibling.rChild == None or sibling.rChild.color == "b"):
					return 3
				else:
					return 4
			else:
				sibling = cur.parent.lChild
				if sibling == None:
					return 5
				if (sibling.lChild != None and sibling.lChild.color == "r") and (sibling.rChild == None or sibling.rChild.color == "b"):
					return 3
				else:
					return 4	
				
		
	def delete(self,val):
		# local functions to help finding the leftmost and rightmost child of a node
		def leftMost(node):
			if node.lChild == None:
				return node
			else:
				return leftMost(node.lChild)
		def rightMost(node):
			if node.rChild == None:
				return node
			else:
				return rightMost(node.rChild)
				
		if not self.find(val):
			print("There is no node with this value in the tree")
			return
			
		cur = self.root
		
		# Loop to find the node to delete
		while True:
			if cur.value == val:
				break
			elif cur.value > val:
				parent = cur
				cur = cur.lChild
			else:
				parent = cur
				cur = cur.rChild
		
		# Finds which node is going to replace the deleted node 
		if cur.lChild == None and cur.rChild == None:
			succ = None
		elif cur.lChild == None or cur.rChild == None:
			# cur has one child
			if cur.lChild != None:
				succ = cur.lChild
			else:
				succ = cur.rChild
		else:
			# Replace the value of the node to be deleted by its in-order successor
			# cur = in order successor and succ is the node which will replace it
			succ = leftMost(cur.rChild)
			cur.value = succ.value
			cur = succ
			succ = succ.rChild
		
		done = False
		if cur.color == "r" or (succ != None and succ.color == "r"):
			done = True
		if cur == self.root:
			self.root = succ
			succ.parent = succ
		else:
			if cur.parent.lChild == cur:
				cur.parent.lChild = succ
			else:
				cur.parent.rChild = succ
			if succ != None:
				succ.parent = cur.parent
				succ.color = "b"
		if done:
			return
		else:
			case = self.deleteCheck(cur)
			while True:
				if case == 1:
					if cur.parent.lchild == cur:
						# if cur is a left child
						cur.parent.color = "r"
						cur.parent.rChild.color = "b"
						self.rotateLeft(cur.parent)
						case = self.deleteCheck(cur)
					else:
						# cur is a right child
						cur.parent.color = "r"
						cur.parent.lChild.color = "b"
						self.rotateRight(cur.parent)
						case = self.deleteCheck(cur)
				elif case == 2:
					# set sibling's color to red
					if cur.parent.lChild == cur:
						cur.parent.rChild.color = "r"
					else:
						cur.parent.lChild.color = "r"
					if cur.parent.color == "r":
						# set parent's color to black and were done
						cur.parent.color == "b"
						break
					else:
						cur = cur.parent
						case = self.deleteCheck(cur)
				elif case == 3:
					if cur.parent.lChild == cur:
						sibling = cur.parent.rChild
						sibling.color == "r"
						if sibling.lChild != None:
							sibling.lChild.color = "b"
						self.rotateRight(sibling)
						case = self.deleteCheck(cur)
					else:
						sibling = cur.parent.lChild
						sibling.color == "r"
						if sibling.rChild != None:
							sibling.rChild.color = "b"
						self.rotateLeft(sibling)
						case = self.deleteCheck(cur)
				elif case == 4:
					if cur.parent.lChild == cur:
						self.rotateLeft(cur.parent)
						cur.parent.parent.color = cur.parent.color
						cur.parent.color = "b"
						if cur.parent.parent.rChild != None:
							cur.parent.parent.rChild.color = "b"
					else:
						self.rotateRight(cur.parent)
						cur.parent.parent.color = cur.parent.color
						cur.parent.color = "b"
						if cur.parent.parent.lChild != None:
							cur.parent.parent.lChild.color = "b"
					break
				else:
					break
						

	def printColor(self):
		dic = dict()
		def traverse(node):
			if node == None:
				return
			else:
				traverse(node.lChild)
				dic[node] = [node.lChild, node.rChild]
				traverse(node.rChild)
		traverse(self.root)
		for i in dic.keys():
			print(i.value, end=":")
			print(i.color, end=" ")
		print()
				
tree = RBTree(6)
tree.insert(4)
tree.insert(7)
tree.insert(3)
tree.insert(5)
tree.printChildren()
tree.printColor()
tree.delete(6)
tree.printChildren()
tree.printColor()

	