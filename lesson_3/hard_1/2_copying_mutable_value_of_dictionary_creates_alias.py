# What does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)


# MY SOLUTION
# I think `print(num_list)` will output `[1, 2]`.
# I think `print(dictionary)` will output ` {'first': [1]}`.


# SOLUTION
# First one Correct.
# Second one Incorrect.

# num_list = dictionary['first'] 
# This assigns the reference to the memory address that list (`[1]`) 
# that the key `first` is paired up with to `num_list`.
# So `num_list` at this point refers to `[1]`.

# Now `num_list` & the paired value (`[1]`) of `first` in the 
# dictionary both point to the same object in memory.

# num_list.append(2) 
# This line mutates that list with the `.append()` method, which 
# appends an element (in this case, `2`) to the end of the list.
# So at this point `num_list` refers to `[1, 2]`.

# `print(dictionary)` should now output `{'first': [1, 2]}`

# This is because mutating one will reflect on the other. 

# If we want to modify `num_list` without modifying the original 
# dictionary, there are a couple of options:

# 1
# Initialize `num_list` with a reference to a copy of the original list:
dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# 2
# Use list slicing which returns a new list:
dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)