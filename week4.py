# name="soha Ramadan"
# name1=name
# name1=name1+"s"
# print (hex(id(name)))# location in memory 
# print (hex(id(name1)))
# print(name,name1)
# ==================================================
# string tricks
name = "soha"
# print (name[0])
# print (name[-1])
# print (name[:2]) #so
# print (name[::2]) #sh swap 1 letter
print (name[::-1]) #revers string
# ==================================================

# """ 
# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
#  """
# def first_and_last(message):
#     if  message == "" or message[0] == message[-1] :
#         return True
#     else:
#         return False

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))


# fruit = "Mangosteen "
# print(id(fruit))
# a=fruit.replace("M","x")
# print(id(a))
# print(a)
# print(fruit[:5] + fruit[5:])
# a="ali ibrahim"
# print(a.index("ikk"))

# mutable same varible diffrent memory locations  so is False == True
# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# if a == b:
#     print(True)
# else:
#     print(False)
#----------------------------search for characters or string------------------
#name= "Soha @ gmail.com"
#print("S"  in  name)
#a="yes soha".lstrip()
#print(a)
#a="yes soha".rstrip()
#print(a)
# print("soha".endswith("sa")) # معرفة اذا كانت تنتهي بسلسلة فرعية معينة ام لا
# print("Soha".isnumeric())#معرفة اذا كانت االسلسلة رقمية
# print("123".isnumeric())
# print("-".join(["Soha","Saad","Mohammed","Ramadan"]))
# print("Soha Saad Mohammed Ramadan".split())
# def combine_lists(list1, list2):
# # Generate a new list containing the elements of list2
# # Followed by the elements of list1 in reverse order
#     new_list = list2
#     for i in reversed(range(len(list1))):
#         new_list.append(list1[i])
#     return new_list
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))
