# PROBLEM
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

# Alyssa noticed that this code would fail when the input is a
# negative number, and asked Alan to change the loop. How can he make
# this work? Note that we're not looking to find the factors for 
# negative numbers, but we want to handle it gracefully instead of
# going into an infinite loop.

# Bonus Question: What is the purpose of `number % divisor == 0` in
# that code?

def factors(number):
    if number < 0:
        return "Please try again with a non-negative number."

    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(9))  # [1, 3, 9]
print(factors(-4)) # Please try again with a non-negative number.

# My Bonus Question Solution
# The purpose of `number % divisor == 0` is to check if `number` is
# divisible by `divisor`.


# SOLUTION
def factors(number):
    divisor = number
    result = []
    while divisor > 0: # This line was changed !
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

# Bonus Answer: It determines whether dividing the integer `number` is
# by the integer `divisor` leaves a remainder of `0`. That is, 
# `number % divisor == 0` is truthy if number is a factor of
# `divisor`.


# NOTES
# So what I did makes the code longer & does not handle the case in 
# which `number` is `0`.

# LS's solution just adjusts the loop condition itself, effectively
# handling zero and negative cases without needing an extra check. 