from array_stack import *
from linked_stack import *

# -str -> stack
# -calculates string with postfix method and returns result in stack.
# -def postfix_calc(string):
# -	pass
def postfix_calc(string):
	stack = empty_stack()
	marks = string.split()
	for i in range(len(marks)):
		if marks[i] != "+" and marks[i] != "-" and marks[i] != "*" and marks[i] != "/":
			stack = push(stack, float(marks[i]))
		else:
			if marks[i] == "+":
				tmp = pop(stack)
				stack = tmp[1]
				tmp2 = pop(stack)
				stack = tmp2[1]
				stack = push(stack, float(tmp2[0]) + float(tmp[0]))
			if marks[i] == "-":
				tmp = pop(stack)
				stack = tmp[1]
				tmp2 = pop(stack)
				stack = tmp2[1]
				stack = push(stack, float(tmp2[0]) - float(tmp[0]))
			if marks[i] == "*":
				tmp = pop(stack)
				stack = tmp[1]
				tmp2 = pop(stack)
				stack = tmp2[1]
				stack = push(stack, float(tmp2[0]) * float(tmp[0]))
			if marks[i] == "/":
				tmp = pop(stack)
				stack = tmp[1]
				tmp2 = pop(stack)
				stack = tmp2[1]
				stack = push(stack, float(tmp2[0]) / float(tmp[0]))
	return peek(stack)