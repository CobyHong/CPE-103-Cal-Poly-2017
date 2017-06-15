from linked_list import *

# -Stack consist of:
# -lst which consist of
# -Pair Class
# -None
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
# -	pass
def empty_stack():
    return Stack(None)

# -stack, value -> stack
# -return stack with value being first element in stack lst attribute.
# -def push(stack, value):
# -	pass
def push(stack,value):
    return Stack(Pair(value,stack.lst))

# -stack -> value, Stack
# -remove first element in stack lst attribute and shows what element was removed.
# -def pop(stack):
# -	pass
def pop(stack):
    if(stack.lst is None):
        raise IndexError
    else:
        temp=stack.lst.first
        stack=Stack(stack.lst.rest)
        return temp,stack

# -stack -> int
# -returns size of stack.
# -def size(stack):
# -	pass
def size(stack):
    if(stack.lst is None):
        return 0
    else:
        return 1+size(Stack(stack.lst.rest))

# -stack -> boolean
# -returns true if stack lst attribute is empty and false if not.
# -def is_empty(stack):
# -	pass
def is_empty(stack):
    return stack.lst is None

# -stack -> value
# -returns first item in stack.
# -def peek(stack):
# -	pass
def peek(stack):
    if(stack.lst is None):
        raise IndexError
    else:
        return stack.lst.first