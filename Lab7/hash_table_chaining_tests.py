import unittest
from hash_table_chaining import *

class TestList(unittest.TestCase):
	#1
	def test_empty(self):
		test = empty_hash_table()
		self.assertEqual(test, HashTable(8))
	#2
	def test_insert(self):
		a = insert( HashTable(5), 1, 1)
		b = insert(a, 2, 2)
		c = insert(b, 2, 3)
		d = insert(c, 4, 4)
		e = insert(d, 5, 5)
		f = insert(e, 6, 6)
		g = insert(f, 7, 7)
		h = insert(g, 8, 8)
		i = insert(h, 9, 9)
		self.assertEqual(get(i,1), 1)
		self.assertEqual(get(i,2), 3)
		self.assertEqual(get(i,4), 4)
		self.assertEqual(get(i,5), 5)
		self.assertEqual(get(i,6), 6)
		self.assertEqual(get(i,7), 7)
		self.assertEqual(get(i,8), 8)
		self.assertEqual(get(i,9), 9)
	#3
	def test_get(self):
		test = insert(HashTable(2), 1, "test")
		self.assertEqual(get(test, 1), "test")
	#4
	def test_get_2(self):
		self.assertRaises(LookupError, get, empty_hash_table(), 3)
	#5
	def test_remove(self):
		a = insert( HashTable(10), 1, 1)
		b = insert(a, 2, 2)
		c = insert(b, 2, 3)
		d = insert(c, 4, 4)
		test = remove(d, 4)
		self.assertEqual(test, b)
	#6
	def test_remove_2(self):
		self.assertRaises(LookupError, remove, empty_hash_table(), 3)
	#7
	def test_size(self):
		a = insert( HashTable(10), 1, 1)
		b = insert(a, 2, 2)
		c = insert(b, 3, 3)
		d = insert(c, 4, 4)
		self.assertEqual(size(d), 4)
	#8
	def test_load_factor(self):
		a = insert( HashTable(10), 1, 1)
		b = insert(a, 2, 2)
		c = insert(b, 3, 3)
		d = insert(c, 4, 4)
		self.assertEqual(load_factor(d), 4/10)
	#9
	def test_collisions(self):
		a = insert( HashTable(10), 1, 1)
		b = insert(a, 2, 2)
		c = insert(b, 2, 3)
		d = insert(c, 4, 4)
		self.assertEqual(collisions(d), 1)
	#10
	def test_rehash(self):
		a = insert( HashTable(10), 2, 1)
		b = insert(a, "I", 2)
		c = insert(b, "Like", 3)
		d = insert(c, "Poop", 4)
		test = rehash(d)
		self.assertEqual(get(test, 2), 1)
		self.assertEqual(get(test, "I"), 2)
		self.assertEqual(get(test, "Like"), 3)
		self.assertEqual(get(test, "Poop"), 4)
	#11
	def test_print(self):
		print(HashTable(4))

if __name__ == '__main__':
    unittest.main()
