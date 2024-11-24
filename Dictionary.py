# Example 1: Creating and printing a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Example 2: Accessing dictionary items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Example 3: Duplicate keys in a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Example 4: Dictionary length
print(len(thisdict))

# Example 5: Dictionary with different data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Example 6: Checking the type of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Example 7: Using the dict() constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Example: Get the value of the "model" key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:

# Example: Get the value of the "model" key
x = thisdict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example: Get a list of the keys
x = thisdict.keys()
print(x)

# Example: Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# Get Values
# The values() method will return a list of all the values in the dictionary.

# Example: Get a list of the values
x = thisdict.values()
print(x)

# Example: Make a change in the original dictionary, and see that the values list gets updated as well
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Example: Add a new item to the original dictionary, and see that the values list gets updated as well
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

# Example: Get a list of the key:value pairs
x = thisdict.items()
print(x)

# Example: Make a change in the original dictionary, and see that the items list gets updated as well
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Example: Add a new item to the original dictionary, and see that the items list gets updated as well
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example: Check if "model" is present in the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Example 1: Adding an item to the dictionary using a new key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Example 2: Adding an item to the dictionary using the update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


# Example 1: Using pop() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print("After pop('model'):", thisdict)

# Example 2: Using popitem() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print("After popitem():", thisdict)

# Example 3: Using del keyword to remove a specific item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print("After del thisdict['model']:", thisdict)

# Example 4: Using del keyword to delete the entire dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)  # Uncommenting this line will cause an error because "thisdict" no longer exists.

# Example 5: Using clear() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print("After clear():", thisdict)


# Example dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

# Use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)

# Use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)

# Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
  print(x, y)

# Example 1: Using the copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Example 2: Using the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#using the copy() method and the dict() function. Both methods create a new dictionary that is a copy of the original, allowing changes to be made to the copy without affecting the original dictionary.

# Example 1: Creating a nested dictionary
myfamily = {
  "child1": {
      "name": "Emil",
      "year": 2004
  },
  "child2": {
      "name": "Tobias",
      "year": 2007
  },
  "child3": {
      "name": "Linus",
      "year": 2011
  }
}

# Example 2: Creating separate dictionaries and then nesting them
child1 = {
  "name": "Emil",
  "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}

# Accessing items in a nested dictionary
print(myfamily["child2"]["name"])  # Output: Tobias

# Looping through nested dictionaries
for x, obj in myfamily.items():
  print(x)
  for y in obj:
      print(y + ':', obj[y])