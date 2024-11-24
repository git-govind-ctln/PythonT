# Example 1: range(stop)
# Generates numbers from 0 to stop-1
example1 = list(range(5))
print("Example 1:", example1)  # Output: [0, 1, 2, 3, 4]

# Example 2: range(start, stop)
# Generates numbers from start to stop-1
example2 = list(range(2, 5))
print("Example 2:", example2)  # Output: [2, 3, 4]

# Example 3: range(start, stop, step)
# Generates numbers from start to stop-1, incrementing by step
example3 = list(range(0, 10, 2))
print("Example 3:", example3)  # Output: [0, 2, 4, 6, 8]

# Example 4: range(start, stop, -step)
# Generates numbers from start to stop+1, decrementing by step
example4 = list(range(5, 0, -1))
print("Example 4:", example4)  # Output: [5, 4, 3, 2, 1]

# Example 5: range(-stop, 0)
# Generates negative numbers from -stop to -1
example5 = list(range(-5, 0))
print("Example 5:", example5)  # Output: [-5, -4, -3, -2, -1]

# Example 6: range(0)
# Generates an empty sequence
example6 = list(range(0))
print("Example 6:", example6)  # Output: []

#slicing 

# Define a sample list
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 1: list[start:end]
# Slices the list from index start to end-1
slice1 = sample_list[1:4]
print("Example 1:", slice1)  # Output: [1, 2, 3]

# Example 2: list[start:]
# Slices the list from index start to the end
slice2 = sample_list[2:]
print("Example 2:", slice2)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# Example 3: list[:end]
# Slices the list from the beginning to end-1
slice3 = sample_list[:3]
print("Example 3:", slice3)  # Output: [0, 1, 2]

# Example 4: list[:]
# Copies the entire list
slice4 = sample_list[:]
print("Example 4:", slice4)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 5: list[start:end:step]
# Slices the list from start to end-1 with a step
slice5 = sample_list[0:10:2]
print("Example 5:", slice5)  # Output: [0, 2, 4, 6, 8]

# Example 6: list[::-1]
# Reverses the list
slice6 = sample_list[::-1]
print("Example 6:", slice6)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Example 7: list[-3:]
# Slices the last three elements
slice7 = sample_list[-3:]
print("Example 7:", slice7)  # Output: [7, 8, 9]

# Example 8: list[:-3]
# Slices all but the last three elements
slice8 = sample_list[:-3]
print("Example 8:", slice8)  # Output: [0, 1, 2, 3, 4, 5, 6]