from list_queue import *
import unittest

class TestCases(unittest.TestCase):
	def test00_interface(self):
		test_queue = empty_queue()
		test_queue = enqueue(test_queue, "foo")
		peek(test_queue)
		_, test_queue = dequeue(test_queue)
		size(test_queue)
		is_empty(test_queue)
	#1
	def test_empty(self):
		self.assertEqual(empty_queue(), Queue(None, None))
	#2
	def test_enq(self):
		front = Pair(5, Pair(4, None))
		back = Pair(1, None)
		test = Queue(front, back)
		self.assertEqual(enqueue(test, 5), Queue(Pair(5, Pair(4, None)), Pair(5, Pair(1, None))))
	#3
	def test_reverse(self):
		list1 = Pair(1, Pair(2, Pair(3, None)))
		test = reverse(list1)
		self.assertEqual(test, Pair(3, Pair(2, Pair(1, None))))
	#4
	def test_dequeue(self):
		q = empty_queue()
		q1 = enqueue(q, 2)
		q2 = enqueue(q1, 3)
		test = dequeue(q2)
		self.assertEqual(test, (2, Queue(Pair(3, None), None)))
	#5
	def test_dequeue_2(self):
		self.assertRaises(IndexError, dequeue, Queue(None,None))
	#6
	def test_dequeue_3(self):
		front = Pair(5, Pair(4, None))
		back = Pair(1, None)
		test = Queue(front, back)
		self.assertEqual(dequeue(test), (5, Queue(Pair(4, None),Pair(1, None))))
	#7
	def test_size(self):
		front = Pair(5, Pair(4, None))
		back = Pair(1, None)
		test = size(Queue(front, back))
		self.assertEqual(test, 3)
	#8
	def test_is_empty(self):
		front = Pair(5, Pair(4, None))
		back = Pair(1, None)
		test = is_empty(Queue(front, back))
		self.assertFalse(test)
	#9
	def test_is_empty_2(self):
		front = empty_list()
		back = empty_list()
		test = is_empty(Queue(front, back))
		self.assertTrue(test)
	#10
	def test_peek(self):
		front = Pair(5, Pair(4, None))
		back = Pair(1, None)
		test = peek(Queue(front, back))
		self.assertEqual(test, 5)
	#11
	def test_peek_2(self):
		front = empty_list()
		back = Pair(1, None)
		test = peek(Queue(front, back))
		self.assertEqual(test, 1)
	#12
	def test_peek_3(self):
		self.assertRaises(IndexError, peek, Queue(None,None))
	#13
	def test_print(self):
		print(Queue(None,None))

if __name__ == '__main__':

	unittest.main()

