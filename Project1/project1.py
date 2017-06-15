import unittest

# a Strlist is of
# - "mt" or
# - Pair(first,rest)
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __eq__(self, other):
    	if type(other) == Pair:
    		first_eq = (self.first == other.first)
    		rest_eq = (self.rest == other.rest)
    		return first_eq and rest_eq
    	else:
    		return False
    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))

# a class with
# name being a string
# a Strlist is of
# - "mt" or
# - Pair(first,rest)
class ClassShape:
    def __init__(self, name, strlist):
        self.name = name
        self.strlist = strlist
    def __eq__(self, other):
        return ((type(other) == ClassShape)
          and self.name == other.name
          and self.strlist == other.strlist)
    def __repr__(self):
        return ("ClassShape({!r}, {!r})".format(self.name, self.strlist))

# strlist -> strlist
# Takes in strlist and turns values into "{!r}" except for "mt"
def multi_sub(strlist):
	if strlist == "mt":
		return "mt"
	value = "{!r}"
	return Pair(strlist.first.replace(strlist.first,value), multi_sub(strlist.rest))

# strlist -> string
# Takes in strlist and seperates values into seperate lines 
def join_lines(strlist):
    if strlist == "mt":
        return ""
    return strlist.first + '\n' + join_lines(strlist.rest)

# strlist -> strlist
# Takes strlist and returns strlist with addition of self.{value} = {value} to each value
def fields_to_assignments(strlist):
	if strlist == "mt":
		return "mt"
	return Pair("    " + "    " + "self." + strlist.first + " = " + strlist.first,fields_to_assignments(strlist.rest))

# strlist -> strlist
# Takes a strlist and returns strlist with values exchanged for {tabX2} and self.{value} == other.{value}
def fields_to_assignments_eq(strlist):
	if strlist == "mt":
		return Pair("                )", "mt")
	return Pair("                " + "and self." + strlist.first + " == other." + strlist.first,fields_to_assignments_eq(strlist.rest))

# strlist -> strlist
# Takes in strlist and returns strlist with values for {tabX} self.{value}
def fields_to_assignments_repr(strlist):
	if strlist == "mt":
		return "mt"
	return Pair("self." + strlist.first,fields_to_assignments_repr(strlist.rest))

# strlist -> string
# Takes in strlist and returns values seperated by commas
def commasep(strlist):
	if strlist == "mt":
		return ""
	return ", " + strlist.first + commasep(strlist.rest)

# strlist -> strlist
# Takes in strlist and returns strlist with starting value being int definition and then followed by fields_to_assignments values
def init_method(strlist):
	if strlist == "mt":
		return Pair("    def __init__(self):", Pair("        pass", "mt"))
	return Pair("    " + "def __init__(self" + commasep(strlist) + "):", fields_to_assignments(strlist))

# strlist -> strlist
# Takes in strlist and returns strlist with starting value being eq definition and then followed by field_to_assignment_eq values
def eq_method(ClassShape):
	if ClassShape.strlist == "mt":
		return Pair("    " + "def __eq__(self, other):", Pair("        " + "return (type(other) == " + ClassShape.name, Pair("                )", "mt")))
	return Pair("    " + "def __eq__(self, other):", Pair("        " + "return (type(other) == " + ClassShape.name, fields_to_assignments_eq(ClassShape.strlist)))

# strlist -> strlist
# Takes in strlist and returns strlist with starting value being repr definition and then followed by field_to_assignment_repr values
def repr_method(ClassShape):
	if ClassShape.strlist == "mt":
		return Pair("    " + "def __repr__(self):", Pair("    " + "    return " + '"' + ClassShape.name + '()"' + ".format()", "mt"))
	return Pair("    " + "def __repr__(self):", Pair("    " + "    return " + '"' + ClassShape.name + "(" + ClassShape.strlist.first.replace(ClassShape.strlist.first,"{!r}") + commasep(multi_sub(ClassShape.strlist.rest)) + ')".format(' + ClassShape.strlist.first.replace(ClassShape.strlist.first, "self." + ClassShape.strlist.first) + commasep(fields_to_assignments_repr(ClassShape.strlist.rest)) +")", "mt"))

# strlist -> string
# Takes in strlist and converts into whole creation of boilerplate for any stated class with any amount of attributes
def render_class(ClassShape):
	return "class " + ClassShape.name + ":"  + "\n" + join_lines(init_method(ClassShape.strlist)) + "\n" + join_lines(eq_method(ClassShape)) + "\n" + join_lines(repr_method(ClassShape))

