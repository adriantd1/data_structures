class BinaryHeap:
	# Initialize the heap as the list if one is passed, else as an empty heap
	def __init__(self, lst=None):
		# The tree is 1-indexed so the 0th value is negative infinity
		self.ar = [float("-inf")]
		self.ar.extend(lst)
	
	# Return the parent of index i
	def parent(self, i):
		return i//2
	
	# Return the left child of i
	def leftChild(self, i):
		if i*2 <= len(self.ar)-1:
			return i*2
		else:
			return None
	
	# Return the right child of i
	def rightChild(self, i):
		if i*2 + 1 <= len(self.ar)-1:
			return i*2 + 1
		else:
			return None
	
	# Swap the values at ar[i] amd ar[j]
	def swap(self, i, j):
		temp = self.ar[i]
		self.ar[i] = self.ar[j]
		self.ar[j] = temp
	
	# Move the value of ar[i] up
	def upHeap(self, i):
		if i > 1:
			if self.ar[i] > self.ar[self.parent(i)]:
				self.swap(i, self.parent(i))
				self.upHeap(self.parent(i))
	
	# Move the value of ar[i] down
	def downHeap(self, i):
		if self.leftChild(i) != None:
			# if i is not a leaf
			if self.rightChild(i) != None:
				# if i has 2 children, find the min of the two
				m = min(self.ar[self.leftChild(i)], self.ar[self.rightChild(i)])
				if self.ar[m] == self.ar[self.leftChild(i)]:
					m = self.leftChild(i)
				else:
					m = self.rightChild(i)
			else:
				m = leftChild(self, i)
			if self.ar[m] > self.ar[i]:
				self.swap(m, i)
				self.downHeap(m)
	
	def buildHeap(self):
		for i in range(len(self.ar) // 2, len(self.ar)):
			self.upHeap(i)
			
	def insert(self, value):
		self.ar.append(value)
		self.upHeap(self.ar(len)-1)
		
	def pop(self):
		val = self.ar[1]
		self.ar[1] = self.ar[len(self.ar) - 1]
		self.ar.pop()
		self.downHeap(self.ar[1])
		return val
		
	def size(self):
		return len(self.ar) - 1
		
	def print(self):
		for i in range(1, len(self.ar)):
			print(self.ar[i], end=", ")
		print()
		
heap = BinaryHeap([1,2,3,4,5,6,7,8,9])
heap.buildHeap()
heap.print()
heap.pop()
heap.print()
		