import unittest

# * Section 1 (Lists)

# * dd: NumList Data Definition

# "mt" --> means empty!!! Just the way the teacher likes it!

# ListItem is either:
# - string or number

# a List is either:
# - a numlist or Strlist

#a NumList is one of
# - "mt", or
#Pair(first, rest)

# a Strlist is of
# - "mt" or
# - Pair(first,rest)
class Pair:
	def __init__(self,first,rest):
		self.first = first #ListItem
		self.rest = rest #List
	def __repr__(self):
		return "Pair({!r},{!r})".format(self.first,self.rest)
	def __eq__(self,other):
		return type(self) == type(other) and self.first == other.first and self.rest == other.rest

# * 1:

# Strlist -> int
# Finds the length of a Strlist
def length(strlist):
	if strlist	== "mt":
		return 0
	return 1 + length(strlist.rest) #So if not mt, knows first is filled, then goes to rest and calulates that.  


# * 2:

# numlist -> float
# sum the numbers in the numlist
def sum(numlist):
	if numlist == "mt":
		return 0
	else:
		return numlist.first + sum(numlist.rest)

# * 3:

# numlist float -> numlist
# Return number of values in numlist that are greater than the threshold
def count_greater_than(numlist,threshhold):
	if numlist == "mt":
		return 0
	else:
		if numlist.first > threshhold: #Test first number
			return 1 + count_greater_than(numlist.rest,threshhold) #add one since it be true
		else:
			return count_greater_than(numlist.rest,threshhold) #keep going with no additon

# * 4:

# strlist value -> int
#Finds value in the strlist and returns position
def find(strlist,value,position=0):
    if strlist == "mt":
        return None
    else:
        if strlist.first == value:
            return position
        else:
            return find(strlist.rest,value,1+position)


# * 5:

# numlist -> numlist
# Reduces all values in numlist by one
def sub_one_map(numlist):
	if numlist == "mt":
		return "mt"
	return Pair(numlist.first - 1, sub_one_map(numlist.rest))

# * 6:

# numlist -> numlist
# Puts new new_num into correct index in an already sorted least to greatest numlist
def insert(strlist,value):
    if(strlist == 'mt'):
        return Pair(value,'mt')
    else:
        if(strlist.first >= value):
            return Pair(value, Pair(strlist.first, strlist.rest))
        else:
            return Pair(strlist.first, insert(strlist.rest,value))

# * Tests : the test case class for the list functions
class TestCases(unittest.TestCase):
    def test_length(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = length(list1)
        print(Pair(23,"mt"))
        self.assertEqual(test,3)

    def test_length_2(self):
        list1 = "mt"
        test = length(list1)
        self.assertEqual(test,0)

    def test_sum(self):
        list1 = Pair(1.1,Pair(2,Pair(3,"mt")))
        test = sum(list1)
        self.assertEqual(test,6.1)

    def test_sum_2(self):
        list1 = "mt"
        test = sum(list1)
        self.assertEqual(test,0)

    def test_count_greater_than(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = count_greater_than(list1,1)
        self.assertEqual(test,2)

    def test_count_greater_than_2(self):
        list1 = "mt"
        test = count_greater_than(list1,1)
        self.assertEqual(test,0)

    def test_find(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = find(list1,2)
        self.assertEqual(test,1)

    def test_find_2(self):
        list1 = "mt"
        test = find(list1,3)
        self.assertEqual(test, None)

    def test_find_3(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = find(list1,4)
        self.assertEqual(test, None)

    def test_sub_one_map(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = sub_one_map(list1)
        result = Pair(0,Pair(1,Pair(2,"mt")))
        self.assertEqual(test,result)

    def test_sub_one_map_2(self):
        list1 = "mt"
        test = sub_one_map(list1)
        result = "mt"
        self.assertEqual(test,result)

    def test_insert(self):
        list1 = Pair(1,Pair(2,Pair(3,"mt")))
        test = insert(list1,2.5)
        result = Pair(1,Pair(2,Pair(2.5,Pair(3,"mt"))))
        self.assertEqual(test,result)

    def test_insert_2(self):
        list1 = "mt"
        test = insert(list1,2.5)
        result = Pair(2.5, "mt")
        self.assertEqual(test,result)

    def test_insert_3(self):
        self.assertEqual(insert(Pair(11,'mt'),10),Pair(10,Pair(11,'mt')))
        self.assertEqual(insert('mt',10),Pair(10,'mt'))
        self.assertEqual(insert(Pair(1,Pair(3,Pair(5,'mt'))),2),Pair(1,Pair(2,Pair(3,Pair(5,'mt')))))

if __name__ == '__main__':
    unittest.main()



