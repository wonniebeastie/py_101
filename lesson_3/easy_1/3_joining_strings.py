famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and "
# prepended to the front of the string.

starting_string = "Four score and "

# MY SOLUTIONS

# Method 1
new_string = starting_string + famous_words
print(new_string)  # Four score and seven years ago...


# Method 2
new_string = f'{starting_string}{famous_words}'
print(new_string)  # Four score and seven years ago...