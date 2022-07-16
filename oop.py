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
class Person:
    def __init__(self, fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def __str__(self):
        return f" the first nam eis {self.fname} and last name is {self.lname}"
    
s1= Person("Soha","Saad",17)
print(s1.fname.upper(),s1.lname,s1.age)
s1.age=19 # change attribute values 
print(s1.fname,s1.lname,s1.age)
print(s1)
