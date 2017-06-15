import sys
import unittest
from linked_list import *
from array_list import *

# -lst, lst, index -> boolean, funtion
# -Checks values of list in index and compares them. Made spacifically for array lists.
# -If values are equal, compares next index by calling another compare function.
# -Order by # -album -> artist -> title -> number
# -def compare(lst1,lst2,index):
# -pass

#test
def compare(lst1, lst2):
  if lst1 < lst2:
    return True
  elif lst1 == lst2:
    return False
#number
def compare0(lst1, lst2):
  if lst1[3] < lst2[3]:
    return True
  elif lst1[3] == lst2[3]:
    return False
#title
def compare1(lst1, lst2):
  if lst1[2] < lst2[2]:
    return True
  elif lst1[2] == lst2[2]:
    return compare0(lst1,lst2)
#artist
def compare2(lst1, lst2):
  if lst1[1] < lst2[1]:
    return True
  elif lst1[1] == lst2[1]:
    return compare1(lst1,lst2)
#album
def compare3(lst1, lst2):
  if lst1[0] < lst2[0]:
    return True
  elif lst1[0] == lst2[0]:
    return compare2(lst1,lst2)

# -lst, input -> lst
# -Hub user input on sorting
# -User's choice chooses which index sorting will begin at.
# -Invalid choice returns print statement and returns to home().
# -sorter(lst,num):
# -pass
def sorter(lst,num):
  if num == "0":
    sort(lst, compare0)
    home(lst)
  if num == "1":
    sort(lst, compare1)
    home(lst)
  if num == "2":
    sort(lst, compare2)
    home(lst)
  if num == "3":
    sort(lst, compare3)
    home(lst)
  else:
    print("\n... Invalid sort option")
    home(lst)

# -file, lst -> list of arrays
# -Goes though the file, and grabs correctly formatted songs only and provides number.
# -Incorrectly formatted songs are returned as errors with number corresponding to place in file.
# -Used in printing information of songs for option 2 and malform errors.
# -def logger(file,lst):
# -pass
def logger(file, lst):
  print("\nCatalog input errors: ")
  f = open(file)
  count = 0
  for i in f:
    split = i.strip().split("--")
    count += 1
    if split == [""]:
      continue
    elif len(split) == 3:
      lst = add(lst, length(lst), [split[2], split[1], split[0], str(length(lst))])
    else:
      print("line " + str(count) + ": malformed song information")
  return lst

# -lst -> string
# -This will work with the foreach function. The following function will be applied to every index value of the list.
# -Index value = Song classes.
# -def catalog(lst):
# -pass
def catalog(lst):
  print(lst[3]+ '--' + lst[2] + '--' + lst[1] + '--' + lst[0])

# -lst, user input -> string
# -Takes in lst, and number user has inputted.
# -Grabs index value in list at inputted number by user and applies string changes.
# -def info(lst,number):
# -pass
def info(lst,num):
  if 0 <= int(num) < length(lst):
    f = get(lst, int(num))
    print ("\nSong information ...\n    Number: "+ f[3] + "\n    Title: " + f[2] + "\n    Artist: " + f[1] + "\n    Album: " + f[0])
  else:
    print("\n... Invalid song number\n")

# -Nothing -> string
# -Prints out interface for music_catalog.
# -def interface():
# -pass
def interface():
  print("\nSong Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit") 

# lst -> strings
# -Joins all functions together.
# -lst attribute serves as mutable lst that can go into all functions.
# -globals serve to not be reiterated.
# -def home(lst):
# -pass
lst = empty_list()
lst = logger(sys.argv[1], lst)
def home(lst):
  interface()
  user = input("Enter selection: ")
  if user == "1":
    foreach(lst, catalog)
    home(lst)
  if user == "2":
    num = input("Enter song number: ")
    info(lst, num)
    home(lst)
  if user == "3":
    print("\nSort songs\n    0) By Number\n    1) By Title\n    2) By Artist\n    3) By Album")
    num = input("Sort by: ")
    sorter(lst, num)
  if user == "4":
    song = input("Enter song file: ")
    lst = logger(song, lst)
    home(lst)
  if user == "0":
    print("\nYou have exited")
    sys.exit()
  else:
    print("\ninvalid choice")
    home(lst)

# -Running program
home(lst)
