# Write code that prints True or False depending on whether the string
# ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

# MY SOLUTION
def find_exclamation(string):
    result = '!' in string
    return result

print(find_exclamation(str1))  # True
print(find_exclamation(str2))  # False

# SOLUTION
# I used the `in` operator to solve this but `str.endswith()` method
# can also be used:
# print(str1.endswith("!"))  # True
# print(str2.endswith("!"))  # False