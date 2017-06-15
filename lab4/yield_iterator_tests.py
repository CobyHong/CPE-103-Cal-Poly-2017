from linked_list import Pair, yield_iterator
import unittest

class TestCases(unittest.TestCase):
	#1
	def test_yield_iter(self):
		list1 = Pair(7, Pair(6, Pair(5, Pair(4, Pair(3, Pair(2, Pair(1, None)))))))
		test = yield_iterator(list1)
		self.assertEqual(next(test), 7)
		self.assertEqual(next(test), 6)
		self.assertEqual(next(test), 5)
		self.assertEqual(next(test), 4)
		self.assertEqual(next(test), 3)
		self.assertEqual(next(test), 2)
		self.assertEqual(next(test), 1)

if __name__ == '__main__':
	unittest.main()