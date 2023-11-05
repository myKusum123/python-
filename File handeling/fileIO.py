#Python has several functions for creating, reading, updating, and deleting files.

'''
*Opening a file -Before we can perform any operations on a file we must first open it. python provides the open()function to open a file . it takes two arguments : The name of the file and the mode in which the file should be opened. The mode can be 'r' for reading and 'w' for writing and a for appending
Example:(how to open a file for reading)
f=open('myfile.txt','r')# myfile.txt vanni xuttai file banau nu parni hunxa balla erroe aaudae na

*File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append(add something to the end of a written document append ko meaning) - Opens a file for appending, creates the new file if it does not exist

"w" - Write - Opens a file for writing, creates the new file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

-In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.
'''
#***********************************************************************
#read
'''
*Open a File on the Server
Assume we have the following file, located in the same folder as Python:

demofile.txt# it is a file name

Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

-To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:

Example:
f = open("demofile.txt", "r")
print(f.read())

*If the file is located in a different location, you will have to specify the file path, like this:

Example
Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

*Read Only Parts of the File
-By default the read() method returns the whole text, but you can also specify how many characters you want to return:

Example:
-Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

*Read Lines
-You can return one line by using the readline() method:

Example
Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())

-By calling readline() two times, you can read the two first lines:

Example
Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

-By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)
*Close Files
-It is a good practice to always close the file when you are done with it.

Example
Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

'''
# example
f= open('myfile.txt','r')# myfile.txt vanni chai file ho and yo chai xuttai new file open 
#garnu parxaani r vaneko chai read ho yesle open garxa
#f= open('myfile.txt') yo matra gareu vani pni run hunxa kina ki read default mode ho
text=f.read()# text vaneko chai variable name ho and read le chai f variable  ko read garxa
print(text)
f.close()# yo close garni bani chai garnu parxa yesle chai file lai close garxa
#*************************************************************************************************
# Write(w)
'''
*Write to an Existing File
-To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

ExampleGet your own Python Server
Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
Example
Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
Note: the "w" method will overwrite the entire file.

*Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

Example
Create a file called "myfile.txt":

f = open("myfile.txt", "x")
Result: a new empty file is created!

Example
Create a new file if it does not exist:

f = open("myfile.txt", "w")


'''
#Example:write (w)

f= open('myfile2.txt','w')# hamile w le arko file nikalna sakxau or create file
text=f.read
print(text)
f.close()
#++++++++++++++++++

#using append
f = open("myfile2.txt", "a")# jati choti append run garxau teti choti nai add hunxa and close chai garnu parxa hai ani balla dekhau xa output ma
f.write(" Now the file has more content!")# myfile2.txt ma yo add hunxa( Now the file has more content!)
f.close()# yeha samma ,matra lekhyo vani k he pni print hudae na so ahmile read garnu parni hunxa ani balla sab run hunxa
#open and read the file after the appending:
f = open("myfile2.txt", "r")
print(f.read())

#+++++++++++++
f = open("myfile3.txt", "w")# yo chai ekchoti matra output ma dekhau xa print vako
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("myfile3.txt", "r")
print(f.read())

###########################################################################
'''
*Python Delete File
Delete a File
-To delete a file, you must import the OS module, and run its os.remove() function:

Example:
Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
Delete Folder
To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":

import os
os.rmdir("myfolder")
Note: You can only remove empty folders.
'''

'''
text(t)-t mode is used to handle text files. t refers to the text mode there is no difference between r and rt or w and wt since text mode is the default. The default mode is r(open for reading text synonym of rt)
example:
f=open('myfile.txt','rt')
text=f.read()
f.close()

binary(b)=used to handle binary file {image,pdfsetc}

f=open('myfile.txt','rb')# jbg ma lanu xa vani image ma lanu xa vani
text=f.read()
f.close()
'''
# text(t)
f=open('myfile.txt','rt')
text=f.read()
f.close()
#b(binary)
f=open('myfile.txt','rb')
text=f.read()
f.close()
#############################
'''
*With statement
you can use the with statement to automatically close the file you are done with it
'''
with open('myfile.txt4','a') as f:
    f.write("hey i am inside with")# hamile close gari rakhnu pardae na aafai atomaticaly close hunxa with statement le


    '''
    why we need to know filehandeling
    -the reason is that if you know file handeling ver well so suppose you are making any game and you have to save its highest score you can do that . you can store any data of your program inside the file in a way you can use the files as tempt database or you can use as a data store if you want to store anything
    '''