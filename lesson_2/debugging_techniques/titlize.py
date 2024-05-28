def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
        new_words.append(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))


# PROBLEM: Return a given string with the first letter of each word
# capitalized, except the words that are 2 characters long or less.

# INPUT: String with all lower case letters
# OUTPUT: String with all letters that are greater than 2 characters capitalized

# MENTAL MODEL: Given a string with lowercase letters, iterate through each
# word; If the word is more than two characters long, capitalize the first 
# letter, and if it is less than two characterse long, leave it as is.
# Return the new capitalized string.

# PSEUDOCODE:
# Given a string, 
# Iterate through each word
#     If word length is greater than 2 characters, 
#         Capitalize the first letter of the word then add it to new string.
#     Else, add it to new string as is. 
# Return new string. 

# PSEUDOCODE PRACTICE AFTER DEBUGGING ATTEMPT:
# 1) Create a function called `titlize`, that takes one argument.
#     a) Within the function, create a variable called `words` that will hold
#     the reference to the string with each word split into a list.
#     b) Create a variable called `new_words` and have it hold an empty list.
#     c) Iterate through each word in the `words` list -
#         i) If the length of the element, `word`, is greater than 2 characters,
#            reassign `word` with the first letter of the string capitalized,
#            then append that result to the `new_words` list;
#            Otherwise, just append the word as is to the `new_words` list.
#     d) Return the list joined as one string.
# 2) Create variable called `title` that holds the string `hello world of 
#    programming`.
# 3) Output the result of the `titlize` function with `title` as the argument.

