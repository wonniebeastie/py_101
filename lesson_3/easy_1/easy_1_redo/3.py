# PROBLEM
# Starting with the string:
famous_words = "seven years ago..."
# Show two different ways to create a new string with `"Four score and "` 
# prepended to the front of the string.

# INPUTS & OUTPUTS
# I: given string
# O: Four score and [given string]

# EXAMPLE(S)
# I: seven years ago...
# O: Four score and seven years ago...

# RULES (EXPLICIT/IMPLICIT)
# - 2 different ways
# - "Four score and " must be prepended to the front of given string
# - Be returned as a new string 

# QUESTIONS / BRAINSTORM
# - create a new string with the value `"Four score and "`
# - concatenate it to the existing string with `+` operator.
# - use the `print` function and a comma to concatenate the two strings.
# - use the `join` string method

# GOAL
# To prepend the string `"Four score and "` to the given string in 2 ways.

four_score = "Four score and "

print(four_score + famous_words) # Four score and seven years ago...
print(four_score, famous_words) # Four score and  seven years ago...
# Above does not work because it adds a whitespace before 
print(four_score, famous_words, sep='') # Four score and seven years ago...

list_of_words = [four_score, famous_words]
print(''.join(list_of_words)) # Four score and seven years ago...