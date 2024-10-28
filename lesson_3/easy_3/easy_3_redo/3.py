# PROBLEM
# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"

print(str1)

# This will output:
# ```
# hello there
# ```

# The variable `str2` is created on line 5 with the reference to the
# string assigned to `str1`. Both `str1` & `str2` refer to the same
# object in memory at this point.

# Then `str2` is reassigned with the string `"goodbye!"` on line 6.

# This reassignment does not affect `str1` as demonstrated on line 8 -
# you're simply making `str2` to refer to a different object in memory.

# SOLUTION
# Same as mine but the reason is not because of immutability. 
# Reassigning `str2` simply breaks the connection between `str1` &
# `str2`. So they both point to different objects. 