'''
Object oriented programming language is a way from which we will understand  the program  easily
and you will also be able to perform ations on those entities very easily. it is ame to make things
There are two approaches that are use to write program or code
1 procedural programming
2.Object Oriented programming-it helps to map our variables with real world entities

#calss-It is a blueprint or template  for creating  object or it defines the properties and 
methods that an object of that class will have
properties are the data or state of 
an object and methods are the actions

#An object is an instance of class and it contsains its own data and methods 

#Abstraction is the process of hiding the internal details of an application from the outer world. 

#encapsulation in OOPs is the concept of binding fields (object state) and methods (behavior) together as a single unit.

# Inheritance is the concept in OOPs in which one class inherits the attributes and methods of another class.

#Polymorphism is a feature of object-oriented programming languages that allows a specific routine to use variables of different types at different times.

'''
'''
RailwayForm=class(blueprint)
harry-harry ki info wala form-object(entity)
tom-tom ki info wala form-object(entity)
subham-subham ki info wala form-object(entity)


if you want to change the name then
subham.changeName('subhi')


#Self parameter
- Self parameter is a reference to the current instance of the class and use to access variables that belongs to the class

self means that object for which this method is called
'''

# class Person:
#     name='kusum'
#     occupation= 'Software Developer'
#     def info(self):
#         print(f'{self.name} is a {self.occupation}')

# a=Person()
# b=Person()
# a.name ='Sibha'
# a.occupation='backend developer'
# b.name='Kusum'
# b.occupation='Software developer'
# # print(a.name, a.occupation)
# a.info()# yesma chai print gari rakhnu ardae na yo mathi nai print vae sakeko xa
# b.info()# hmaile 
    
'''
Create a Class
To create a class, use the keyword class:
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5
'''
#===========================
'''
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
'''
##############################
'''
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
Note: The __init__() function is called automatically every time the class is being used to create a new object.

'''

#########################
'''

The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

Example
The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
Example
The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
'''
#######################
'''
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
'''
#######################
'''
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example
Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

'''

#Example
# class Car:
#     name='Honda'# properties define gareko properties chai value ra variable lai vanxa 
#     def set_name(self,name):# class vitra function banayo vani function vandae na yeslai.. yeslai method vaninxa
#         self.name=name
#         self.get_name()

#     def get_name(self):# hmaile ()parathensis lai khali rakhadae nau yesma jun name vayeni rakhxau 
#         print (self.name)
# car1=Car()# function vako vaye chai hamile sidae car() vanera call garthim but aba mildae na kina ki yo class ko object bata matra call garna milxa car1=car() garera chai hamile object banako xau
# car1.set_name('honda1')

# Magic Method or constructor- automatically run hunxa yedi certain kam gari raxau vani object sanga and magic method vaneko chai __init__class ko yestoh method h jun chai already class le banae sakeko method ho yo method chai automatic run hunxa jaba hami object certain kam garxau

class Car:
    def __init__(self,name ,speed ,weight): # yo __init__ method vaneko chai yestoh method ho class ko jun chai already define vae sakeko xa and objjet banau dah aafai run unxa# __init__ gareu vani chai already define name ho agi tw hamile set_name yesari name lekhera definegareko thiyeu
     self.name=name
     self.speed=speed
     self.weight=weight
    def __str__(self):#yo method chai taba run hunxa jaba hamile objectt lai print garxau ya value magxau teti khera yo method automatically run hunxa
       return self.name
car1=Car(name="fararii",speed='250km/hr', weight='15000kg')
# print(car1.name,car1.speed,car1.weight)
print(car1)

# Encapsulation

# class User:# yo vayo protective attribute _single underscore
#     def __init__(self, username, password):
#         self._username=username# __username yesma double underscore use vako xa so yo private attribute ho and _username single underscore use garim vanechai protective attribute ho
#         self._password=password
# user1=User('Kusum@1gmail.com', '1234')
# print(user1._username)

# class User:# __double underscore(private attribute) aba yeslai kasari hatauni by using getter
#     def __init__(self, email, password):
#         self.__email=email
#         self.__password=password
#     def get_email(self):#(getter method) yedi hamile private attribute lai bahira show garnu paryo vani chai hamile calss vitra  get lai return garnu parni hunxa
#         return self.__email
#     def set_email(self,email):# setter method vaneko chai private attribute value lai chai change garni method ho
#         self.__email=email
#         self.get_email()# get_email return gareko
        
# user1=User('kanchan7@gmail.com','1234')
# # print(user1.get_email())
# user1.set_email('a@gmail.com')
# print(user1.get_email())
    
