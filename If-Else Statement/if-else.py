''' Input-(for cli)It is a function thet we can use in python to take input form users through 
terminal(yo terminal mai kam garxa)
IF-Else
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''
#userage=input('What is your age')# hamile string matra rakhna milxa input ma[=variable(username)le data(input())]lai assign gari raxa .yesle terminal ma input magi rako hunxa
#variable ko kam chai data ko location tha pauni ho
#print(username)
#user_name=int(userage)
#print(type(user_name)) 
a=10
b=5.4
c=a+b
d=int(b)
#print(type(username))

#print(d)
#print(type(b))
#print(c)


#If else statement= condition is true or false (comparison or variable operation yo condition ma boolean value hunxa
#yo program le variable  boolean value store gari raxa 
raining=True


if raining:
    print('take your umbrella')
else:
   print('donot take umbrela')


#yo program le operation comparison garni kam gareko xa boolean value
a=4
b=2

if a>b:
       print
       
       ('a is greater than b')
elif a==b:    #yedi arko condition launu xa vani if else ko bich ma elif rakhdah hunxa
       print('A is equal to b') 
elif a<b:    
       print('b is greater than a')             
else:
       print('a is not greater than b')

# hamile if double lekhna milxa
print('***************Calculator*****************')
print('select your operation')
a=int(input('enter your a number'))

b=int(input('enter your b number'))

if a>b:
    print('A is greater than B')
    if b<a:
     print(' B is greater than A')
    else:
       print('Those values might be equal')
       if a==b:
          print('They are equal')


# Another example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short Hand If(If you have only one statement to execute, you can put it on the same line as the if statement.)
a=20
b=10
if a > b: print("a is greater than b")

# Short Hand If ... Else(If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:)
# with two conditions
a = 2
b = 330
print("A") if a > b else print("B")
# with 3 conditions 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")# a>b xa vani A print garxa and a==b xa vani = print garxa ani dubai ma k he xaina vani B print garxa

# And  (using if)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#   Or (using if)
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not (using if)
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested If -You can have if statements inside if statements, this is called nested if statements.
# ( if statement vitra chai ajhai if statement layo vani nestes if vaninxa)
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    #  if pni print hunxa and if vitra ko if pni print hunxa

# The pass Statement-if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# ( hamile  if ko k he code lekhi sakeu and kunai reason le if statement with no content rakhnu paryo so teslai ignore or avoid error garna ko lagi nested if use garxau)

a = 33
b = 200

if b > a:
  pass


