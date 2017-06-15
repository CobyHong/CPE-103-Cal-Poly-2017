import sys
sys.setrecursionlimit(5100)
from linked_list import *

# -Queue consist of:
# -front which consist of
# -Pair Class
# -None
# -same for lst2
class Queue:
    def __init__(self, front, back):
        self.front = front
        self.back = back
    def __eq__(self, other):
        return ((type(other) == Queue)
          and self.front == other.front
          and self.back == other.back
        )
    def __repr__(self):
        return "Front: %r, Back: %r" % (self.front, self.back)

# -Nothing -> Queue
# -returns an empty Queue
# -def empty_queue():
# - pass
def empty_queue():
    return Queue(empty_list(), empty_list())

# -Queue, value -> Queue
# -return Queue with value being first element in Queue front attribute.
# -def enqueue(Queue, value):
# - pass
def enqueue(q,value):
    return Queue(q.front, add(q.back, 0, value))

# -Queue -> value, Queue
# -remove first element in Queue front attribute and shows what element was removed.
# -def dequeue(Queue):
# - pass
def dequeue(q):
    if q.front is None:
        if q.back is None:
            raise IndexError
        else:
            early = reverse(q.back)
            return early.first, Queue(early.rest,None)
    else:
        return (q.front.first, Queue(q.front.rest, q.back))

# -Queue -> int
# -returns size of Queue.
# -def size(Queue):
# - pass
def size(q):
    return length(q.front) + length(q.back)

# -Queue -> boolean
# -returns true if Queue front attribute is empty and false if not.
# -def is_empty(Queue):
# - pass
def is_empty(q):
    return q.front is None and q.back is None

# -Queue -> value
# -returns first item in Queue.
# -def peek(Queue):
# - pass
def peek(q):
    if(q.front is None):
        if(q.back is None):
            raise IndexError
        else:
            early = reverse(q.back)
            return early.first
    else:
        return q.front.first
