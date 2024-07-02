# Two different ways to remove all elements from this list:
numbers = [1, 2, 3, 4]

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