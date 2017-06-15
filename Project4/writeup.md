Project 4
=========

# Team Members:

- Connor Graves
- Abhishek Kundu
- Spencer Gilson
- Coby Hong

# Expected Data Structures
In our opinion, coverage.py uses a linked list in order to track the lines in the code that have yet to be executed. When coverage is run, it creates the linked list and fills it with the line numbers of all executable lines of code. As a line of code is visited and completed, the corresponding value in the list is deleted and a counter increments by one every time to track finished lines. This results in the shrinking of the list and total number of completed lines. When the code being tested is done executing, the remaining items that have yet to be completed in the linked list are the missed lines of code. These remaining items or lines of code in the linked list are then printed onto the screen with stated line or location and the percentage covered; which is calculated by our counter of completed task, divided by the initial size of the list beforehand. This would have a performance of O(n), but it will also be very easy and reliable to implement.

# Initial Code Examination
The files of coverage.py are arranged into 3 main groups. The main section, in the root of the files as far as coverage.py is concerned, holds the setup functions and the main function, responsible for starting up the program. The coverage folder holds all the actual code that tests the coverage of our files. Within this section is a folder with code in C (cTracer). This C code makes up the tracer part of coverage. From looking at the summary.py and result.py files stored in the coverage folder, we have determined that an array list is used to store the unvisited lines of code. The test folder holds tests in test files for each of their counterparts in the rest of the software.
 
[Coverage Directory]
 
Parser.py - Takes lines from input file. Parser then determines which lines are executable code, and what cannot be executed. Lines are then assigned based on their executability. In this file, lines in the file are simply designated as runnable or not.
 
Pickle2json.py - This file simply converts data that is taken in. In total, there are two functions in this file. The first function takes in “coverage data” and turns it into “pickle_read_raw_data”. The last function then converts the output or pickle data from the last function into readable JSON information.
 
Version.py - Version takes in info from “version_info”, which is presented in tuple sets,  and creates a readable string on that info. Additionally, the file has a function creating a URL for coverage.py.
 
Annotate.py - The  functions annotate the lines of the source file using “>”,  “-”, and “!”. After running coverage, these symbols are applied to the lines. “>” stands for executed line, “-” stands for excluded, “ and “!” stand for executable lines they were not run by the report. Overall, this file is made of two functions. One runs the report which tests if each line is run, and the “AnnotateReporter” which applies symbols to represents executed, and not executed lines.
 
Bytecode.py - This file contains only one function and import types module. This function goes through the executed code objects and pushes both the objects and their children into a stack to be returned later. I’m assuming a tree was created labeling a executable code object with its lines on left and right branches. This tree is then stacked based on order of operations.
 
[Tests]
 
Test_results.py - Test to see if the statements, code executed, and missing are done correctly with checker determining if ratio of covered to missed is done properly.
 
Test_pick2json.py - File tests conversion from both ways of coverage data and pickle data. First test works on coverage into pickle data, then another for pickle into JSON. There is as well a function that seems to create a pickle filename from the coverage.

# Detailed Code Examination
While looking at the file tracer.c, found in the C code section mentioned in the previous section, we discovered that it was used to monitor the python script developed by the user, using a stack to track what lines have been executed. The stack is defined in datastack.h and datastack.c and consists of of 3 governing variables. Depth determines the point in the stack that is being pushed or popped(think height, but inverted since adding to a stack in C means increasing the address value, which is down in most memory depictions). Stack is the actual data in the stack, and alloc is the size memory space allocated to the stack, since memory must be manually allocated in C. After all the code is done executing, the values (line numbers that tracer.c saw were executed) in the stack are compared to the line numbers found in the .pyc file of the user.
The line numbers of all executable code in your python program are stored in a table in the .pyc file, and coverage reads that table into lines. The data in the line is a dictionary mapping file names to dictionaries. 
 
The values that exist in the .pyc file, but not in the stack generated by the C code, are the lines of code that were not executed. According to the documentation, that is written in c - in order to reduce runtimes, since running a function in python each time a line is executed adds a significant amount of overhead.  Afterwards in the reporting phase of the code, array lists are used to hold values,such as missed lines and filenames, so that they may be inserted into strings in order to be printed to the user of lines executed, and ratio of covered to uncovered represented as percentage.
 
# Summary
 
The coverage.py folder is scattered all over the place and is difficult to navigate multiple folders within it. The usage of structured comments throughout the files makes the files very easy to read and gives the reader a good sense as to that the functions do. If this code is to be maintained or updated further, the coder should maintain the style and the formatting that has been used throughout. The coder of these files had made sure to define the variables and give a purpose statement for each of the functions. Going through CPE 202, has given us the basic fundamentals of how to write readable code so that it can be easily followed through by another coder. Maintaining the procedure of defining data structures, having a signature for each function and defining its purpose would definitely help a lot in the Software Development Cycle in industry.
 
 
