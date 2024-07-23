# Write two distinct ways of reversing the list without mutating the 
# original list.

numbers = [1, 2, 3, 4, 5]     

# MY SOLUTIONS

# A
print(list(reversed(numbers)))  # [5, 4, 3, 2, 1]
# The result of `reversed(numbers)` had to be converted to a list in 
# order to be usable (a.k.a. use with the print function) because the 
# result is a lazy sequence, meaning it can't be used until it's 
# specifically requested.
print(numbers) # [1, 2, 3, 4, 5]

# B
print(numbers[::-1])  # [5, 4, 3, 2, 1]
print(numbers) # [1, 2, 3, 4, 5]