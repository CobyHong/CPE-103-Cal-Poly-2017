
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
    if index < 0:
        raise IndexError()
    else:
        if index == position:
            return Pair(value, lst)
        elif lst == None:
        	raise IndexError()
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

# list, function -> list
# returns list with function applied to each element in list
# def foreach(lst, function):
#   pass
def foreach(lst, function):
    if lst == None:
        return None
    else:
    	function(lst.first)
    	foreach(lst.rest, function)

# lst function value -> lst
# Uses compare function to determine if value should be added to beginning of Pair
# def insert(lst, function, value):
#   pass
def insert(lst, function, value):
    if lst == None:
        return add(empty_list(), 0, value)
    elif function(value, lst.first):
        return add(lst, 0, value)
    else:
        return Pair(lst.first, insert(lst.rest, function, value))

# lst, function -> lst
# creates new lst in which compared items are returned into that list
# def sort(lst, function):
# pass
def sort(lst, function, new_lst=empty_list()):
    if lst == None:
        return new_lst
    else:
        new_lst = insert(new_lst, function, lst.first)
        return sort(lst.rest, function, new_lst)