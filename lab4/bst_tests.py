from bst import *
import unittest

class TestCases(unittest.TestCase):
	#1
	def test_comes_before(self):
		test = comes_before(1,2)
		self.assertTrue(test)
	#2
	def test_comes_before_2(self):
		test = comes_before(3,2)
		self.assertFalse(test)
	#3
	def test_is_empty(self):
		test = is_empty(BinarySearchTree(comes_before, None))
		self.assertTrue(test)
	#4
	def test_is_empty_2(self):
		test = is_empty(BinarySearchTree(comes_before, BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))))
		self.assertFalse(test)
	#5
	def test_insert(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = insert(p, 3)
		self.assertEqual(test,insert(p,3))
	#6
	def test_insert_2(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = insert(p, 20)
		self.assertEqual(test,insert(p,20))
	#7
	def test_insert_3(self):
		b = None
		p = BinarySearchTree(comes_before, b)
		test = insert(p, 20)
		self.assertEqual(test,insert(p,20))
	#8
	def test_lookup(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = lookup(p, 7)
		self.assertTrue(test)	
	#9
	def test_lookup_2(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = lookup(p, 100)
		print(test)
		self.assertFalse(test)
	#10
	def test_lookup_3(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = lookup(p, 1)
		print(test)
		self.assertFalse(test)	
	#11
	def test_delete(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 10)
		self.assertEqual(test, delete(p,10))
	#12
	def test_delete_2(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 7)
		self.assertEqual(test, delete(p,7))
	#13
	def test_delete_3(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 15)
		self.assertEqual(test, delete(p,15))
	#14
	def test_delete_4(self):
		b = None
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 15)
		self.assertEqual(test, delete(p,15))
	#15
	def test_delete_5(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), None), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 7)
		self.assertEqual(test, delete(p,7))
	#16
	def test_delete_6(self):
		b = BSTNode(10, BSTNode(7, None, BSTNode(4, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		test = delete(p, 7)
		self.assertEqual(test, delete(p,7))
	#17
	def test_lowest(self):
		b = BSTNode(10, BSTNode(7,None,None), BSTNode(None, None, None))
		test = lowest(b)
		self.assertEqual(test, 7)
	#18
	def test_remove_lowest(self):
		b = BSTNode(10, BSTNode(7,None,None), BSTNode(None, None, None))
		test = remove_lowest(b)
		self.assertEqual(test, remove_lowest(b))
	#29
	def test_print(self):
		b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))
		p = BinarySearchTree(comes_before, b)
		print(b)
		print(p)

if __name__ == '__main__':

	unittest.main()