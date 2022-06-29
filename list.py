# # a= [111,12,13,43,66,'','']
# # del a[1] # delete element by index
# # a.remove(43)# delete element by value
# # print(a)


# # a = [1, 4, 6, 2, 6, 1]
# # a.insert(22,"soha")
# # print("List before calling pop function:")
# # print(len(a))



# #################################################
# # a[5]=99
# # # list built in function 
# # print (len(a)) # len function 
# # print (1 in a) # check value available
# # for i in a : # iterate value not index
# #     print (i)

# # # for i in range (0,4):# index iteration
# # #     print (i)
# # Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1
# # def get_word(sentence, n):
# # 	# Only proceed if n is positive 
# # 	if n > 0:
# # 		words = sentence.split()
# # 		# Only proceed if n is not more than the number of words 
# # 		if n <= len(words):
# # 			return(words[n-1])
# # 	return("Nothing")

# # print(get_word("This is a lesson about lists", 4)) # Should print: lesson
# # print(get_word("This is a lesson about lists", -4)) # Nothing
# # print(get_word("Now we are cooking!", 1)) # Should print: Now
# # print(get_word("Now we are cooking!", 5)) # Nothing
# def skip_elements(elements):
# 	# Initialize variables
# 	new_list = []
# 	i = 0



# The skip_elements function returns a list containing every other element
#  from an input list, starting with the first element. Complete this function
#  to do that, using the for loop to iterate through the input list.
# 	# Iterate through the list

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for i in range (0,len(elements) ,2):
		# Does this element belong in the resulting list?
		if  :
			# Add this element to the resulting list
			___
		# Increment i
		___

	return []

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


