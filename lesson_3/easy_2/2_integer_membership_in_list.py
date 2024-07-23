# Given a number and a list, determine whether the number is included 
# in the list.
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

# MY SOLUTION
print(number1 in numbers)  # False
print(number2 in numbers)  # True

# SOLUTION
# Correct. 
# The `in` keyword can be used to check the existence of an element a 
# list in Python.