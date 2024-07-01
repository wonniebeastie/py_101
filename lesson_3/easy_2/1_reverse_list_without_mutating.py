# Two different ways to reverse the list without mutating the original.

numbers = [1, 2, 3, 4, 5]     

print(list(reversed(numbers)))  # [5, 4, 3, 2, 1]
print(numbers) # [1, 2, 3, 4, 5]

print(numbers[::-1])  # [5, 4, 3, 2, 1]
print(numbers) # [1, 2, 3, 4, 5]