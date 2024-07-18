# Function to return all factors of `number`.
# def factors(number):
#     divisor = number
#     result = []
#     while divisor != 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

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

print(factors(-100))

# PROBLEM
# The while loop keeps looping because a negative # is not 0
# and it will keep decrementing so will never be 0, causing an 
# infinite loop.


# BONUS QUESTION
# The purpose of `number % divisor == 0` is to check if the current
# divisor divides into the given number evenly, without leaving a 
# remainder.