# Write code that prints True or False depending on whether the string
# ends with an exclamation mark.

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def find_exclamation(string):
    result = '!' in string
    return result

print(find_exclamation(str1))
print(find_exclamation(str2))

# str.endswith() method can also be used.