'''
#Datatype
The type of data we use in program for various operation or work

 #Datatype in Python
*string
*Integer
*Float
*List
*Set
*Tuple
*Dictionary
*Boolean
*None

#String 
-  double ya single quatation vitra symbol ,number ra name  hunu paryo string ma
*Text Data
a= "Hello World" 
a= variable and "hello world"= string
print (type(a)) - kun data type ho thapauni
print(a)- a lai print garni
print (a [0])- 0 ma kun word parxa vanera tha pauni
example
a= 'Hello world  25468*((25485))'
a="Hello World"
a= "Hello World's"#if we want to use this (')  in string then  we use double quatation
a= 'Hello World"s'# if we want to use this (")  in string then  we use single quatation
 
#Integer
- it is a number
Product_price= 123456
Quantity= 10
 print('Product_price*Quantity)

 # Float
 - we use decimal number
 decimal_number= 2.6
 print (decimal_number)

 
 #list - Mutable
 - we use square bracket[]
 - in square bracket we put group of data like string float integer etc
 - we can put duplicate data in list eg: a=['apple' 'apple', 2,2,3,4] here apple
   cames two time and number 2 is also comming 2 times
 -we can change the define data in list 
  Product_list=["hello world" ,2 , 2.5]- here we are using string, float ,integer etc 
  so we called list because here is group of other data

  #Set
  -It is  unique group of data which is use in {}
  - We use curle bracket{}
  -in curle bracket we put only integer and float
  - number and float should be unique
   
  a={2,3,2.5}
  print(a)

 # Tuple - Immutable
 - we use small bracket()
 -in small bracket we put group of other data like string float integer etc
 - we use unique data
 -we cannot change the define data in Tuple
 data means small bracket vitra vako-('apple',2,3,5.6) 
Product_list=('apple',2,3,5.6)- only unique number and name has came we cannot repeat it

#Dictionary
-It is a group of data of  value and key
-we use curle bracket{}
-key should be in unique
a= {'a':'rama'} here 'a' is a key and we have to put :(column) and then 
    we use that key value 'rama' in curle bracket

#Boolean
- we use in true or false
- we used in operations
- define fact 

#NoneType
-yesko kam chai kali xa yeso kunai data hudae na
-hamile variable banauna man lageko xa but variable vitra kunai data rakhna 
mn xaina ahile paxi rakhnni ho vani hamile none use garna sakxau
- hamile k he operation garna mildae na
a= none

# Why we use data types in python
kina ki data types anusar kam hunxa program and every data types have different nature
according to it behave 
example: string vaneko euta text data ho ra text data anusar behave garxa
       : integer vaneko euta number data ho ra number data anusar behave garxa
#type()
-type() vaneko function  kina ki yesma group of words ma paranthesis use vako xa
 like bracket ,comma or paranthesis diyera word lai call garnu nai function ho  
- if we dont know the what type of data then we use type() 
example: a=(type(a)) j pni huna sakxa data like string, float etc
'''
# String Example
e= "Hello World"
print (type(e))
print(e)
print (e [0])
f= 'Hello world  25468*((25485))'
print (f)

g= ''' Hello World's 
"name" '''# if we want to use single and double quatation then we use triple quatation and triple quatation can use for comment also and multiple or new line
print(g)
h= "Hello World's"#if we want to use this (')  in string then  we use double quatation
print(h)
i= 'Hello World"s'# if we want to use this (")  in string then  we use single quatation
print(i)
 
 #Integer Example
Product_price= 123456
Quantity= 10
print(' Multiplication of Product_price and Quantity:', Product_price * Quantity)

#Float Example
decimal_number= 2.6
print (decimal_number)

#list Example
Product_data=["hello world" ,2 , 2.5]
print (Product_data)
Product_data=["hello world","hello world" ,2 , 2, 2.5]

#Set Example
a={2,3,2.5}
print(a)

# Tuple
Product_list=('apple',2,3,5.6)
print(Product_list)

# Dictionary
b= {'a':'rama','b':'cow','c':'10'}
print (b)

#Boolean
c=True
print(c)

#None type
d=None
print(d)

# Type Function= type()
print(type(d))
print(type(['2']))

# Types of operator
'''Arithmetic Operators
 -mathmatical operators(+,-,*,/,%,) like :addition ,subtraction ,division
#Assignment Operators
# Comparision Operators
 #Logical Operators
-And: if both statement is true then then the result will be true  
-Or: if the one statement is true then the result will be true
-Not: if the statement is true then the result eill be false(reverse)
#Membership Operators
# Identity Operators
#Bitwise Operators
'''

#===================================================================================
# 1. Arithmetic Arithmetic Operators
   #addition operators(we can add same data type) but we cannot add different types
   #  of bracket, string and integer or we can add up to tuple not set
   #concatenate= add two string using +
