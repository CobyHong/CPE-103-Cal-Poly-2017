from array_list import *

# -Stack consist of:
# -lst which consist of
# -List Class
# -empty_list()
class Stack:
    def __init__(self, lst):
        self.lst = lst
    def __eq__(self, other):
        return ((type(other) == Stack)
          and self.lst == other.lst
        )
    def __repr__(self):
        return ("Stack({!r})".format(self.lst))

# -Nothing -> Stack
# -returns an empty stack
# -def empty_stack():
# - pass
def empty_stack():
    return Stack(empty_list())

# -stack, value -> stack
# -return stack with value being first element in stack lst attribute.
# -def push(stack, value):
# - pass
def push(stack,value):
    return Stack(add(stack.lst,0,value))

# -stack -> value, Stack
# -remove first element in stack lst attribute and shows what element was removed.
# -def pop(stack):
# - pass
def pop(stack):
    if(stack.lst.size<1):
        raise IndexError
    else:
        tmp=stack.lst.lst[0]
        remove(stack.lst,0)
        return tmp,stack

# -stack -> int
# -returns size of stack.
# -def size(stack):
# - pass
def size(stack):
    return stack.lst.size

# -stack -> boolean
# -returns true if stack lst attribute is empty and false if not.
# -def is_empty(stack):
# - pass
def is_empty(stack):
    return stack.lst.size == 0

# -stack -> value
# -returns first item in stack.
# -def peek(stack):
# - pass
def peek(stack):
    if(stack.lst.size<1):
        raise IndexError
    else:
        return stack.lst.lst[0]
