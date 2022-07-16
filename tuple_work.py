# a= ("welcome",2022,"delta","mansoura",2022,"delta")#القيم في tuple لا تتكرر
# #a[0]="come
# print(len(a))
# for i in a:
#     #x= "["+str(a.index(i))+"]"+"="+i
#    #print("[{}] = {}" .format(a.index(i), i))
#    print(f"[{ a.index(i)}] = {i}" )
# example of seperete telephone No
# def fun1 (no):
#     city=no[0:3]
#     phone=no[3:]
#     return city,phone
# seperateTel =fun1("050465678")

# print(f"City code= {seperateTel[0]} , phone nomber ={seperateTel[1]}")
# print(seperateTel)
# #print(type(seperateTel))

# ----------------------------------------------------------
# قيمة الb tuple
# a,c,b=1,2,(3,4,6,7,8,9,0)
# print (f"{a} {b}  ")
# print (type(b))


# #encapsulation as list
# a,*b=1,2,3,4,b
# print (f"{a} {b}  ")
# print (type(b))

# -----------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6]
# # for number in numbers:
# #     print(number,end =" ")

# for number in numbers:
#     print(number, end=" ")

#-------------------------------------------
# ==================================================
# def skip_elements(elements):
#     selected = []
#     for index,element in enumerate (elements):
#         if index %2 == 0:
#             selected.append(element)#يكتب الجملة كاملة
#             # selected+=element#يكتب الحرةف منفصلة 
#     return selected
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
