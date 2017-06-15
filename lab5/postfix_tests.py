from postfix import *
import unittest

class TestList(unittest.TestCase):
	def test00_interface(self):
		postfix_calc("1 1 +")
	#1
	def test_profix(self):
		test = postfix_calc("5 3 - 12 * 3 / 10 +")
		self.assertEqual(test, 18)
	#2
	def test_profix_2(self):
		test = postfix_calc("1 2 + 4 *")
		self.assertEqual(test, 12)
	#3
	def test_profix_3(self):
		test = postfix_calc("5 3 + 12 * 3 /")
		self.assertEqual(test, 32)
	#4
	def test_profix_4(self):
		test = postfix_calc("4.34")
		self.assertEqual(test, 4.34)

if __name__ == '__main__':
    unittest.main()