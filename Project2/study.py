import timeit
import linked_list
import array_list
import random
import sys
sys.setrecursionlimit(10100)
import matplotlib.pyplot as plt
 
# print out the timing results
def print_timing(desc, iterations, seconds):
   print('{}\n\t{} iterations in {} seconds'.format(desc, iterations, seconds))
 
 
# build a list for this test ... the type of list is passed as module
def build_list(n, module, max=10000):
   list = module.empty_list()
   for pos in range(n):
      list = module.add(list, pos, random.randrange(max))
 
   return list
 
 
# the function passed to foreach must take an argument, but we
# don't really want to do anything with it for this experiment
def noop(value):
   pass
 
 
# timeit expects that the function passed will take no arguments, so
# this function gathers the arguments and returns a new function that
# uses them, but that itself does not take any arguments
def build_operation_foreach(list, module):
   def run_foreach():
   	module.foreach(list, noop)
 
   return run_foreach

#############################################################

def less_than(a,b):
	if a < b:
		return True
	else:
		False

def build_operation_sort(list, module, function):
   def run_sort():
   	module.sort(list, function)
 
   return run_sort

#############################################################

def build_operation_add(list1, num_elements, module, max=10000):
	def run_add():
		lst = list1
		for i in range(num_elements):
			lst = module.add(lst, i, random.randrange(max))
	return run_add

#############################################################

def build_operation_get(list1, num_elements, module):
	def run_get():
		for i in range(module.length(list1)):
			module.get(list1, i)
	return run_get

#############################################################

def build_operation_song_info(list1, num_elements, module):
	def run_song_info():
		module.get(list1, random.randrange(num_elements))
	return run_song_info

#############################################################

def build_operation_add_songs_random(initial, add, module):
	def run_add_songs_random():
		initialD = initial
		for i in range(module.length(add)):
			initialD = module.add(initialD, random.randrange(module.length(initialD)), module.get(add, i))
	return run_add_songs_random

#############################################################

def build_operation_add_songs_beginning(initial, add, module):
	def run_add_songs_beginning():
		initialD = initial
		for i in range(module.length(add)):
			initialD = module.add(initialD, 0, module.get(add, i))
	return run_add_songs_beginning

#############################################################

