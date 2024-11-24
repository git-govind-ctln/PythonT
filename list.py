# Create a List:

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# # Lists allow duplicate values:

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# #Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# #String, int and boolean data types:

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# #A list with strings, integers and boolean values:

# list1 = ["abc", 34, True, 40, "male"]

# # What is the data type of a list?

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))


# #Using the list() constructor to make a List:

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)


# Print the second item of the list:

# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])



# # -1 refers to the last item, -2 refers to the second last item etc.

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])


# #Return the third, fourth, and fifth item:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# #This example returns the items from the beginning to, but NOT including, "kiwi":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])


# #This example returns the items from "cherry" to the end:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])


# #This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# # Check if "apple" is present in the list:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# #Change the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# #Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# #Change the second value by replacing it with two new values:

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# #Change the second and third value by replacing it with one value:

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# #Insert "watermelon" as the third item:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# #Using the append() method to append an item:

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# #Insert an item as the second position:

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# #Add the elements of tropical to thislist:

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# #Add elements of a tuple to a list:

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# #Remove "banana":

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# #Remove the first occurrence of "banana":

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# #The pop() method removes the specified index.

# Remove the second item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# Remove the last item:

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# #Remove the first item:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# #Delete the entire list:

# thislist = ["apple", "banana", "cherry"]
# del thislist

# #The clear() method empties the list.

# #The list still remains, but it has no content.


# #Clear the list content:

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)