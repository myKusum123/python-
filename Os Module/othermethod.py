#readlines()method- The readline method reads a single line from the file. if we want to read 
#multiple lines, we can use a loop
# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     print(line)# yo first print hunxa
#     if not line :
#      print(line,type(line))#class string dekhauxa
#      break
    
# the readlines()method reads all the lines of the file and returns  them as a list of strings
'''
why readline ,ethod is used
-because it helps you to read any file line by line
'''
#3 subject have 3 students marks
# f=open('myfile3.txt','r')
# i=0
# while True:
#     i=i+1# i ko value badae janxa
#     line=f.readline()
#     if not line :
#      break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f'marks of students {i} in math is : {m1}')
#     print(f'marks of students {i} in social is : {m2}')
#     print(f'marks of students {i} in Grammer is : {m3}')
    # ahile gari rakheko sab string ho yedi hamile intiger ma change garnu xa vani typecasting ko use garnu parni hunxa

# This marks is out of 50 and i want to calculate its percentage then so i have to double them to get the percentage
# f=open('myfile3.txt','r')
# i=0
# while True:
#     i=i+1# i ko value badae janxa
#     line=f.readline()
#     if not line :
#      break
#     m1=int(line.split(",")[0])# int le number ma lerauxa
#     m2=int(line.split(",")[1])
#     m3=int(line.split(",")[2])
#     print(f'marks of students {i} in math is : {m1*2}')# m1 ma *2 garni ani percentage ma auxa but double double ani hamile int ma convert garnu parxa string kina ki ahile yo string ma xa
#     print(f'marks of students {i} in social is : {m2*2}')
#     print(f'marks of students {i} in Grammer is : {m3*2}')

'''
*writelines()method
The writelines ()method in python writes a sequence of string to a file. The sequence can be any iterable object , such as a list or a tuple

In down example : This will write the strings in the lines list to the file myfile.txt The\n xharacter are used to add newline characters to the end of each string.

'''
f=open('myfile.txt','w')
lines=['line\n','line 2\n', 'line 3\n']# it is iterable kina ki writelines use gareko xau ani line by line paste hunxa txt ma
f.writelines(lines)
f.close

#========
'''
keep in mind that the writeness() method doesnot add newline character between the strings in the sequence. if you want to add newlines between the strings , you can use a loop to write each string seperately

'''
f=open('myfile.txt','w')
lines=['line1','line 2', 'line 3']
for line in lines:
 f.write(line + '\n')
f.close