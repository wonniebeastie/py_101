# Rewrite so there's only one `return` statement & 
# does not explicitly use `True` or `False`.

# Two different solutions.

# My interpretation:
# 'blue' and 'green' are truthy values 
# others are falsy.

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

# 1
def is_color_valid(color):
    if color == 'green' or color == 'blue':
        result = bool(color)
    else:
        result = bool('')
    return result


#2
def is_color_valid_2(color):
    color = 'green' in color or 'blue' in color
    return color

print(is_color_valid('green'))
print(is_color_valid_2('b'))