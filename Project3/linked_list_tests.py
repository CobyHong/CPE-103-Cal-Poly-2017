import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    #0
    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
        print(Pair(1,Pair(2,Pair(3, None))))
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
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = length(list1)
        self.assertEqual(test, 3)
    #3
    def test_length_2(self):
        list1 = None
        test = length(list1)
        self.assertEqual(test, 0)
    #4
    def test_add(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = add(list1, 2, "poop")
        self.assertEqual(test, Pair(1, Pair(2, Pair("poop", Pair(3, None)))))
    #5
    def test_add_2(self):
        list1 = None
        test = add(list1, 0, "poop")
        self.assertEqual(test, Pair("poop", None))
    #6
    def test_add_3(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = add(list1, 0, "poop")
        self.assertEqual(test, Pair("poop", Pair(1, Pair(2, Pair(3, None)))))
    #7
    def test_add_4(self):
        self.assertRaises(IndexError, add, None, 4, "poop")
    def test_add_5(self):
        self.assertRaises(IndexError, add, Pair(1,Pair(2,Pair(3, None))), -6, "poop")
    #8
    def test_get(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = get(list1, 2)
        self.assertEqual(test, 3)
    #9
    def test_get_2(self):
        self.assertRaises(IndexError, get, None, 2)   
    #10
    def test_get_3(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = get(list1, 0)
        self.assertEqual(test, 1)
    #11
    def test_set(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = set(list1, 0, "poop")
        self.assertEqual(test, Pair("poop", Pair(2, Pair(3, None))))
    #12
    def test_set_2(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = set(list1, 1, "poop")
        self.assertEqual(test, Pair(1 , Pair("poop", Pair(3, None))))
    #13
    def test_set_3(self):
        self.assertRaises(IndexError, set, None, 2, "poop")
    #14
    def test_remove_lst(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = remove_lst(list1, 0)
        self.assertEqual(test, Pair(2, Pair(3, None))) 
    #15
    def test_remove_lst_2(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = remove_lst(list1, 2)
        self.assertEqual(test, Pair(1, Pair(2, None)))
    #16
    def test_remove_lst_3(self):
        self.assertRaises(IndexError, remove_lst, None, 2)
    #17
    def test_remove(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = remove(list1, 0)
        self.assertEqual(test, (1, Pair(2,Pair(3, None))) )
    #18
    def test_remove_2(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = remove(list1, 2)
        self.assertEqual(test, (3, Pair(1, Pair(2, None))) )
    #19
    def test_remove_3(self):
        self.assertRaises(IndexError, remove, None, 2)
    #19
    def test_foreach(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        def cube(a):
            return a*a*a
        test = foreach(list1, cube)
        self.assertEqual(list1, Pair(1,Pair(2,Pair(3, None))))
    #20
    def test_foreach_2(self):
        list1 = empty_list()
        def cube(a):
            return a*a*a
        self.assertEqual(cube(3), 27)
        test = foreach(list1, cube)
        self.assertEqual(list1, None)
    #21
    def test_foreach_3(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        def cube(a):
            return a*a*a
        self.assertEqual(cube(3), 27)
        test = foreach(list1, cube)
        self.assertEqual(test, None)
    #22
    def test_sort(self):
        list1 = Pair(1,Pair(5,Pair(3, None)))
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = sort(list1, compare)
        self.assertEqual(test, Pair(1,Pair(3,Pair(5, None))))
    #23
    def test_sort_2(self):
        list1 = empty_list()
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = sort(list1, compare)
        self.assertEqual(test, None)
    #24
    def test_insert(self):
        lst = empty_list()
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert(lst, compare, 3)
        self.assertEqual(test, Pair(3,None))
    #25
    def test_insert_2(self):
        list1 = Pair(1,Pair(3,Pair(5, None)))
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert(list1, compare, 0)
        self.assertEqual(test, Pair(0,Pair(1,Pair(3, Pair(5, None)))))
    #26
    def test_insert_3(self):
        list1 = Pair(1,Pair(3,Pair(5, None)))
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert(list1, compare, 2)
        self.assertEqual(test, Pair(1,Pair(2,Pair(3, Pair(5, None)))))
    #27
    def test_insert_sorted(self):
        list1 = empty_list()
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert_sorted(list1, 2, compare)
        self.assertEqual(test, Pair(2, None))
    #28
    def test_insert_sorted_2(self):
        list1 = Pair(1,Pair(5,Pair(7, None)))
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert_sorted(list1, 0, compare)
        self.assertEqual(test, Pair(0,Pair(1,Pair(5, Pair(7, None)))))
    #29
    def test_insert_sorted_3(self):
        list1 = Pair(1,Pair(5,Pair(7, None)))
        def compare(a,b):
            if a < b:
                return True
        self.assertEqual(compare(1,2), True)
        self.assertEqual(compare(2,1), None)
        test = insert_sorted(list1, 3, compare)
        self.assertEqual(test, Pair(1,Pair(3,Pair(5, Pair(7, None)))))

if __name__ == '__main__':
    unittest.main()