class TestCases(unittest.TestCase):
	#1
	def test_multi_sub(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = multi_sub(list1)
		self.assertEqual(test, Pair('{!r}', Pair('{!r}', Pair('{!r}', 'mt'))))
	#2
	def test_multi_sub_2(self):
		list1 = "mt"
		test = multi_sub(list1)
		self.assertEqual(test, "mt")
	#3
	def test_join_lines(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = join_lines(list1)
		self.assertEqual(test, 'x\ny\nz\n')
	#4
	def test_join_lines_2(self):
		list1 = "mt"
		test = join_lines(list1)
		self.assertEqual(test, "")
	#5
	def test_fields_to_assignments(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = fields_to_assignments(list1)
		self.assertEqual(test, Pair('        self.x = x', Pair('        self.y = y', Pair('        self.z = z', 'mt'))))
	#6
	def test_fields_to_assignments_2(self):
		list1 = "mt"
		test = fields_to_assignments(list1)
		self.assertEqual(test, "mt")
	#7
	def test_fields_to_assignments_eq(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = fields_to_assignments_eq(list1)
		self.assertEqual(test, Pair('                and self.x == other.x', Pair('                and self.y == other.y', Pair('                and self.z == other.z', Pair('                )', 'mt')))))
	#8
	def test_fields_to_assignments_eq_2(self):
		list1 = "mt"
		test = fields_to_assignments_eq(list1)
		self.assertEqual(test, Pair("                " + ")", "mt"))
	#9
	def test_fields_to_assignments_repr(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = fields_to_assignments_repr(list1)
		self.assertEqual(test,  Pair('self.x', Pair('self.y', Pair('self.z', 'mt'))))
	#10
	def test_fields_to_assignments_repr_2(self):
		list1 = "mt"
		test = fields_to_assignments_repr(list1)
		self.assertEqual(test, "mt")
	#11
	def test_commasep(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = commasep(list1)
		self.assertEqual(test,  ", x, y, z")
	#12
	def test_commasep_2(self):
		list1 = "mt"
		test = commasep(list1)
		self.assertEqual(test,  "")
	#13
	def test_init_method(self):
		list1 = Pair("x",Pair("y",Pair("z", "mt")))
		test = init_method(list1)
		self.assertEqual(test, Pair('    def __init__(self, x, y, z):', Pair('        self.x = x', Pair('        self.y = y', Pair('        self.z = z', 'mt')))))
	#14
	def test_init_method_2(self):
		list1 = "mt"
		test = init_method(list1)
		self.assertEqual(test, Pair("    def __init__(self):", Pair("        pass", "mt")))
	#15
	def test_eq_method(self):
		list1 = ClassShape("Point", Pair("x", Pair("y",Pair("z", "mt"))))
		test = eq_method(list1)
		self.assertEqual(test, Pair('    def __eq__(self, other):', Pair('        return (type(other) == Point', Pair('                and self.x == other.x', Pair('                and self.y == other.y', Pair('                and self.z == other.z', Pair('                )', 'mt')))))))
	#16
	def test_eq_method_2(self):
		list1 = ClassShape("Point", "mt")
		test = eq_method(list1)
		self.assertEqual(test, Pair("    " + "def __eq__(self, other):", Pair("        " + "return (type(other) == " + "Point", Pair("                )", "mt"))))
	#17
	def test_repr_method(self):
		list1 = ClassShape("Point", Pair("x", Pair("y",Pair("z", "mt"))))
		test = repr_method(list1)
		self.assertEqual(test, Pair('    def __repr__(self):', Pair('        return "Point({!r}, {!r}, {!r})".format(' + 'self.x, self.y, self.z)', 'mt')))
	#18
	def test_repr_method_2(self):
		list1 = ClassShape("Point", "mt")
		test = repr_method(list1)
		self.assertEqual(test, Pair("    " + "def __repr__(self):", Pair("    " + "    return " + '"' + "Point" + '()".format()', "mt")))
	#19
	def test_render_class(self):
		print(render_class(ClassShape("Point", Pair("x", Pair("y",Pair("z", "mt"))))))
	#20
	def test_render_class_2(self):
		print(render_class(ClassShape("Point", "mt")))
	#21
	def test_Pair(self):
		print(Pair("x", Pair("y", Pair("z", "mt"))))
	#22
	def test_ClassShape(self):
		print(ClassShape("Point", Pair("x", Pair("y", Pair("z", "mt")))))
	#23
	def test_Type(self):
		self.assertEqual(ClassShape("Point", Pair("x", Pair("y",Pair("z", "mt")))), ClassShape("Point", Pair("x", Pair("y",Pair("z", "mt")))))

if __name__ == '__main__':
	unittest.main()


