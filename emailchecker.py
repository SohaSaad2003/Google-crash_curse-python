# email checker ===( we can use index function 0rn we make it )
""" a= "soh3a@hotmail.com"
inx = a.index('3')
print(inx)
 """
#########################
# inx=0
# for i in a :
#     if '@'==i :
#         name = a[:inx]
#         print (i,"index =",inx,name)
#     inx+=1

# ---------------------------format String output---------------
# a= 3
# b = 5
# s= "soha"
# print("a===>",a,"b======>",b)
# print("a===> {0} b======>{1}".format(a,b))
# print("a===> {a} b======>{b}".format(a=b*2,b=b))

# print("a===> {} b======>{}".format(a,b))
# print("a===> %d b======>%s "%(a,s))
# # the best output 
# print(f"a===> {a} b======>{s} ")

# ---------------------------Task---------------

#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam"
# def student_grade(name, grade):
# 	return "name {} recieved grade {}% on the exam ".format(name,grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# ---------------------------format String decimal---------------


a= 10
b = 598877.6754
s= "soha"
# print("a===>",a,"b======>",b)
# print("a===> {0:.2f} b======>{1:.0f}".format(a,b))
# print("a===> {a:.2f} b======>{b:.2f}".format(a=b*2,b=b))

# print("a===> {:.2f} b======>{}".format(a,b))
# print("a===> %d b======>%s "%(a,s))
# the best output 
# print(f"a===> {a:.2f} b======>{s} ")

# ------------------- بحجز عدد حانات للاحراج --------------------------
# for i in range (1,10):
#     a*=4
#     print("a===> {:>12.2f} b======>{}".format(a,b))


# -------------
#count the substring in any string ex. sting " soha soha " substring "soha " count =2
#string.count(substring) Returns the number of times substring is present in the string
#string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.



# a= "soha  soha  "
# x= a.count("a",0,5)
# print (x)
# print(a.replace("soha","saad"))
# print (a)

a= ["hello","my",'age']

print (**a)
print (a)

