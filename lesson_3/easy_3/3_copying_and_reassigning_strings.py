# What will the following code output?
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# Try to answer without running the code.

# MY SOLUTION:
# I think it will output "hello there" because:
# One line 2, you're assigning the reference to where the string "hello 
# there" is located in memory to `str1`;
# On line 3, you're assigning that same reference to `str2`;
# On line 4, you're reassigning `str2` with the reference to where 
# the new string "goodbye!" is stored.
# But the original reference to "hello there" that `str1` holds remains
# unchanged. 

# SOLUTION:
# Correct. 
# The output is `hello there`. In Python, strings are immutable so there 
# is no way to change the value of `str1` unless we reassign it. When we 
# do `str2 = str1` we are pointing the variable `str2` to the same 
# memory location as the original string. Once we reassign `str2` 
# again, on line 3, it just changes what `str2` variable points to, and
# doesn't affect variable `str1`.