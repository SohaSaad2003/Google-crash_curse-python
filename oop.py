# list of method in ANY CLASS

# print(dir(0))
# print(dir(""))
# 
#لو محتار في اسم المتغير 
# _= 10
# print(_)

#__ init__
#local method لا تستدعى باسمها
# name = "soha saad ramadan "
# print(name.title())
# help("")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#class and constructor and object 
# class Person:
#     def __init__(self, fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def __str__(self):
#         return f" the first nam eis {self.fname} and last name is {self.lname}"
    
# s1= Person("Soha","Saad",17)
# print(s1.fname.upper(),s1.lname,s1.age)
# s1.age=19 # change attribute values 
# print(s1.fname,s1.lname,s1.age)
# print(s1)



# #___________________________________________________
# class Dog:
#   years = 0
#   def dog_years(self):
#     return self.years*7
    
# fido=Dog()
# fido.years=3
# print(fido.dog_years())

# example in our course 
# class Dog:
#   def __init__(self,years):
#     self.y=years

#   def dog_years (self):
#     return self.y*7
# fido=Dog(3)
# print(fido.dog_years())

#_________________________________________________
#we should create object to show docstring
class Person:
  """Outputs a message with the name of the person class """
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

p1 = Person ("soha")

#help(p1.greeting)
# from re import S


# class Students :
  
#   def __init__(self,name,id,degree):
#     self.name= name
#     self.id=id
#     self.degree= degree
#   def perc(self):
#     """ 11111 دالة تحسب درجة الطالب"""
#     return self.degree/100*100
#   def __str__(self) :
#     return f"name is {self.name} id is { self.id} percntage is {self.perc()}"
# s=Students("Soha",1345,50)

# print(f"name is {s.name} id is { s.id} percntage is {s.perc()}")

# # dconstractur use del 
# del s # delete objects  
# del s.id # delete attribute 

# # help(s.perc)