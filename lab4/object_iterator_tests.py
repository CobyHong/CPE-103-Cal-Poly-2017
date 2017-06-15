from linked_list import Iterator, object_iterator, has_next, next, Pair
import unittest

class TestCases(unittest.TestCase):

	def test_reprr(self):

		lst1 = Pair(1, Pair(2, None))
		self.assertEqual(repr(lst1), 'Pair(1, Pair(2, None))')

	def test_repr(self):

		lst1 = Pair(1, Pair(2, None))

		it1 = Iterator(lst1)

		self.assertEqual(repr(it1), 'Iterator(Pair(1, Pair(2, None)))')

	def test_object_iter(self):

		self.assertEqual(object_iterator(Pair(6, Pair(5, None))), Iterator(Pair(6, Pair(5, None))))

	def test_has_next(self):

		self.assertEqual(has_next(Iterator(Pair(9, None))), True)

	def test_next(self):

		self.assertEqual(next(Iterator(Pair(10, Pair(5, None)))), 10)

	def test_next_raiseStop(self):

		self.assertRaises(StopIteration, next, Iterator(None))


if __name__ == '__main__':

	unittest.main()