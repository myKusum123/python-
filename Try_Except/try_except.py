'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except 
blocks.
'''
'''Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:

Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:'''

#The try block will generate an exception, because x is not defined:

# try:
#   print(x)
# except:
#   print("An exception occurred")

'''
Many Exceptions
-You can define as many exception blocks as you want, e.g. if you want to execute a special 
block of code for a special kind of error:
'''
# Print one message if the try block raises a NameError and another for other errors:
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

'''  
Else
You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:
'''
# try:
#   print("Hello")# try pi true xa so yo ni run hunxa
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")#and yo print huna

'''
Exceptions in python 
-when these exception occurrs the python interpreter stops the current process and passes it to the calling proocess until it is handled. it is not handled the program will be crash
'''
# a=input('Enter the number: ')
# print(f"Multiplication of {a} is : ")
# try:
#   for i in range (1, 11):
#     print(f"Multiplication of {int(a)} X {i} = {int(a)*i}")
# except Exception as e:# Exception as e nalekhe pni hunxa lekhe pni hunxa lekhyo vnai chai hamile k error vako ho tyo pni vandinxa output ma
#   print ('invalid input !')

# print('Some tips are important')# print hunxa hai eni haru chai
# print(' End of program')


# Another example 
# try :
#   num= int (input("Enter an integer: "))
#   a=[6, 3]
#   print(a[num])# [num]- indexing like  is  and 3  is 1
# except ValueError:# hamile aba yes ma chai number bahek aru alphebetic haleu vani print ma j lekheko xa tei out puut ma aauxa
#   print("Number enterd is not an integer.")
# except IndexError:
#   print("Index Error")

# yedi try execute vako xa vani except execute hunnna
#   =====================================
'''finally-The finally block, if specified, will be executed regardless if the try block 
raises an error or not.
The finally code block is also a part of exception hadeling, when we handle excepton using 
the try and except block we can include a finally block at the end. The finally block is 
always executed, so it is generally used for doing the concluding tasks like closing 
database connection or may be ending the program execution with a delightful message

'''
# try:
#   print(x)
# except:
#   print("Something went wrong")# x define vako xaina so tyo false ho ani except run hunxa and finally jahile pni run hunxa
# finally:
#   print("The 'try except' is finished")


def func1():
  try:
    l=[1, 4, 5, 6]
    i=int(input('enter the index: '))
    print (l[i])# number halyo vani error aaudae na aba alphabetic halyo vani error aauxa
    return 1
  except:
    print('some error occured')
    return 0
  
  finally:
    print('I am always executed')
print(func1()) #-yestoh garyo vani error aauxa
# hamile function return gardah pni finally execute garxa
