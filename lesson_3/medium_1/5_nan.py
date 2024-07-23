# What will this code output?

nan_value = float("nan")

print(nan_value == float("nan"))  # False

# MY SOLUTION
# I think this will throw an error.

# SOLUTION 
# Incorrect.
# It does not throw an error. 
# It outputs "False".
# `nan` is a special numberic value that tells you that an operation 
# that was supposed to return a number failed.
# Python does NOT let you use `==` to check if a value is nan. 




# BONUS QUESTION
# How can you reliably test if a value is nan?

# MY SOLUTION
import math 

print(math.isnan(float("nan")))  # True 

# SOLUTION
# import math

# nan_value = float("nan")

# print(math.isnan(nan_value))