
#BSTNode is of:
# -value
# -left - another BSTNode
# -right - another BSTNode
class BSTNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def __eq__(self, other):
        return ((type(other) == BSTNode)
          and self.value == other.value
          and self.left == other.left
          and self.right == other.right
        )
    def __repr__(self):
        return ("BSTNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

##############################################################################################

#BinarySearchTree is of:
# -BSTNode
# -function comes_before
class BinarySearchTree:
    def __init__(self, comes_before, node=None):
        self.node = node
        self.comes_before = comes_before

    def __eq__(self, other):
        return ((type(other) == BinarySearchTree)
          and self.node == other.node
          and self.comes_before == other.comes_before
        )

    def __repr__(self):
        return ("BinarySearchTree({!r}, {!r})".format(self.node, self.comes_before))

##############################################################################################

# -a, b -> boolean
# -Checks to see if a is less than b, returns True if so and False otherwise.
# -def comes_before(a,b):
# -	pass
def comes_before(a,b):
  if a < b:
    return True
  else:
    return False

##############################################################################################

# -bst -> boolean
# -If the bst given is empty, will return True, else will be False.
# -def is_empty(bst):
# - pass
def is_empty(bst):
  if bst.node == None:
    return True
  else:
    return False

# -tree, value -> tree
# -inserts value into tree at correct node location using function.
# -def insert_work(tree,value, function):
# - pass
def insert_work(tree, value, function):
  if tree == None:
    return BSTNode(value, None, None)
  elif function(value, tree.value):
    if tree.left:
      insert_work(tree.left, value, function)
    else:
      tree.left = BSTNode(value, None, None)
  elif not function(value, tree.value):
    if tree.right:
      insert_work(tree.right, value, function)
    else:
      tree.right = BSTNode(value, None, None)
  return tree

# -bst, value -> bst
# -runs insert function on node part of bst.
# -def insert(bst,value):
# -	pass
def insert(bst,value):
	return BinarySearchTree(bst.comes_before, insert_work(bst.node,value, bst.comes_before))

##############################################################################################

# -tree, value -> boolean
# -Looks up value in tree, if found returns True, else False.
# -def lookup_work(tree,value, function):
# - pass
def lookup_work(tree,value, function):
    if not function(value, tree.value) and not function(tree.value, value):
        return True
    else:
    	if function(value, tree.value):
    		if tree.left:
    			return lookup_work(tree.left, value, function)
    		else:
    			return False
    	if not function(value, tree.value):
    		if tree.right:
    			return lookup_work(tree.right, value, function)
    		else:
    			return False

# -bst, value -> bst
# -runs lookup function on node part of bst.
# -def lookup(bst,value):
# -	pass
def lookup(bst,value):
	return lookup_work(bst.node, value, bst.comes_before)

##############################################################################################

# -tree, value -> tree
# -Removes value in tree and reorders to meet tree requirements.
# -def remove_work(tree,value,function):
# -	pass
def remove_work(tree, value, function):
    if tree == None:
        return None
    if not function(value, tree.value) and not function(tree.value, value):
        if tree.left == None and tree.right == None:
        	return None
        elif tree.left and tree.right == None:
            return tree.left
        elif tree.left == None and tree.right:
            return tree.right
        elif tree.left and tree.right:
        	return BSTNode(lowest(tree.right), tree.left, remove_lowest(tree.right)) #swaps lowest right to value,and removes lowest right.
    else:
        if function(value, tree.value):
            if tree.left:
            	return BSTNode(tree.value, remove_work(tree.left, value, function), tree.right)
        if not function(value, tree.value):
            if tree.right:
            	return BSTNode(tree.value, tree.left, remove_work(tree.right, value, function))

# -HELPER
# -Finds the lowest value by traversing left side (left always smaller than right).
# -def lowest(tree):
# -	pass
def lowest(tree):
	if tree.left == None and tree.right == None:
		return tree.value
	else:
		return lowest(tree.left)

# -HELPER
# -Removes lowest value by traversing left side (left always smaller than right).
# -def remove_lowest(tree):
# -	pass
def remove_lowest(tree):
	if tree.left == None and tree.right == None:
		return None
	else:
		return BSTNode(tree.value, remove_lowest(tree.left), tree.right)

# -bst, value -> bst
# -runs remove function on node part of bst.
# -def remove(bst,value):
# -	pass
def delete(bst,value):
    return BinarySearchTree(bst.comes_before, remove_work(bst.node, value, bst.comes_before))

##############################################################################################

# -tree -> Pair
# -Order node in Bst infix order.
# -infix_iterator_work(tree):
# - pass
def infix_iterator_work(tree):
  if tree is not None:
    yield from infix_iterator_work(tree.left)
    yield tree.value
    yield from infix_iterator_work(tree.right)

# -bst -> Iterator
# -performs function and puts into Iterator class
# -def infix_iterator(bst):
# - pass 
def infix_iterator(bst):
  return infix_iterator_work(bst.node)

##############################################################################################

# -tree -> Pair
# -Order node in Bst postfix order.
# -postfix_iterator_work(tree):
# - pass
def postfix_iterator_work(tree):
  if tree is not None:
    yield from postfix_iterator_work(tree.left)
    yield from postfix_iterator_work(tree.right)
    yield tree.value

# -bst -> Iterator
# -performs function and puts into Iterator class
# -def infix_iterator(bst):
# - pass 
def postfix_iterator(bst):
  return postfix_iterator_work(bst.node)
##############################################################################################

# -tree -> Pair
# -Order node in Bst prefix order.
# -prefix_iterator_work(tree):
# - pass
def prefix_iterator_work(tree):
  if tree is not None:
    yield tree.value
    yield from prefix_iterator_work(tree.left)
    yield from prefix_iterator_work(tree.right)

# -bst -> Iterator
# -performs function and puts into Iterator class
# -def infix_iterator(bst):
# - pass 
def prefix_iterator(bst):
  return prefix_iterator_work(bst.node)
##############################################################################################

#              10              #
#       7            15        #
#   4       N     N     N      #
# N    N                       #