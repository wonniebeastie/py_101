# PROBLEM
# Given a number and a list, determine whether the number is included 
# in the list.
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

# I & O
# I: a list
# O: True or False

# RULES
# - a number and a list will be given.
# - must find whether the given number is included in the given list.

print(number1 in numbers) # False 
print(number2 in numbers) # True

# This code uses the `in` membership operator to see if the given 
# number exists in the given list.