a=6
b=9
c=2.5
#print(a+b+c)
a='2.5'
b='3'
#print(a+b)
a= 'hello'
b='world'
#print(a+b)
a='hello'
b='2'
#print(a+b)

c=['hello',2,3]
d=['2',3,4]
#print(c+d)
# Subtraction Arithmetic Operator( we can use integer and float data type)
a=20
b=30
#print(a-b)

# Multiplication Arithmetic Operator
# we can multiply string and number not an string* string but we can multiply float and integer
a=23
b=36
#print(a*b)
a='23'
b=5
#print(a*b)#we  can use string for duplication(2323232323)

#Division Arithmetic Operator(we can divide float and integer)
a=10
b=2
c=a/b
#print(a/b)
#print(type(c))
a=10.2
b=3
#print(a/b)

#Foor Arithmetic Operator( we use //)decimal vandah aagadi ko value matra aauxa or decimal bahek aru number return garxa
a=10
b=2
#print(a//b)

#Exponential Arithmetic Operator(power of something)we use**
a=3
b=4
#print(a**b)

#Modulus Operator(we use %) divide ko reminder nikalxa
a=20
b=3
#print(a%b)

# 2.Assignment operator( a variable le hello data assign gari raxa) (= [equal to]means assignment operator variable lai data assign garnu nai)
''' = is a assignment operator, assigs data yto variable   
 why we need assignment operator-because kahile kahi hami snga dherae data huna sakxa tyo
#data lai chai feri feri use garnu parxa so tyo thulo data lai lekhi rakhnu vanda baru 
variable ma store garni ra recall garni feri'''
a='Hello'
#print(a)

 #Add assignment operator(add only variable or variable vari... matra kam garxa)
a=10
b=20
# a and b vlaue lai add garera naya value banau nu xa
c=a+b
a+=b#(if you want to add old and new variable then you can use+= ani yo  aagadi ko left pati variable chai ma store hunxa)
#print(a)
#print(c)

#subtract assignment operator
a=20
b=30
#a=60(yesle over ride gari raxa pahila ko a lai)
print(a-b)
a-=b
b-=a
#print(b)
#print(a)
 # MUltiply assignment Operator
a=20
b=30
#print(a*b)
a*=b
#print(a)
 
#Division assignment Operator
a=20
b=30
print(a/b)
a/=b
#print(a)

#Floor Assignment Operator
a=20
b=30
a//=b
#print(a)

#Exponential Assignment Operator
a=20
b=30
a**=b
#print(a)

# Modulus Assignment Operator
a=20
b=30
a%=b
#print(a)

#3.Comaprision Operator(compare the two data)
# Greater than
a=6
b=3
#print(a>b)#(a is bigger than b)

# Less Than
a=2
b=3
#print(a<b)#(a is smaller than b)

#is equal
a=3
b=3
#print(a==b)

#not  is equal
a=5
b=3
#print(a!=b)

# Greater than or equal to
a=5
b=4
print(a>=b)
a=4
a=4
#print(a>=b)

#less than or equal To
a=8
b=6
#print(a>=b)
a=4
a=4
#print(a>=b)

#4. LOgical Operators
#a. And Operator
a=8
b=6
c=10
d=9
e= a>b and c>d
 #print(e)
f=a<b and c<d#(And operators check whether the two operations is true , if one of them operation is false
#if one of them operation is false 
# it returns false and if both are operation is true then it returns true)
#print(f)

#b.Or gate
a=8
b=6
c=10
d=9
e= a>b or c>d #( or operaters  check whether one of two operations is true,
#if true then it returns true , else if two operation is false it returns false)

print(e)
f=a<b or c>d or c<a
#print(f)

#c.not gate
a=8
b=6
c=10
d=9
e= not (a>b and c>d)# reverse gardinxa value ya data lai
#print(e)

#5. Membership Operators (euta data chai arko data ko part ho ki nai vanera chaeck garxa)
# we can use string, set, list and dictionary()
# group of data sanga matra use huni vayo in le integer sanga use hunna
# 1. In Operator
'''a= 'kusum'
b='m'
e="kusum Magar"
f="magar"
g=e in f
c=a in b
d=b in a
print(c)
print(d)# true because m ma kusum include hunxa
print (g)#false because f ma kusum include xaina
iteration - group of data ma euta euta jani ho . for example here is [abcd] then it goes ['a','b']'''
a=4.5
b=['hello',1,2,4.5]# we can use string, set, list and dictionary()
c=a in b
#print (c)

d='a'#(value check hunna key  sanga matra check hunxa in dictitonary)'
e={'a':'hello','b':'world'}
f=d in e
#print(f)

g='hello world'#(string is a group  character ho tesaile check hunxa )
h='hello'
i=h in g
#print(i)

j=4
k=(4,5,6)
l=j in k
#print(l)

