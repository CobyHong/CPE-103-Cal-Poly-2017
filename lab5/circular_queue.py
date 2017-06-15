
# -Queue consist of:
# -front which consist of
# -lst
# -size1
# -start
# -end
class Queue:
    def __init__(self, lst, size1=0, start=0, end=0):
        self.lst = lst
        self.size1 = size1
        self.start = start
        self.end = end
    def __eq__(self, other):
        return ((type(other) == Queue)
          and self.lst == other.lst
          and self.size1 == other.size1
          and self.start == other.start
          and self.end == other.end
        )
    def __repr__(self):
        return ("Queue({!r}, {!r}, {!r}, {!r})".format(self.lst, self.size1, self.start, self.end))

# -Nothing -> Queue
# -returns an empty Queue
# -def empty_queue():
# - pass
def empty_queue():
  return Queue([None]*5000)

# -Queue, value -> Queue
# -return Queue with value being first element in Queue front attribute.
# -def enqueue(Queue, value):
# - pass
def enqueue(q,value):
  if q.size1 < 5000:
  	q.lst[q.end]=value
  	q.size1 += 1
  	q.end = (q.end+1)%5000
  else:
  	raise IndexError()
  return q

# -Queue -> value, Queue
# -remove first element in Queue front attribute and shows what element was removed.
# -def dequeue(Queue):
# - pass
def dequeue(q):
  if q.size1 == 0:
    raise IndexError()
  else:
    tmp = q.lst[q.start]
    q.start = (q.start+1)%5000
    q.size1 -= 1
  return tmp, q

# -Queue -> int
# -returns size1 of Queue.
# -def size1(Queue):
# - pass
def size(q):
  return q.size1

# -Queue -> boolean
# -returns true if Queue front attribute is empty and false if not.
# -def is_empty(Queue):
# - pass
def is_empty(q):
  return q.size1 == 0

# -Queue -> value
# -returns first item in Queue.
# -def peek(Queue):
# - pass
def peek(q):
  if q.size1 == 0:
    raise IndexError
  else:
  	return q.lst[q.start]
