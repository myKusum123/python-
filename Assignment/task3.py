# CALCULATOR
# Take first and second from user as input.
# Take arithmetic symbols operation from user to perform with those numbers .
# Perform the operation described by the user.

class Calculator:
    def add(self , n1,n2):
        return n1+n2
    def subtract(self, n1, n2):
        return n1-n2
    def multi(self , n1,n2):
        return n1*n2
    def divide(self , n1,n2):
        return n1/n2
calc1=Calculator()

fn=int(input('Enter Your First Number: '))
sn=int(input('Enter Your Second Number: '))
user_Choose=input('Select your operation :+ ,- ,* ,/ : ')

if user_Choose =='+':
    print('The addition of', fn, 'and', sn, 'is', calc1.add(fn,sn))
elif user_Choose =='-':
    print('The Subtraction of ', fn, 'and' ,sn,'is' ,calc1.subtract(fn,sn))

elif user_Choose =='*':
    print('The multi of ', fn, 'and' ,sn,'is' ,calc1.multi(fn,sn))

elif user_Choose =='/':
     print('The Subtraction of ', fn, 'and' ,sn,'is' ,calc1.subtract(fn,sn))

else :
    print('Invalid command')


    



# Get user input


# Function to perform arithmetic operations
# def calculate(num1, num2, operation):
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             return "Division by zero is not allowed"
#         return num1 / num2
#     else:
#         return "Invalid operation"

# # Get user input
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (+, -, *, /): ")

#     result = calculate(num1, num2, operation)
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")