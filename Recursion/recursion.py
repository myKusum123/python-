'''
Recursion is the process of defining something interms of itself 

IN python , we know a function xan call other functions. It is even possible for the function to call itself 
'''
# factorial(7)=7*6*5*4*3*2*1
# factorial(6)=6*5*4*3*2*1
# factorial(5)=5*4*3*2*1
# factorial(4)=4*3*2*1
# factorial(3)=3*2*1
# factorial(2)=2*1
# factorial(1)=1
# factorial (n)=n * factorial (n-1)

def factorial(n):
    if (n==0 or n==1):
     return 1
    else:
       return n * factorial (n-1)# function lai nai recall garni
print (factorial (3)) 
print (factorial (8)) 
print (factorial (5)) 