def run_one_experiment_foreach(num_elements, num_iterations, module, lst_foreach):
   list = build_list(num_elements, module)
   to_run = build_operation_foreach(list, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_foreach.append(seconds)
 
   print_timing('{}.foreach identity: {} elements'.format(module.__name__,
      num_elements), num_iterations, seconds)

def run_one_experiment_sort(num_elements, num_iterations, module, function, lst_sort):
   random.seed(1)
   list = build_list(num_elements, module)
   to_run = build_operation_sort(list, module, function)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_sort.append(seconds)
 
   print_timing('{}.sort identity: {} elements'.format(module.__name__,
      num_elements), num_iterations, seconds)

def run_one_experiment_add(num_elements, num_iterations, module, lst_add):
   lst_mt = module.empty_list()
   to_run = build_operation_add(lst_mt, num_elements, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_add.append(seconds)
 
   print_timing('{}.add identity: {} elements'.format(module.__name__,
      num_elements), num_iterations, seconds)

def run_one_experiment_get(num_elements, num_iterations, module, lst_get):
   list = build_list(num_elements,module)
   to_run = build_operation_get(list, num_elements, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_get.append(seconds)
 
   print_timing('{}.get identity: {} elements'.format(module.__name__,
      num_elements), num_iterations, seconds)

def run_one_experiment_song_info(num_elements, num_iterations, module, lst_info):
   list = build_list(num_elements,module)
   random.seed(1)
   to_run = build_operation_song_info(list, num_elements, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_info.append(seconds)

   print_timing('{}.song_info identity: {} elements'.format(module.__name__,
      num_elements), num_iterations, seconds)

def run_one_experiment_add_song_random(num_iterations, module, initial_elements, add_elements, lst_random):
   initial = build_list(initial_elements, module)
   add = build_list(add_elements, module)
   random.seed(1)
   to_run = build_operation_add_songs_random(initial, add, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_random.append(seconds)
 
   print_timing('{}.add_songs_random identity: {} elements'.format(module.__name__,
      add_elements), num_iterations, seconds)

def run_one_experiment_add_song_beginning(num_iterations, module, initial_elements, add_elements, lst_beginning):
   initial = build_list(initial_elements, module)
   add = build_list(add_elements, module)
   random.seed(1)
   to_run = build_operation_add_songs_beginning(initial, add, module)
   seconds = timeit.timeit(to_run, number=num_iterations)
   lst_beginning.append(seconds)
 
   print_timing('{}.add_songs_beginning identity: {} elements'.format(module.__name__,
      add_elements), num_iterations, seconds)
 
 
# let's try just one experiment for now

#plot foreach vs get(DONE)
#3 growth strategies 
#array_list vs linked_list load times(DONE), sort, song_info(DONE), add_songs(2) (DONE)

lst_foreach_L=[]
lst_foreach_A=[]

lst_sort_L=[]
lst_sort_A=[]

lst_add_L=[]
lst_add_A=[]

lst_get_L=[]
lst_get_A=[]

lst_info_L=[]
lst_info_A=[]

lst_random_L=[]
lst_random_A=[]

lst_beginning_L=[]
lst_beginning_A=[]

#############################################################

def beginning(lst, types):
	n=10
	for i in range(4):
		test = run_one_experiment_add_song_beginning(10, types, 1000, n, lst)
		n+=100
	return lst
beginning(lst_beginning_L, linked_list)
beginning(lst_beginning_A, array_list)

plt.plot([10,110,210,310], lst_beginning_L, label="beginning_linked")
plt.plot([10,110,210,310], lst_beginning_A, label="beginning_array")
plt.legend()
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.show()

#############################################################

def randoms(lst, types):
	n=10
	for i in range(4):
		test = run_one_experiment_add_song_random(10, types, 1000, n, lst)
		n+=100
	return lst
randoms(lst_random_L, linked_list)
randoms(lst_random_A, array_list)

plt.plot([10,110,210,310], lst_random_L, label="random_linked")
plt.plot([10,110,210,310], lst_random_A, label="random_array")
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.legend()
plt.show()

#############################################################

def info(lst,types):
	n=10
	for i in range(4):
		test = run_one_experiment_song_info(n, 10, types, lst)
		n+=100
	return lst
info(lst_info_L, linked_list)
info(lst_info_A, array_list)

plt.plot([10,110,210,310], lst_info_L, label="info_linked")
plt.plot([10,110,210,310], lst_info_A, label="info_array")
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.legend()
plt.show()

#############################################################

def getter(lst,types): #COMPARE THIS TO FOREACH
	n=10
	for i in range(4):
		test = run_one_experiment_get(n, 10, types, lst)
		n+=100
	return lst
getter(lst_get_L, linked_list)
getter(lst_get_A, array_list)

#############################################################

def locater(lst,types):
	n=10
	for i in range(4):
		test = run_one_experiment_add(n, 10, types, lst)
		n+=100
	return lst
locater(lst_add_L, linked_list)
locater(lst_add_A, array_list)

plt.plot([10,110,210,310], lst_add_L, label="add_linked")
plt.plot([10,110,210,310], lst_add_A, label="add_array")
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.legend()
plt.show()

#############################################################

def sorter(lst,types, function):
	n=10
	for i in range(4):
		test = run_one_experiment_sort(n, 10, types, function, lst)
		n+=100
	return lst
sorter(lst_sort_L, linked_list, less_than)
sorter(lst_sort_A, array_list, less_than)

plt.plot([10,110,210,310], lst_sort_L, label="sort_linked")
plt.plot([10,110,210,310], lst_sort_A, label="sort_array")
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.legend()
plt.show()

#############################################################

def foreach(lst,types):
	n=10
	for i in range(4):
		test = run_one_experiment_foreach(n, 10, types, lst)
		n+=100
	return lst
foreach(lst_foreach_L, linked_list)
foreach(lst_foreach_A, array_list)

#############################################################

#Foreach vs Get Linked Comparison
plt.plot([10,110,210,310], lst_get_L, label="get_linked")
#plt.plot([10,100,1000], lst_get_A, label="get_array")
plt.plot([10,110,210,310], lst_foreach_L, label="foreach_linked")
#plt.plot([10,100,1000], lst_foreach_A, label="foreach_array")
plt.xlabel("Number of Elements")
plt.ylabel("runtime in seconds")
plt.legend()
plt.show()