import sys
sys.setrecursionlimit(2**20)

# PQueue class models a queue and it's constructor accepts: the list and the comes_before function
# PQueue consist of:
# A pair list
# comes_before function
class PQueue:
    def __init__(self, plist, comes_before):
        self.plist = plist
        self.comes_before = comes_before
    def __eq__(self, other):
        return ((type(other) == PQueue)
          and self.plist == other.plist
          and self.comes_before == other.comes_before
        )
    def __repr__(self):
        return ("PQueue({!r}, {!r})".format(self.plist, self.comes_before))

# linked list are:
# None, or
# Pair(first, rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Pair)
          and self.first == other.first
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))

# -a, b -> boolean
# -Checks to see if a is less than b, returns True if so and False otherwise.
# -def comes_before(a,b):
# - pass
def comes_before(a,b):
  if a < b:
    return True
  else:
    return False

# list -> int
# returns the length of the list
# def length(lst):
#   pass
def length(lst):
    if lst == None:
        return 0
    else:
        return 1 + length(lst.rest)

# None -> list
# returns an empty list
# def empty_list():
#   pass
def empty_list():
    return None

# list, index, value -> list
# Takes in list, puts value into desired index, returns new list with changes
# def add(lst, index, value):
#   pass
def add(lst, index, value, position=0):
    if (index < 0 or lst == None) and index != 0:
        raise IndexError()
    else:
        if index == position:
            return Pair(value, lst)
        else:
            return Pair(lst.first, add(lst.rest, index, value, 1+position))

# list, index -> value
# returns the value at a certain index
# def get(lst, index):
#   pass
def get(lst, index, position=0):
    if index < 0 or lst == None:
        raise IndexError()
    else:
        if position == index:
            return lst.first
        else:
            return get(lst.rest,index,1+position)

# list, index, value -> list
# returns a list with the value at the index if appropriate
# def set(lst, index, value):
#   pass
def set(lst, index, value, position=0):
    if index < 0 or lst == None:
        raise IndexError()
    else:
        if index == position:
            return Pair(value, lst.rest)
        else:
            return Pair(lst.first, set(lst.rest, index, value, 1+position))

# list, index -> list
# returns list with removed value
# def remove_lst(lst, index):
#   pass
def remove_lst(lst, index, position=0):
    if index < 0 or lst == None:
        raise IndexError()
    else:
        if index == position:
            return lst.rest
        else:
            return Pair(lst.first, remove_lst(lst.rest, index, 1+position))

# list, index -> (number, list)
# treturns list with value at index that was removed
# def remove(lst, index):
#   pass
def remove(lst,index):
    if index < 0 or lst == None:
        raise IndexError()
    else:
        return (get(lst, index), remove_lst(lst, index))

# list -> list
# returns the list in reverse order.
# def reverse(lst):
#   pass
def reverse(list_to_reverse):
    temparray=[]
    templist=None
    if(list_to_reverse==None):
        return None
    else:
        for index in range(length(list_to_reverse)):
            temparray.append(list_to_reverse.first)
            list_to_reverse=list_to_reverse.rest
        for index in range(0,len(temparray)):
            templist=Pair(temparray[index],templist)
        return templist

#############################################################

#comes_before function -> PQueue
#returns an empty queue implementation
#def empty_pqueue(comes_before):
#   pass
def empty_pqueue(func):
    return PQueue(empty_list(),func)

#PQueue,value->PQueue
#returns the Priority Queue after adding the value in the proper place
#def enqueue(PQueue,value):
#   pass
def enqueue(q,value):
    return PQueue(pinsert(q.plist,value,q.comes_before),q.comes_before)

#List,value,comes_before->list
#Helper function for enqueue that inserts value into proper place in plist
#def pinsert(List,value,comes_before):
#   pass
def pinsert(plist,value,comes_before):
    if(plist==None):
        return Pair(value,None)
    else:
        if not comes_before(plist.first, value):
            return Pair(value, plist)
        else:
            return Pair(plist.first, pinsert(plist.rest, value, comes_before))

#Pqueue -> value, Pqueue
#removes upcoming value in Pqeueue and returns the value that had been removed.
#def dequeue(q):
#   pass
def dequeue(q):
    if(q.plist ==None):
        raise IndexError()
    else:
        tmp= q.plist.first
        return tmp, PQueue(q.plist.rest, q.comes_before)

#Pqueue -> value
#returns upcoming value in pqueue
#def peek(q):
#   pass
def peek(q):
    if(q.plist==None):
        raise IndexError()
    else:
        return q.plist.first

#Pqueue -> int
#returns size or number of elements in Pqeueue list.
#def size(q):
#   pass
def size(q):
    return length(q.plist)

#Pqeueue -> boolean
#if plist is empty returns true if not returns false.
#def is_empty(q):
#   pass
def is_empty(q):
    return q.plist is None

