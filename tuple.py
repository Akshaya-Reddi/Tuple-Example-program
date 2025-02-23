"""
# Read input as a tuple of strings
input_tuple = tuple(input().split())

# Find lengths of each element in the tuple
length_list = [len(i) for i in input_tuple]

# Find the maximum length
max_length = max(length_list)

# Extract elements with the maximum length
list_max = [i for i in input_tuple if len(i) == max_length]

# Convert the list back to a tuple
tuple_max = tuple(list_max)

print(tuple_max)

"""
# Read input as a tuple of words
input_tuple = tuple(input().split())

# Find the maximum word length
max_length = max(map(len, input_tuple))

# Extract words with the maximum length and convert to tuple
tuple_max = tuple(word for word in input_tuple if len(word) == max_length)

# Print the result
print(tuple_max)
