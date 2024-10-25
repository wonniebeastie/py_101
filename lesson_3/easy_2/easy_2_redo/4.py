# PROBLEM
# Given a list of numbers `[1, 2, 3, 4, 5]`, mutate the list by removing
# the number at index 2, so that the list becomes `[1, 2, 4, 5]`.

numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers) # [1, 2, 4, 5]
# We can use the `del` keyword to remove the element at index `2`
# during runtime. 

numbers = [1, 2, 3, 4, 5]
numbers.pop(2) 
print(numbers) # [1, 2, 4, 5]
# This one uses the `pop` list method to "pop out" the element at index
# 2. This method is mutating, which is why printing the original list
# prints `[1, 2, 4, 5]`.

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers) # [1, 2, 4, 5]
# This one utilizes the `remove` list method. But this time, instead of
# passing the index position as the argument, we pass the element that
# we want removed from the list.