#2. Not in operator
a='hello'
b='hello world'
c=a not in  b
#print (c) false it is oposite of in
a='hi'
b='hello world'
c=a not in  b
#print(c) true 

#6. Identity operator( idenity check garxa duitai eutai ho ki nai vanera)
#Is Operator
a='hello'
b='hello '
c=a is b# ora==b
print (c)

#is not operator
a='hello'
b='hello '
c=a is not b# or a !=b( != yesle chai data sanga kam garxa) and (is not le chai binary level ma pni check garxa)
print(c)

#7. Bitwise Operator -(binary level ma kam garxa)-(use & this symbol)
# And bitwise operator
a=7
b=6
c= a & b
#print(c)
'''1 2 4 8 (yesma chai 1 ra 0 aayo vani 0 return hunxa)
1 1 1   
0 1 1
-----
0 1 1=6
'''

#Or bitwise operator(| use this symbol)
'''
1 2 4 8 (yesma chai 1 ra 0 aayo vani pni 1 return garxa)
0 1 1   
1 1 0
-----
1 1 1=7
'''

a=6
b=3
c= a | b
#print(c)

# Invert bit wise operator -~ use this symbol
'''
-1-6 = -7(yesle -1 garni kam garxa ra - add garxa)
'''
a=~6
print(a)

#Shift right bit wise operator
a= 8
c=a>>8 #(yesle chai two step uta lani garxa data lai)
print (c)

#Shift left bit wise operator
a= 5
c=a<<5
print(c)

# XOR bit wise Operator
a=3
b=2
c=a^b
print(c)
'''
421
011
010
===
 01
'''





# *Arithmetic operation
# *Add
# a=10
# b=14
# #c=a+b
# a+=b
# print(b)
# a='6'
# b='8'
# c='kusum'
# print(a+b+c)

# a=('kusum',2,2.5) add ma chai up to tuple add hunxa but set disvtionary hudae na
# b=('magar',3,3.5)
# print(a+b)

# *subtraction we cansubtract integer and float
# a=20
# b=10
# c=a-b
# a-=b
# print(a)

# *multiplication-we cant multiply string and string but we can multiply string and float 
# a=10
# b=10
# a*=b
# print(a)
# *Divide-only integer and float
# a=10
# b=2
# a/=b
# print(a)

# *floor- point vandah aagadi ko number matra nikalxa
# a=10
# b=2
# a//=b
# print(a)
# *Exponential-it works for the power of 
# a=10
# b=2
# a**=b
# print(a)

# *modulus- reminder
# a=10
# b=2
# a%=b
# print(a)

#Comparision operator

# *Greater than(>)
# a=10
# b=2
# print(a>b)

# #Smaller than(<)
# a=2
# b=3
# print(a<b)

#equal to( ==)
# a=1
# b=1
# print(a==b)

#not equal(!=)
# a=10
# b=20
# print(a!=b)

#Greater than or equal to(>=)
a=10
b=20
print(b>=a)

#smaller than or equal to(<=)
a=10
b=20
print(a<=b)

#Logical Operators

# And (euta pni false vayo vani false hunxa)
# a=10
# b=20
# c=30
# d=10
# c=a<b and c>d # true beacuse both variable are true
#c= a>b and c<d(false because both are false if one also false then it will false )
# print(c)

#Or (euta matra true vayo vani true hunxa)
# a=10
# b=20
# c=30
# d=10
# e=a<b or c<d
# print(e)

#not
# a=10
# b=20
# c=30
# d=10
# e=not(a<b and c>d)
# print(e)

#Membership
# 1. in 
# 2. in not

# a='kusum'
# b='k'
# print(b in a)
# #Membership tuple
# a=('kusum')
# b=('kusum',2,3)
# print(a in b)

# #Membership set is not allowed
# a={'kusum'}
# b={'kusum',2,3}
# print(a in b)

# #Membership Dictionary key matra ralhni
#in
# # a='k'
# # b={'m':'gar','r':'rai','k':'kus'}
# # c=a in b
# # print(c)

# #not in
# a='m'
# b='magar'
# print(a not in b)

# #identifier = is
# # is not
# a='kusum'
# b='m' 
# print(a is not b)

# is
# a='kusum'
# b='kusum'
# print(a is b)

# * Bitwise Operator
# And Bitwise(	x & y)
# a=10
# b=20
# print (a&b)

#or bitwise(x | y)
# a=20
# b=5
# c=a|b
# print(c)

# invert bitwise or not bitwise(~x)

a=~20
print(a)

# XOR bitwise (The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:)
# 6 = 0000000000000110
# 3 = 0000000000000011

#left shift bitwise or Zero fill left shift(x << 2)

a=20
b=a<<2
print(b)

#right shift bitwise or Signed right shift	(x >> 2)
a=30
b=a>>3
print(b)




