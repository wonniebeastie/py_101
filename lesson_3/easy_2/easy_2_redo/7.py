# PROBLEM
# Write a one-liner to count the number of lower-case `t` characters in
# each of the following strings:
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t')) # 2
print(statement2.count('t')) # 0

# This code uses the `count()` string method to count the number of times
# a value occurs in a string.

# Without the `count()` method:

def count_value(txt):
    count = 0

    for char in txt:
        if char == 't':
            count += 1
    
    return count

print(count_value(statement1)) # 2
print(count_value(statement2)) # 0

# This function takes one string argument and iterates through the
# string to find how many times the value `'t'` occurs throughout it.
# There's a `count` variable set to `0` that will increment each time
# the character is `'t'`, and returns it.