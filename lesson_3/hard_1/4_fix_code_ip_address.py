# Ben was tasked to write a simple Python function to determine whether 
# an input string is an IP address using 4 dot-separated numbers, e.g.,
# `10.4.5.11`.

# Alyssa supplied Ben with a function named `is_an_ip_number`. 
# It determines whether a string is a numeric string between `0` and `255` 
# as required for IP numbers and asked Ben to use it. 
# Here's the code that Ben wrote:

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break

#     return True

# Alyssa reviewed Ben's code and said, "It's a good start, but you 
# missed a few things. You're not returning a false condition, and 
# you're not handling the case when the input string has more or less
# than 4 components, e.g., `4.5.5` or `1.2.3.4.5`: both those values should
# be invalid."

# Help Ben fix his code.


# MY SOLUTION

# OBJECTIVE
# Return a False condition
# Make strings that are less than or greater than 4 invalid.

# HINT: Alyssa's `is_an_ip_number` function
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    # Make strings that have > or < 4 components invalid
    if len(dot_separated_words) != 4:
        return False
    
    # False condition
    for item in dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address("14.7.23.9"))        # True
print(is_dot_separated_ip_address("4.6."))             # False
print(is_dot_separated_ip_address("3.8.12.18.00"))     # False 
print(is_dot_separated_ip_address("14.5.7.pineapple")) # False


# SOLUTION
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# The problem with the second part was that Ben used a `break` 
# statement to break out of the `while` loop, which caused control to 
# fall through to the `return True` statement. 