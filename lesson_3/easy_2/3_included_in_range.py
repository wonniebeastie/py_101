# Check if `42` lies between `10` and `100`, inclusive
# Same for values `100` & `101`

number_range = tuple(range(10, 101))

print(42 in number_range)   # True
print(100 in number_range)  # True
print(101 in number_range)  # False