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