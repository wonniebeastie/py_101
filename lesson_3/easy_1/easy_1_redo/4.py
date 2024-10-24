# PROBLEM
# Using the following string, print a string that contains the same 
# value, but using all lowercase letters except for the first 
# character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

# INPUTS & OUTPUTS
# I: a string
# O: the input string but first letter uppercase & everything else lower
#    lowercase 

# EXAMPLE(S)
# I: "the Munsters are CREEPY and Spooky."
# O:'The munsters are creepy and spooky.'

def capitalize(txt):
	print(txt.capitalize())

capitalize(munsters_description) # The munsters are creepy and spooky.

# This function takes one string as an argument and calls the `capitalize`
# method on the string and prints it. 