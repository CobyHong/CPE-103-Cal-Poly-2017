import unittest

# * Section 2 (Trees)

# * dd: NumTree Data Definition

# "mt" --> means empty!!! Just the way the teacher likes it!

# ListItem is either:
# - string or number

# a List is either:
# - a numlist or Strlist

#a Tree is one of
# - "mt", or
#TreeNode(value, left, right)
class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def __eq__(self, other):
    	if type(other) == TreeNode:
    		value_eq = (self.value == other.value)
    		left_eq = (self.left == other.left)
    		right_eq = (self.right == other.right)
    		return value_eq and left_eq and right_eq
    	else:
    		return False
    def __repr__(self):
        return ("TreeNode:({!r}, {!r}, {!r})".format(self.value, self.left, self.right))

# * 1:

# tree -> int
# Takes in a tree and returns number of elements in tree
def size(tree):
	if tree == "mt":
		return 0
	return 1 + size(tree.left) + size(tree.right)

# * 2:

# tree -> int
# Takes in a tree and returns number of leaves (nodes with no branches)
def num_leaves(tree):
	if tree == "mt":
		return 0
	else:
		if(tree.left and tree.right == "mt"):
			return 1
		else:
			return num_leaves(tree.left) + num_leaves(tree.right)

# * 3:

# tree -> float
# Takes in tree and finds sum of all values in the nodes
def sum(tree):
	if tree == "mt":
		return 0
	else:
		return tree.value + sum(tree.left) + sum(tree.right)

# * 4:

# Skip this function! Freebie! Go get a lemonade.

# * 5:

# tree -> boolean
# Takes in tree and sees if any sibling nodes are 3 times the value of parent node and returns True or False
def has_triple(tree):
	if tree == "mt":
		return False
	if tree.left =="mt" and tree.right == "mt":
		return False
	else:
		if tree.left != "mt":
			if tree.left.value == 3 * tree.value:
				return True
		if tree.right != "mt":
			if tree.right.value == 3 * tree.value:
				return True
		return has_triple(tree.left) or has_triple(tree.right)

# * 6:

# tree -> tree
# Takes in tree and returns new tree where all values are less by one
def sub_one_map(tree):
	if tree == "mt":
		return "mt"
	return TreeNode(tree.value -1, sub_one_map(tree.left), sub_one_map(tree.right))

# * Tests : the test case class for the tree functions
class TestCases(unittest.TestCase):
    def test_size(self):
        list1 = TreeNode(1,TreeNode(2, "mt", "mt"),TreeNode(3, "mt", "mt"))
        test = size(list1)
        self.assertEqual(test,3)

    def test_size_2(self):
        list1 = "mt"
        test = size(list1)
        self.assertEqual(test,0)

    def test_num_leaves(self):
        list1 = TreeNode(1,TreeNode(2, "mt", "mt"),TreeNode(3, "mt", "mt"))
        test = num_leaves(list1)
        self.assertEqual(test,2)

    def test_num_leaves_2(self):
        list1 = "mt"
        test = num_leaves(list1)
        self.assertEqual(test,0)

    def test_sum(self):
        list1 = TreeNode(1,TreeNode(2, "mt", "mt"),TreeNode(3, "mt", "mt"))
        test = sum(list1)
        self.assertEqual(test,6)

    def test_sum_2(self):
        list1 = "mt"
        test = sum(list1)
        self.assertEqual(test,0)

    def test_has_triple(self):
        list1 = TreeNode(2,TreeNode(2, "mt", "mt"),TreeNode(6, "mt", "mt"))
        test = has_triple(list1)
        self.assertEqual(test,True)

    def test_has_triple_2(self):
        list1 = TreeNode(2,TreeNode(2, "mt", "mt"),TreeNode(8, "mt", "mt"))
        test = has_triple(list1)
        self.assertEqual(test,False)

    def test_has_triple_3(self):
        list1 = "mt"
        test = has_triple(list1)
        self.assertEqual(test,False)

    def test_has_triple_4(self):
        list1 = TreeNode(2,TreeNode(6, "mt", "mt"),TreeNode(2, "mt", "mt"))
        test = has_triple(list1)
        self.assertEqual(test,True)

    def test_sub_one_map(self):
        list1 = TreeNode(1,TreeNode(2, "mt", "mt"),TreeNode(5, "mt", "mt"))
        test = sub_one_map(list1)
        result = TreeNode(0,TreeNode(1, "mt", "mt"),TreeNode(4, "mt", "mt"))
        self.assertEqual(test,result)

    def test_sub_one_map_2(self):
        list1 = "mt"
        test = sub_one_map(list1)
        result = "mt"
        self.assertEqual(test,result)

    print(TreeNode(23,"mt","mt"))

if __name__ == '__main__':
    unittest.main()


