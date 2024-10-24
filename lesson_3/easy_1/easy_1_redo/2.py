str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

# PROBLEM
# How can you determine whether a given string ends with an exclamation 
# mark (`!`)? Write some code that prints `True` or `False` depending on 
# whether the string ends with an exclamation mark.

# INPUTS & OUTPUTS
# I: a string
# O: True or False

# EXAMPLE(S)
# See code examples

# RULES (EXPLICIT/IMPLICIT)
# - the end of the string must be checked 
# - if it ends with `!`, it must return `True`
# - else, it must return `False`

# QUESTIONS / BRAINSTORM
# - 
# - 

# GOAL
# 

# DS
# 

# STEPS
# define function `ends_with_exc` (takes one string argument)
#     if the last character in the string is equal to `'!'`, return True
#     else return False

def ends_with_exc(text):
	if text[-1] == '!':
		return True
	else:
		return False

print(ends_with_exc(str1)) # True
print(ends_with_exc(str2)) # False

# This function uses the index position `-1` to find the last character
# in the string and returns `True` if it is equal to `'!'` and returns
# `False` if it does not. 