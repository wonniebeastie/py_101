famous_words = "seven years ago..."

# Two different ways to create a new string with "Four score and "
# prepended to the front of the string.

starting_string = "Four score and "


# Method 1
new_string = starting_string + famous_words
print(new_string)


# Method 2
new_string = f'{starting_string}{famous_words}'
print(new_string)