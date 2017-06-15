import sys
import unittest
from linked_list import *
#class Song models a song with attributes like:
#song number
#song’s title
#song artist
#song album
class Song:
    def __init__(self, num, title, artist, album):
        self.num = num
        self.title = title
        self.artist = artist
        self.album = album

    def __eq__(self, other):
        return ((type(other) == Song)
          and self.num == other.num
          and self.title == other.title
          and self.artist == other.artist
          and self.album == other.album
        )

    def __repr__(self):
        return ("Song({!r}, {!r}, {!r}, {!r})".format(self.num, self.title, self.artist, self.album))
#None->String
#prints the menu
def print_menu():
    print('Song Catalog\n1) Print Catalog\n2) Song Information\n3) Sort\n4) Add Songs\n0) Quit')
#String,List->List
#adds the file contents to Song objects
def add_to_catalog(file_name,songs_list):
    fin = open(file_name,'r')
    for line_no, line in enumerate(fin):
        a=line.split('--')
        #temp_line=str.rstrip(str.lstrip(line))
        if len(line.strip()) == 0 :
            continue
        elif(len(a)>2):
            #print(Song(length(songs_list),a[0],a[1],a[2]))
            songs_list=add(songs_list,length(songs_list),Song(length(songs_list),a[0],a[1],a[2]))
        else:
            print("malformed song at",line_no+1)
    return (songs_list)
#List->None
#prints the entries in the class object after being called by foreach
def print_catalog(current_obj):
    print(str(current_obj.num)+'--'+current_obj.title+'--'+current_obj.artist+'--'+current_obj.album)
    return None
#List,number->None
#prints the particular song Information
def song_information(songs_list,song_number):
    if(song_number<0 or song_number>=length(songs_list)):
        print('... Invalid song number')
        return None
    else:
        current_obj=get(songs_list,song_number)
        print(str(current_obj.num)+'--'+current_obj.title+'--'+current_obj.artist+'--'+current_obj.album)
        return None
#number->string
#prints the menu and accepts what the user wants to do
def menu(choice='default'):
    global songs_list
    while(choice!='0'):
        if(choice=='default'):
            songs_list=empty_list()
            songs_list=add_to_catalog(sys.argv[1],songs_list)
            print_menu()
            menu(input('enter choice:\n'))
        elif(choice=='1'):
            foreach(print_catalog,songs_list)
            print_menu()
            menu(input('enter choice:\n'))
        elif(choice=='2'):
            song_number=eval(input("Enter song number\n"))
            song_information(songs_list,song_number)
            print_menu()
            menu(input('enter choice:\n'))
        elif(choice=='4'):
            songs_list=add_to_catalog(sys.argv[1],songs_list)
            print_menu()
            menu(input('enter choice:\n'))
        else:
            print('invalid choice\n')
            print_menu()
            menu(input('enter choice:\n'))
menu()
