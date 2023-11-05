
# variable is a name location in memeory that stores a values 
x=8
print(x)# globale variable
def kusum():
    x=5# local variable
    print(f'The local variable is {x}')
    print("Hi all of you !")
print(f"The globa variable is{x}")
kusum()# function recall gareko so mathi ko run vayesi matra yo run hunxa
print(f"The global variable is{x}")
'''
Local variable-is a variable that is defined within a function and is only accessible within that function it is created when function is called and is destroyed when the function returns 


Global Variable-is a variable that is defined outside of a function or within a function and is accessible from with any function in your code 

'''
# if i want to change  the global variable which is x=10 so what should i do  inside the my_function so that global x becomes 5 and modify the global  variable from within a function
x=10# global variable
def my_function():
    global x
    x=5# mathi ko x global ma print hunna yaha ko print hunxa x
    y=5# local variable
    print(y)
my_function()
print(x)
#print(y)# this variable will cause an error because y is a local variable and is not accessible outside of the functiom