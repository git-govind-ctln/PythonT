# Creating a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate Values in a Set
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 as Duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 as Duplicates
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Getting the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Different Data Types in a Set
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Mixed Data Types in a Set
set1 = {"abc", 34, True, 40, "male"}

# Checking the Data Type of a Set
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Using the `set()` Constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)