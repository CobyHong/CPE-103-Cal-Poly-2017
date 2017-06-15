from array_list import *
#from linked_list import *
from huffman_bits_io import *
import sys
import unittest
import os

# hleaf consist of:
# the cint value of the letter
# its occurence in file proved
class Hleaf:
    def __init__(self, cint, freq):
        self.cint = cint
        self.freq = freq
    def __eq__(self, other):
        return ((type(other) == Hleaf)
          and self.cint == other.cint
          and self.freq == other.freq
        )
    def __repr__(self):
        return ("Hleaf({!r}, {!r})".format(self.cint, self.freq))

# hnode consist of:
# total of left and right occurences
# the greater ASCII character of the two (left and right)
# left and right which are comprised of hleafs or hnodes
class Hnode:
    def __init__(self, freq, cint, left, right):
        self.freq = freq
        self.cint = cint
        self.left = left
        self.right = right
    def __eq__(self, other):
        return ((type(other) == Hnode)
          and self.freq == other.freq
          and self.cint == other.cint
          and self.left == other.left
          and self.right == other.right
        )
    def __repr__(self):
        return ("Hnode({!r}, {!r}, {!r}, {!r})".format(self.freq, self.cint, self.left, self.right))

##################################################

# a, b -> boolean
# checks if a has lesser frequency and returns True.
# if frequency is equal, compares ASCII values instead and returns True.
# def comes_before(a,b):
#	pass
def comes_before(a,b):
	if a.freq < b.freq:
		return True
	elif a.freq == b.freq:
		if a.cint < b.cint:
			return True
		else:
			return False

# a, b -> boolean
# checks if a has lesser frequency and returns True.
# if frequency is equal, compares ASCII values instead and returns True.
# def comes_before(a,b):
#	pass
def comes_before2(a,b):
	if a.cint < b.cint:
		return True
	else:
		return False

# file -> list
# read file and return list of ASCII occurences.
# def accumulator(file_):
#	pass
def accumulator(file):
  f = open(file)
  lst = [0]*256
  for word in f:
  	for letter in word:
  		lst[ord(letter)] = lst[ord(letter)] + 1
  f.close()
  return List(lst, 256, 256)

# file -> list
# returns ASCII list with Hleaf of ASCII value, and number of occurences
# def hleaf_maker(file):
#	pass
def hleaf_maker(file):
	result = empty_list()
	h = accumulator(file)
	for i in range(h.size):
		if h.lst[i] != 0:
			result = add(result, length(result), (Hleaf(i , h.lst[i])))
	return result


# file -> list
# returns ASCII list with Hleaf of ASCII value, and number of occurences
# def hleaf_maker_decode(file):
#	pass
def hleaf_maker_decode(lst):
	result = empty_list()
	h = lst
	for i in range(h.size):
		if h.lst[i] != 0:
			result = add(result, length(result), (Hleaf(i , h.lst[i])))
	return result

# file -> Hnode
# out of sorted listed, creates parent node and keeps building into itself until only one index left or complete Hnode.
# def builder(file):
#	pass
def builder(lst, function):
	if lst == None:
		return None
	else:
		while length(lst) != 1:
			t = lst
			lst = remove(lst, 0)[1]
			lst = remove(lst, 0)[1]
			lst = insert_sorted(lst, Hnode(t.first.freq + t.rest.first.freq, t.first.cint, t.first, t.rest.first) , function)
		return lst.first

# tree -> list of tuples
# traverses built Huffman Tree and generates key for huffman encoding.
# EX: [(32, '00'), (98, '01'), (100, '100'), (99, '101'), (97, '11'), (ASCII Value, Key)]
# def encode_work(tree):
#	pass
def encode_work(tree, code=""):
	if type(tree) == Hnode:
		result = []
		for i in encode_work(tree.left, code + "0"):
			result.append(i)
		for i in encode_work(tree.right, code + "1"):
			result.append(i)
		return result
	if type(tree) == Hleaf:
		return [(tree.cint, code)]

# file, out -> string, header
# Goes through string of file and converts to huffman string.
# def encode(file, out):
#	pass
def huffman_encode(file, out, code=""):
	a = sort(hleaf_maker(file), comes_before2)
	t= builder( sort(hleaf_maker(file), comes_before), comes_before)
	f = encode_work(builder( sort(hleaf_maker(file), comes_before), comes_before))

	if t is not None:
		#writing to outfile
		infile = HuffmanBitsWriter(out)
		#writing numberof bytes / possible letters
		infile.write_byte(length(a))

		for i in range(length(a)):
			infile.write_byte(get(a, i).cint)
			infile.write_int(get(a, i).freq)

		txt0 = open(file)
		txt = txt0.read()
		for c in txt:
			for i in f:
				if ord(c) == i[0]:
					code += i[1]
		if code is not "":
			infile.write_code(code)
		infile.close()
		txt0.close()

		return tree_to_string(t)
	else:
		empty = HuffmanBitsWriter(out)
		empty.write_byte(0)
		empty.close()
		return ""

# file, out -> file txt
# Opens file with bytes header and decodes back into written txt in file.
# def huffman_decode(file,out):
#	pass
def huffman_decode(file, out):

	infile = HuffmanBitsReader(file)
	outfile = open(out, "w")

	number_of_bytes = infile.read_byte()
	empty_freqs = List([0]*256, 256, 256)
	
	total = 0

	#rebuilding list of occurences.
	for i in range(number_of_bytes):
		c = infile.read_byte()
		o = infile.read_int()
		empty_freqs.lst[c] = o
		total += o

	leaf_list = hleaf_maker_decode(empty_freqs)
	tree = builder(sort(leaf_list, comes_before), comes_before)

	for i in range(total):
		letters(infile, tree, outfile)

	if tree == None:
		outfile.close()
	outfile.close()
	infile.close()

# file, tree, outfile -> writes into outfile
# traverses tree and rights letters if 1 or true on right side and if 0 nope.
# def letters(bitfile, tree, out):
#	pass
def letters(bitfile, tree, out):
	if type(tree) == Hleaf:
		out.write(chr(tree.cint))
	else:
		bit = bitfile.read_bit()
		if bit == True:
			letters(bitfile, tree.right, out)
		else:
			letters(bitfile, tree.left, out)

# tree -> string
# returns string of chr value in tree in prefix order.
# def tree_to_string(tree):
#	pass
def tree_to_string(tree):
	if type(tree) == Hleaf:
		return chr(tree.cint)
	else:
		return tree_to_string(tree.left) + tree_to_string(tree.right)

def code_builder(node, char_bin = "", char_tuple_list=empty_list()):
	if type(node) == Hnode:
		code_builder(node.left, char_bin + "0")
		return code_builder(node.right, char_bin + "1")
	elif type(node) == Hleaf:
		char_tuple_list = add(char_tuple_list, length(char_tuple_list), (node.cint, char_bin))
	return char_tuple_list.lst

def encode_work2(tree, code=""):
	if type(tree) == Hnode:
		result = []
		for i in encode_work(tree.left, code + "0"):
			result.append(i)
		for i in encode_work(tree.right, code + "1"):
			result.append(i)
		return result
	if type(tree) == Hleaf:
		return [(tree.cint, code)]

	


p = code_builder( Hnode(6, 99, Hleaf(99, 1), Hnode(5, 97, Hleaf(97, 3), Hleaf(98, 2))))
print(p)

#g = encode_work2(Hnode(6, 99, Hleaf(99, 1), Hnode(5, 97, Hleaf(97, 3), Hleaf(98, 2))))
#print(g)
