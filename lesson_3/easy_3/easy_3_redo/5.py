def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

# PROBLEM
# The following function unnecessarily uses two `return` statements to
# return boolean values. Can you rewrite this function so it only has
# one return statement and does not explicitly use either `True` or
# `False`?

# Try to come up with two different solutions.


# My Solution 1
def is_color_valid(color):
    return color == "blue" or color == "green"

print(is_color_valid("blue"))  # True 
print(is_color_valid("green")) # True
print(is_color_valid("pink"))  # False


# My Solution 2
def is_color_valid(color):
    valid_colors = ["blue", "green"]
    return color in valid_colors

print(is_color_valid("blue"))  # True 
print(is_color_valid("green")) # True
print(is_color_valid("pink"))  # False


# SOLUTION
# We can simplify this function like this:
def is_color_valid(color):
    return color == "blue" or color == "green"

# In functions that return a boolean value, you often don't need
# separate return statements for the True and False cases. Instead,
# you can return the value of a conditional expression directly.

# You can also use the `in` operator to check if the color exists in a
# list:

def is_color_valid(color):
    return color in ["blue", "green"]