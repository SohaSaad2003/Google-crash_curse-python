x={
    'name':"soha",
    'age':19,
    'tel':234423233,
}
# print(x['age']) # print dict value 
# print(x) # print dict (value and keys )
# print('name' in x) # check key in dict 
# for key in x:
#     print(key,"=>",x[key] )
# x['name'] ="basant"# update value 
#del x['name'] # delete key with its value
# for key, value in x.items(): # unpack values and keys
#     print(key,value)
# print(x.keys(),x.values()) # dictinary values and keys (mutable )

# for value in x.values(): # reurn value in iteration
#     print(value)

# def count_letters(text): # count letter in any sentenses
#     result={}
#     for letters in text:
#         if letters not in result:
#             result[letters]=1
#         else:
#             result[letters]+=1
#     return result
# print(count_letters("ssaad"))
# x={
#     'name':"soha",
#     'age':19,
#     'tel':234423233,
# }

# y=x
# x["age"]=29
# print (x)
# print (y)  # {'name': 'soha', 'age': 29, 'tel': 234423233} =x  (mutable same memmory adresss)
            #{'name': 'soha', 'age': 29, 'tel': 234423233}=y 
# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)
def format_address(address_string):
  # Declare variables
  house_no = ""
  street_no = ""
  # Separate the address string into parts
  sep_addr = address_string.split()
  # Traverse through the address parts
  for addr in sep_addr:
    # Determine if the address part is the
    if addr.isdigit():
      house_no = addr
    else:
      street_no = street_no+addr
      street_no = street_no + " "
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_no,street_no)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"




