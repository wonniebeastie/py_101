# PROBLEM
# Write two different ways to remove all of the elements from the 
# following list:

# The `clear()` method
numbers = [1, 2, 3, 4]

numbers.clear()
print(numbers) # []


# `while` loop
numbers = [1, 2, 3, 4]

index = 0
while numbers:
    numbers.pop()
    index += 1

print(numbers) # []
# After solution: You don't need to set the index.

# --------------------------------------

# This doesn't work bc of the way the `del` keyword works.
numbers = [1, 2, 3, 4]

for num in numbers:
    del num

print(f"numbers{numbers}")

# The following are bad ideas because mutating the list while iterating
# through it can lead to unexpected results.

# `for` loop with `pop()` method
# Removing the element at index 0 then incrementing `index` makes it
# skip over one. 
numbers = [1, 2, 3, 4]

index = 0
for num in numbers:
    numbers.pop(index)
    index += 1

print(numbers) # [2, 4]

# This doesn't work because the `for` loop exits early thinking there
# aren't enough items left for the loop to complete the 4 ~planned~
# iterations. 
# Must take into account the list length changing as it loops.
numbers = [1, 2, 3, 4]

for num in numbers:
    numbers.pop(0)

print(numbers) # [3, 4]


# `for` loop with `remove()` method
numbers = [1, 2, 3, 4]

for num in numbers:
    numbers.remove(num)

print(numbers)  # [2, 4]

# ---------------------------------------

# SOLUTION

# Approach 1
numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers) # []


numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

print(numbers) # []

# The solution below just reassigns an empty list to `numbers`, it 
# doesn't actually clear the original list, so it doesn't really work.
# But this is fine if you know there are no other references to the 
# list.
numbers = []