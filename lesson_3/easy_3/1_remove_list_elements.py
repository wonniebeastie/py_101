# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

# MY SOLUTIONS

# 1
numbers.clear()
print(numbers) # []

# 2
numbers = [1, 2, 3, 4]
index = 0

while index <= 3:
    del numbers[0]
    index += 1

print(numbers) # []


# SOLUTION
# First method was one of the solutions in the example.

# Approach 2:
# while numbers:
#     numbers.pop()

# Approach 2 is so simple & interesting.
# "While `numbers` is truthy, run this code:"
# An empty list is falsy, so this will keep looping until it is empty.
# How elegant! :o

# Note that the following solution will set numbers to an empty list, 
# but it doesn't clear the original list. That's fine if you know there
# are no other references to the list:
# numbers = []