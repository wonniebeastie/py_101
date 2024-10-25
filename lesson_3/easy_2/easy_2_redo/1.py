# PROBLEM
# Write two distinct ways of reversing the list without mutating the 
# original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(numbers[::-1]) # [5, 4, 3, 2, 1]
# This one uses the slicing syntax to extract the entire sequence but
# in reverse. Extracting like this does not mutate the original list.

print(list(reversed(numbers))) # [5, 4, 3, 2, 1]
# This one uses the `reversed()` built-in function to reverse `numbers`
# but the returning value is a lazy sequence; So we have to use a
# type constructor here in order to print the elements.

print(numbers is list(reversed(numbers))) # False
# Using the identity operator `is` shows us that these two objects are
# not the same.