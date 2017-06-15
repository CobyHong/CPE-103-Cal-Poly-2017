from array_list import *
import sys


class Song:
    def __init__(self, number, name, artist, album):
        self.number = number
        self.name = name
        self.artist = artist
        self.album = album
    def __eq__(self, other):
        return ((type(other) == Song)
          and self.number == other.number
          and self.name == other.name
          and self.artist == other.artist
          and self.album == other.album
        )
    def __repr__(self):
        return ("Song({!r}, {!r}, {!r}, {!r})".format(self.number, self.name, self.artist, self.album))

##################################################

# -file, lst -> strings
# -Goes through the file, and prints out malformed errors.
# -Ignores white space
def errors(file, lst):
  f = open(file)
  count = 0
  print("Catalog input errors: ")
  for i in f:
    split = i.strip().split("--")
    count +=1
    if split == [""] or len(split) == 3:
      continue
    else:
      print("line " + str(count) + ": malformed song information")

##################################################

# -file, lst -> list class
# -Goes though the file, and grabs correctly formatted songs only.
# -Used in printing information of songs for option 2.
def logger(file, lst):
  f = open(file)
  count = 0
  for i in f:
    split = i.strip().split("--")
    if split == [""]:
      continue
    elif len(split) == 3:
      lst = add(lst, length(lst), Song(count, split[0], split[1], split[2]))
      count +=1
  return lst

##################################################
def print_catalog(input):
	if input == "1":
		catalog(sys.argv[1], empty_list())
		home()
# -file, lst -> strings.
# -Prints out the catalog for option 1.
# -Does not implement logger.
def catalog(file, lst):
	f = open(file)
	count = 0
	dash = "--"
	for i in f:
		split = i.strip().split("--")
		if split == [""]:
			continue
		elif len(split) == 3:
			count += 1
			print(str(count-1) + dash + i.strip())

##################################################

def enter_song_info(input):
	if input == "2":
		return print_info()
# -None -> strings
# -Prints out the Song information inputted by user.
# -Does not have attributes since called by enter_song_info, which contains attribute needed.
def print_info():
	user = input("Enter song number: ")
	g = len(logger(sys.argv[1], empty_list()).lst)
	if 0 <= int(user) <= g-1:
		f = grabber(int(user))
		print ("Song information ...\n    Number: "+ str(f.number) + "\n    Title: " + str(f.name) + "\n    Artist: " + str(f.artist) + "\n    Album: " + str(f.album))
		home()
	else:
		print("... Invalid song number")
		home()

##################################################

def enter_song_file(input,lst):
	if input == "4":
		return add_song(lst)
# -file -> list class
# -Adds songs from another file into existing list
# -Uses logger to do this
def add_song(lst):
	user = input("Enter name of file to load: ")
	lst = logger(user, lst)
	home()

##################################################

# -None -> strings, user input
# -Interactive interface for user and area where all functions are combined and runned.
# -Some function have functions to run them.
lst = empty_list()
lst = logger(sys.argv[1], lst)
def home():
  errors(sys.argv[1], lst) #malformed errors
  print("Song Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit") #menu
  user = input("Enter selection: ") #user input
  print_catalog(user) #option 1 
  enter_song_info(user) #option 2
  enter_song_file(user,lst) #option 4
  quit(user) #option 0

##################################################


def quit(input):
	if input == "0":
		sys.exit()


# -index -> index value
# -Gets index value of logger
# -More efficient than get function
def grabber(index):
	f = logger(sys.argv[1], empty_list()).lst[index]
	return f

##################################################

home()

#print(logger("song_list", empty_list()))
