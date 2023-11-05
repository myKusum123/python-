'''
Seek() function
- The seek ()function allows you to move the current position within a file to a specific 
point. The position is specified in bytes, and you can move either forward or backward 
from the current position

# suppose you want to  edit the 6th character of file so it's not like that you'll read 
the whole file then you'll write it again by changing the 6th  character it'll not be an 
efficient operation so yesko lagi hamile f.seek ko use garxau
'''
with open('myfile.txt','r') as f:
  print(type(f))# gareu vani kun type ho tha pauxau
# move to the 18th byte in the file
  f.seek(18)# first yeha ko 18 character forward aauxa ani  balla tala data ko read hunxa
 # Read the next 5 bytes
  data =f.read(5)
  print(data)# it will read first 5 character
'''
tell() function
-It returns the current position within the file, in bytes.this can be useful for keeping 
track of your location within tha file or for seeking to a specific position relative to 
the current position

'''
# lets suppose you don't know anything or you are in a big program and you want to know from where the reading will start in this function
with open ('myfile.txt','r') as f:
#read the first 10 bytes
  data=f.read(10)
# save the current position
  current_position=f.tell()# yesle chai kaha samma seek gareko xa print gardinxa like hamile mathi 18 samma seek gareko thiyeu ni ani 18 print garax
# seek to the saved position
  f.seek(current_position)# we can find how many character ahead we are in file


  '''
truncate() function
-when we open a file in python using the open function, you can specify the  mode in which 
you want to opem a file. if you specify the mode as 'w' or'a ' the file is opened the write 
mode and you can write to the file . however if you want to truncate the file to a specific 
size, you can use the truncate() function.

 '''
  with open('sample.txt','w') as f:
    f.write('Hello World')
    f.truncate(5)# 5 character ota matra print hunxa
with open('sample.txt','w') as f:
  print(f.read)