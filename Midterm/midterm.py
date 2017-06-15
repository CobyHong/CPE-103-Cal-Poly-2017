from linked_list import *
from array_list import *
from bst import *

# -lst, value -> int
# -Finds element nearest to specified value.
# -find_nearest(lst,value):
# - pass
def find_nearest(lst,value):
  if lst.lst == None:
    raise IndexError()
  else:
    result = []
    for i in range(length(lst)):
      test = lst.lst[i] - value
      result.append(abs(test))
    return value - min(result)

def find_some_sum(tree):
  if tree == None:
    return None
  else:                                         
      lst1 = Pair(tree.value , find_some_sum(tree.left))
      lst1 = str(lst1)
      return lst1



##########################################

list1 = List([1,2,9,4,5], 5, 5)

g = find_nearest(list1,7)
print(g)

##########################################

b = BSTNode(10, BSTNode(7, BSTNode(4, None, None), BSTNode(8, None, None)), BSTNode(15, None, None))

c = find_some_sum(b)
print(c)

#BST