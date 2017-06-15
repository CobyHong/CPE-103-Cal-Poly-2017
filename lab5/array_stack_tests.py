from array_stack import *
import unittest

class TestList(unittest.TestCase):
	def test00_interface(self):
		test_stack = empty_stack()
		test_stack = push(test_stack, "foo")
		peek(test_stack)
		_, test_stack = pop(test_stack)
		size(test_stack)
		is_empty(test_stack)
	#1
	def test_empty_stack(self):
		self.assertEqual(empty_stack(), Stack(empty_list()))
	#2
	def test_push(self):
		list1 = Stack(List([1,2,3,4,5], 5, 5))
		test = push(list1, 7)
		self.assertEqual(test, Stack(List([7,1,2,3,4,5, None], 6, 7)))
	#3
	def test_pop(self):
		list1 = Stack(List([1,2,3,4,5], 5, 5))
		test = pop(list1)
		self.assertEqual(test, (1, Stack(List([2, 3, 4, 5, None], 4, 5))))
	#4
	def test_pop_2(self):
		self.assertRaises(IndexError, pop, Stack(empty_list()))
	#5
	def test_size(self):
		list1 = Stack(List([1,2,3,4,5], 5, 5))
		test = size(list1)
		self.assertEqual(test, 5)
	#6
	def test_is_empty(self):
		list1 = Stack(empty_list())
		test = is_empty(list1)
		self.assertTrue(test)
	#7
	def test_is_empty_2(self):
		list1 = Stack(List([1,2,3,4,5], 5, 5))
		test = is_empty(list1)
		self.assertFalse(test)
	#8
	def test_peek(self):
		list1 = Stack(List([1,2,3,4,5], 5, 5))
		test = peek(list1)
		self.assertEqual(test, 1)
	#9
	def test_peek_2(self):
		self.assertRaises(IndexError, peek, Stack(empty_list()))
	#10
	def test_print(self):
		print(Stack(List([1,2,3,4,5], 5, 5)))

if __name__ == '__main__':
    unittest.main()
