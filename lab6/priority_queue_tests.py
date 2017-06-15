from priority_queue import *
import unittest

class TestCases(unittest.TestCase):
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

################################################

    def test_repr2(self):
        self.assertEqual(repr(Pair(5, None)), "Pair(5, None)")

    def test_length0(self):
        p = Pair(5, Pair(4, None))
        self.assertEqual(length(p), 2)

    def test_repr(self):
        print(empty_pqueue(comes_before))

    def test_empty(self):
        self.assertEqual(empty_pqueue(comes_before), PQueue(None, comes_before))

    def test_enqueue(self):
        p = empty_pqueue(comes_before)
        p2 = enqueue(p, 5)
        self.assertEqual(enqueue(p2, 4), PQueue(Pair(4, Pair(5, None)), comes_before))

    def test_dequeue(self):
        p = empty_pqueue(comes_before)
        p2 = enqueue(p, 5)
        p3 = enqueue(p2, 4)
        self.assertEqual(dequeue(p3), (4, PQueue(Pair(5, None), comes_before)))

    def test_dequeue_error(self):
        self.assertRaises(IndexError, dequeue, empty_pqueue(comes_before))

    def test_peek(self):
        p = empty_pqueue(comes_before)
        p2 = enqueue(p, 5)
        p3 = enqueue(p2, 2)
        p4 = enqueue(p3, 1)
        self.assertEqual(peek(p4), 1)

    def test_peek_error(self):
        self.assertRaises(IndexError, peek, empty_pqueue(comes_before))

    def test_size(self):
        p = empty_pqueue(comes_before)
        p2 = enqueue(p, 2)
        p3 = enqueue(p2, 4)
        p4 = enqueue(p3, 5)
        p5 = dequeue(p4)
        self.assertEqual(size(p5[1]), 2)

    def test_is_empty(self):
        self.assertTrue(is_empty(empty_pqueue(comes_before)))

    def test_reverse(self):
        list1 = Pair(1,Pair(2,Pair(3, None)))
        test = reverse(list1)
        self.assertEqual(test, Pair(3,Pair(2,Pair(1, None))) )

    def test_reverse2(self):
        list1 = None
        test = reverse(list1)
        self.assertEqual(test, None )

################################################
		
if __name__ == '__main__':

    unittest.main()