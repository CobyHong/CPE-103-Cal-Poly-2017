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
    def test_interface_2(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        print(length(temp_list))
        print(get(temp_list, 0))
        set(temp_list,0,'Bye!')
        print(temp_list)
        temp_list = set(temp_list, 0, "Bye!")
        print(range(0,0))
        print(remove(temp_list, 0))
        print(empty_list())
        self.assertEqual(length(empty_list()),0)
        self.assertRaises(IndexError,get,empty_list(),1)
        self.assertRaises(IndexError,set,empty_list(),1,3)
        self.assertRaises(IndexError,remove,empty_list(),1)
        self.assertRaises(IndexError,add,empty_list(),2,3)
        print(add(add(add(empty_list(),0,3),1,2),2,1))
        self.assertEqual(empty_list()==empty_list(),True)

if __name__ == '__main__':
    unittest.main()
