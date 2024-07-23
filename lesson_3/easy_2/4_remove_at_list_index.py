# Given: [1, 2, 3, 4, 5]
# Mutate the list by removing # at index 2.
# Ending up with: [1, 2, 4, 5]

# MY SOLUTION
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)
# The `.pop()` list method removes an element at the specified index #
# and is mutating.
print(numbers)  # [1, 2, 4, 5]

# SOLUTION
# numbers = [1, 2, 3, 4, 5]
# del numbers[2]
# print(numbers)  # [1, 2, 4, 5]
