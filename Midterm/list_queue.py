from linked_list import *
import unittest

# A Queue is a Queue(AnyList, AnyList)
# where Anylist is one of:
# None, or
# Pair(value, AnyList)

class Queue:

	def __init__(self, early, late):

		self.early = early # An AnyList representing the front end of the queue (for dequeueing.)
		self.late = late # An AnyList representing the back end of the queue(for enqueueing)

	def __eq__(self, other):

		return (type(other) == Queue
				and self.early == other.early
				and self.late == other.late	
				)

	def __repr__(self):

		return "Front: %r, Back: %r" % (self.early, self.late)

# -> Queue
def empty_queue():

	return Queue(empty_list(), empty_list())

# Queue value -> Queue
# Enqueues a specified value.
def enqueue(q, val):

	return Queue(q.early, add(q.late, 0, val))

# AnyList -> AnyList
# Reverses a linked list.
def reverse(lst1):

	new_list = empty_list()
	add_index = 0
	for i in range(length(lst1), 0, -1):

		new_list = add(new_list, add_index, get(lst1, i - 1))
		add_index += 1

	return new_list



# Queue -> (val, Queue)
# Dequeues the first element in a queue.
def dequeue(q):

	if q.early == None:

		if q.late == None:

			raise IndexError()

		else:

			new_early = reverse(q.late)
			return (new_early.first, Queue(new_early.rest, None))

	else:

		return (q.early.first, Queue(q.early.rest, q.late))

# Queue -> val
# Returns the first item in a queue.
def peek(q):

	if q.early == None:

		if q.late == None:

			raise IndexError()

		else:

			new_early = reverse(q.late)
			return new_early.first

	else:

		return q.early.first

# Queue -> int
# Returns the size of a queue.
def size(q):

	return length(q.early) + length(q.late)

# Queue -> boolean
# Determines whether or not a queue is empty.
def is_empty(q):

	return q.early == None and q.late == None

q = empty_queue()
print(q)
q1 = enqueue(q, 2)
print(q1)
q2 = enqueue(q1, 5)
print(q2)
q3 = dequeue(q2)
print(q3)

class TestCases(unittest.TestCase):

	def test_empty(self):

		self.assertEqual(empty_queue(), Queue(None, None))

	def test_enq(self):

		early = Pair(5, Pair(4, None))
		late = Pair(1, None)
		self.assertEqual(enqueue(Queue(early, late), 5), Queue(Pair(5, Pair(4, None)), Pair(5, Pair(1, None))))

	def test_reverse(self):

		lst1 = Pair(1, Pair(2, Pair(5, None)))
		self.assertEqual(reverse(lst1), Pair(5, Pair(2, Pair(1, None))))

	def test_dequeue(self):

		q = empty_queue()
		q1 = enqueue(q, 2)
		q2 = enqueue(q1, 3)
		self.assertEqual(dequeue(q2), (2, Queue(Pair(3, None), None)))
if __name__ == '__main__':

	unittest.main()

