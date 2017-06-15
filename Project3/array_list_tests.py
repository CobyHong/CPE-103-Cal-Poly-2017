import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    #1
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    #2
    def test_length(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = length(list1)
        self.assertEqual(test, 5)
    #3
    def test_empty_lst(self):
        self.assertEqual(empty_list(), List([None,None], 0, 2))
    #4
    def test_enlarge(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = enlarge(list1)
        self.assertEqual(test, List([1,2,3,4,5, None, None], 5, 7))
    #5
    def test_add(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = add(list1, 1, 1.5)
        self.assertEqual(test, List([1,1.5,2,3,4,5, None], 6, 7))
    #6
    def test_add_2(self):
        self.assertRaises(IndexError, add, empty_list(), 1, 1.5 )
    #7
    def test_add_3(self):
        list1 = List([1,2,3,4,5,None], 5, 6)
        test = add(list1, 1, 1.5)
        self.assertEqual(test, List([1,1.5,2,3,4,5], 6, 6))
    #8
    def test_get(self):
        list1 = List([1,2,3,4,5,None], 5, 6)
        test = get(list1,1)
        self.assertEqual(test,2)
    #9
    def test_get_2(self):
        self.assertRaises(IndexError, get, empty_list(), 7)
    #10
    def test_set(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = set(list1, 1, "poop")
        self.assertEqual(test, List([1,"poop",3,4,5], 5, 5))
    #11
    def test_set_2(self):
        self.assertRaises(IndexError, set, empty_list(), 6, "poop")
    #12
    def test_remove(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = remove(list1,1)
        self.assertEqual(test, (2, List([1,3,4,5,None], 4, 5)))
    #13
    def test_remove_2(self):
        self.assertRaises(IndexError, remove, empty_list(), 7)
    def test_remove_3(self):
        self.assertRaises(IndexError, remove, empty_list(), 0)
    #14
    print(List([1,2,3,4,5], 5, 5))
    #15
    def test_foreach(self):
        list1 = List([1,2,3,4,5], 5, 5)
        def cube(a):
            return a*a*a
        test = foreach(list1, cube)
        print(list1)
    #16
    def test_foreach_2(self):
        list1 = List([1,2,3,4,3], 5, 5)
        def cube(a):
            return a*a*a
        self.assertEqual(cube(3), 27)
        test = foreach(list1, cube)
        self.assertEqual(test, None)
    #17
    def test_foreach_3(self):
        list1 = List([1,2,3,4,3], 5, 5)
        def cube(a):
            return a*a*a
        self.assertEqual(cube(3), 27)
        test = foreach(list1, cube)
        self.assertEqual(list1, List([1,2,3,4,3], 5, 5))
    #18
    def test_sort(self):
        list1 = List([1,2,3,4,0], 5, 5)
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = sort(list1, compare)
        self.assertEqual(test, List([0,1,2,3,4], 5, 5))
    #19
    def test_sort_2(self):
        list1 = empty_list()
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = sort(list1, compare)
        self.assertEqual(test, empty_list())

if __name__ == '__main__':
    unittest.main()
