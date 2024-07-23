# Alan wrote the following function, which was intended to return all 
# of the factors of number:
# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# Alyssa noticed that this code would fail when the input is a negative
# number, and asked Alan to change the loop. 
# How can he make this work? Note that we're not looking to find the 
# factors for negative numbers, but we want to handle it gracefully 
# instead of going into an infinite loop.

# MY SOLUTION

# OBJECTIVE
# Rewrite the code to stop infinite loop/handle error gracefully.

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-100))  # []

# WHAT WAS THE PROBLEM?
# The while loop keeps looping because a negative # is not 0
# and it will keep decrementing so will never be 0, causing an 
# infinite loop.


# BONUS QUESTION
# What is the purpose of number % divisor == 0 in that code?

# MY SOLUTION TO BONUS QUESTION
# The purpose of `number % divisor == 0` is to check if the current
# divisor divides into the given number evenly, without leaving a 
# remainder.