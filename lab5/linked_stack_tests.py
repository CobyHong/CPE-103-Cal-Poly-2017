from linked_stack import *
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
		self.assertEqual(empty_stack(), Stack(None))
	#2
	def test_push(self):
		list1 = Stack(Pair(1,Pair(2,Pair(3, None))))
		test = push(list1, 7)
		self.assertEqual(test, Stack(Pair(7,Pair(1,Pair(2,Pair(3, None))))))
	#3
	def test_pop(self):
		list1 = Stack(Pair(1,Pair(2,Pair(3, None))))
		test = pop(list1)
		self.assertEqual(test, (1,Stack(Pair(2,Pair(3, None)))))
	#4
	def test_pop_2(self):
		self.assertRaises(IndexError, pop, Stack(None))
	#5
	def test_size(self):
		list1 = Stack(Pair(1,Pair(2,Pair(3, None))))
		test = size(list1)
		self.assertEqual(test, 3)
	#6
	def test_is_empty(self):
		list1 = Stack(None)
		test = is_empty(list1)
		self.assertTrue(test)
	#7
	def test_is_empty_2(self):
		list1 = Stack(Pair(1,Pair(2,Pair(3, None))))
		test = is_empty(list1)
		self.assertFalse(test)
	#8
	def test_peek(self):
		list1 = Stack(Pair(1,Pair(2,Pair(3, None))))
		test = peek(list1)
		self.assertEqual(test, 1)
	#9
	def test_peek_2(self):
		self.assertRaises(IndexError, peek, Stack(None))
	#10
	def test_print(self):
		print(Stack(Pair(1,Pair(2,Pair(3, None)))))
		
if __name__ == '__main__':
    unittest.main()
