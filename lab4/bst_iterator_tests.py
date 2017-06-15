from bst import prefix_iterator, infix_iterator, postfix_iterator, comes_before, BSTNode, BinarySearchTree
import unittest

class TestCases(unittest.TestCase):
	#1
	def test_prefix(self):
		b = BSTNode(10, BSTNode(7, None, BSTNode(4, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = prefix_iterator(p)
		self.assertEqual(next(test), 10)
		self.assertEqual(next(test), 7)
		self.assertEqual(next(test), 4)
		self.assertEqual(next(test), 15)
	#2
	def test_infix(self):
		b = BSTNode(10, BSTNode(7, None, BSTNode(4, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = infix_iterator(p)
		self.assertEqual(next(test), 7)
		self.assertEqual(next(test), 4)
		self.assertEqual(next(test), 10)
		self.assertEqual(next(test), 15)
	#3
	def test_postfix(self):
		b = BSTNode(10, BSTNode(7, None, BSTNode(4, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = postfix_iterator(p)
		self.assertEqual(next(test), 4)
		self.assertEqual(next(test), 7)
		self.assertEqual(next(test), 15)
		self.assertEqual(next(test), 10)

if __name__ == '__main__':

	unittest.main()