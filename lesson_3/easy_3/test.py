def is_color_valid(color):
    return color in ["blue", "green"]
    
print(is_color_valid('pink'))   # False
print(is_color_valid('blue'))   # True
print(is_color_valid('green'))  # True