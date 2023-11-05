'''
Lambda Functions in python
-It is a small Anonymous function without a name
syntax:
lambda arguments: expression
'''
# function use gareko
# def double(x): 
#     return x*2
# print (double(5))

double=lambda x:x*2# hamilae def garnu pni pardae na sidhai answer simple way ma
cube=lambda x: x*x*x# multiply of 3
# aba malai kunai average nikalnu xa like sum divide by something garera
avg=lambda x , y:(x+y)/2
sum=lambda x , y, z:(x+y-z)/2

print(double(5))# print 25 nikalxa
print(cube(5))# print 125 nikalxa
print(avg(3 , 5 ))#print 4 nikalxa
print(sum(3 , 5 , 4))
# hamilae lambda function kahile use garni jaba ki single line ma function lekhna chahanxau

# can we pass a lambda function to another function yes we can
def appl(fx,value):
    return 6+ fx(value)
print(appl(cube, 2))# we can pass function inside another function
#or
print(appl(lambda x: x*x*x))


#########################################
'''

Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:

ExampleGet your own Python Server
Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))
Lambda functions can take any number of arguments:

Example
Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))
Example
Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
Use that function definition to make a function that always doubles the number you send in:

Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
Or, use the same function definition to make a function that always triples the number you send in:

Example
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
Or, use the same function definition to make both functions, in the same program:

Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
Use lambda functions when an anonymous function is required for a short period of time.









'''