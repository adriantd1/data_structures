# implementation of a general purpose segmented tree. The tree stores
# a property (sum, multiplication, gcd, ...) given by the function f
# on an interval. The tree support updates and querying. 
 
ar = [1,3,5,7,9,11]
#list of size 2*len(ar)
tree = [0 for x in range(2*len(ar)+2)]

def f(a,b):
	return a+b
	
def build(f, n, start, end):
	if start == end:
		tree[n] = ar[start]
	else:
		mid = (start + end)//2
		build(f, 2*n, start, mid)
		build(f, 2*n+1, mid+1, end)
		tree[n] = f(tree[2*n], tree[2*n+1])

#change ar[index] to upd and update the tree accordingly		
def update(f, n, start, end, index, upd):
	if start == end:
		ar[index] = upd
		tree[n] = upd
	else:
		mid = (start + end)//2
		if start<=index and index<=mid:
			#index in left subtree
			update(f, 2*n, start, mid, index, upd)
		else:
			#index in right subtree
			update(f, 2*n+1, mid+1, end, index, upd)
		tree[n] = f(tree[2*n], tree[2*n+1])

#query on the range [left:right+1]
#id is the identity s.t. f(a,b) = a
def query(f, id, n, start, end, left, right):
	if(end<left or right<start):
		#range of query is out of the range of n
		return id
	if(left<=start and end<=right):
		#range of query completely include the range of n
		return tree[n]
	#range of query is partially represented by range of n
	mid = (start+end)//2
	l = query(f, id, 2*n, start, mid, left, right)
	r = query(f, id, 2*n+1, mid+1, end, left, right) 
	return f(l,r)