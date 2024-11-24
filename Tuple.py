# Creating a Tuple
thistuple = ("apple", "banana", "cherry")
print("Tuple:", thistuple)

# Tuples Allow Duplicate Values
thistuple_with_duplicates = ("apple", "banana", "cherry", "apple", "cherry")
print("Tuple with duplicates:", thistuple_with_duplicates)

# Tuple Length
print("Length of tuple:", len(thistuple))

# Create Tuple With One Item
single_item_tuple = ("apple",)
print("Single item tuple type:", type(single_item_tuple))

# NOT a tuple
not_a_tuple = ("apple")
print("Not a tuple type:", type(not_a_tuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print("Tuple with strings:", tuple1)
print("Tuple with integers:", tuple2)
print("Tuple with booleans:", tuple3)

# A Tuple with Different Data Types
mixed_tuple = ("abc", 34, True, 40, "male")
print("Mixed data types tuple:", mixed_tuple)

# Checking Tuple Type
mytuple = ("apple", "banana", "cherry")
print("Type of mytuple:", type(mytuple))

# Using the `tuple()` Constructor
constructed_tuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print("Constructed tuple:", constructed_tuple)


# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print("Second item:", thistuple[1])

# Negative Indexing
print("Last item:", thistuple[-1])

# Range of Indexes
thistuple_extended = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Items from index 2 to 5:", thistuple_extended[2:5])

# Range from the beginning to a specific index
print("Items from start to index 4:", thistuple_extended[:4])

# Range from a specific index to the end
print("Items from index 2 to end:", thistuple_extended[2:])

# Range of Negative Indexes
print("Items from index -4 to -1:", thistuple_extended[-4:-1])

# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("Updated tuple:", x)

# Add Items by converting to a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("Tuple after adding an item:", thistuple)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print("Tuple after adding another tuple:", thistuple)

# Remove Items by converting to a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("Tuple after removing an item:", thistuple)

# Delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# Uncommenting the next line will raise an error because the tuple no longer exists
# print(thistuple)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("Green fruit:", green)
print("Yellow fruit:", yellow)
print("Red fruit:", red)

# Unpacking with Asterisk (*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print("Green fruit:", green)
print("Yellow fruit:", yellow)
print("Red fruits:", red)

# Unpacking with Asterisk (*) in the middle
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print("Green fruit:", green)
print("Tropical fruits:", tropic)
print("Red fruit:", red)


# Example 1: Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Example 2: Loop Through the Index Numbers
for i in range(len(thistuple)):
  print(thistuple[i])

# Example 3: Using a While Loop
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)