# make a program with your intro to print type of that you make a program
name='Kusum'
age=28
height=5.3
address='Kalanki'
marriage=False
print(f'''My name is{name}
          I am {age}  years old
          I live in {address}
          I am married {marriage}
           ''')
print (f'''{type(name)} 
           {type(age)}  
           {type(height)}  
           {type(address)}  
           {type(marriage)}  
           ''' )
print (type(age))
print (type(height))
print (type(address))
print (type(marriage))
e= "Hello World"
print (type(e))
print(e)
print (e [5])
print(e[::-1])
f= 'Hello world  25468*((25485))'
print (f)
# we can change in tuple  in list and set but cant change in dictionary


my_tuple=('kusum' , 2,5.2)
list_name=list(my_tuple)
print(list_name)
list_name[1]='Magar'
my_tuple=tuple(list_name)
print(my_tuple)


my_set={'kusum',5,2,2.5}
my_list=list(my_set)
print(my_list)
my_list[3]=2.6
my_set=set(my_list)
print(my_set)


a=('kusum',5,2,3,4)
list_a=list(a)
print(list_a)
list_a[2]='magar'
print(list_a)
a=tuple(list_a)
print(a)