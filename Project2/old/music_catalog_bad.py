from array_list import *
from linked_list import *
import sys

#Current Issue:
#	-Values out of index in Enter song number return larger error.

# -Home screen and center where all functions are put.
# -Calls all functions and functions runs based on conditionals put on user's input
def home():
	print("Song Catalog\n    1) Print Catalog\n    2) Song Information\n    3) Sort\n    4) Add Songs\n    0) Quit\n")
	user = input("Enter selection:")
	quit(user)
	print_catalog(user)
	enter_song(user)
	
##################################################

# -Prints out the catalog portion while also returning back to home screen.
# -If input is out of range, states Invalid options and returns to home screen.
def print_catalog(input):
	if input == "1":
		result = []
		count = 0
		dash = "--"
		f = formatter()
		for i in f:
			result.append(str(count)+dash+i)
			count += 1
		print("\n".join(result))
		home()
	elif input < "0" or input > "4":
		print ('Invalid option')
		home()

##################################################

def enter_song(input):
	if input == "2":
		return print_song()

# -If user inputs 2, prompts input for song number and displays information of song at that list number + prompts up home screen.
# -If invalid song or out of list, returns error and prompts back up home screen.
def print_song():
	user = input("Enter song number:")
	g = formatter()
	if 0 <= int(user) <= len(g)-1:
		f = split_fucking_song(int(user))
		print ("Song information ...\n    Number: "+ user + "\n    Title: " + f[0] + "\n    Artist: " + f[1] + "\n    Album: " + f[2])
		home()
	else:
		print("... Invalid song number")
		home()

##################################################

# -If user inputs 0, terminates program.
# -Will have to reopen python file to use again.
def quit(input):
	if input == "0":
		print("You have exited")
		sys.exit()

##################################################

# -Helper function
# -Reads file and puts items into list, seperated by.
def list_shit():
	result = []
	f = open(sys.argv[1])
	for i in f:
		if i.rstrip():
			result.append(i.rstrip())
	return result

##################################################

# -Helper function
# -Turns each item in list_shit() into its own list by seperating by "--".
def split_fucking_song(index):
	f = formatter()[index]
	result= f.split("--")
	return result

##################################################

# -Helper function
# -Checks validity of songs in list, removes those that have incomplete information.
def formatter():
	result = []
	f = list_shit()
	for i in f:
		if i.count("--") == 2:
			result.append(i)
	return result

##################################################

#Initializing all functions. 
home()