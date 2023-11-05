#typecasting=change or convert one data type into anothe data type
# Two Types of Type casting
#1.Explict Conversion - user le chahera convert garni
#2.Implict Conversion - python le convert garni

# Explict Conversion
pie='3.14'
x=float(pie)
print(type(pie)) # type function
print(x)
print(type(x))

converted_to_float=4.5
#print(type(converted_to_float))
#List
my_list=[1,2,4,3]
#print(tuple(my_list))

#create a tuple and converted to list example a=10 abd a =11 but a collects 11 
my_tuple=(1,2,3,4)# 1=0,2=1,3=2
my_list=list(my_tuple)
#print(my_list)
my_list[0]=12
my_tuple=tuple(my_list)
print(my_tuple)
#print(my_list[0])

String1='Harry'
print('string')
list1=list(String1)
print(list1)
list1[0]=20
list1[1]=100
print(list1)
String1=str(list1)
print(String1)

a='1'
b='2'
print(int(a))
print(int(b))

# Implict Conversion
c=2
d=10.2
print(c+d)


# Indexing

'''integer_variable= 1
print (type(integer_variable))

float_variable= 1.2
print (type(float_variable))'''
# Indexing and Slicing
name="Kusum Magar"
print(type(name))
print(name[0:5])# print kusum 
print(name[1])# print u
print(name[0:])# Kusum Magar
print(name[:4])# print kusu
print(name[6:]) #print magar
print(name[::-1])# reverse hunxa name