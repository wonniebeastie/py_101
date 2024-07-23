# Turn below into this: => 'The munsters are creepy and spooky.'
munsters_description = "the Munsters are CREEPY and Spooky."

# MY SOLUTION
print(munsters_description.casefold().capitalize())

# SOLUTION
# print(munsters_description.capitalize())
# I did not need to method chain as the `capitalize()` method already
# returns the rest of the string in lowercase.

# Lesson: Read documentation better.