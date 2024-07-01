# How do you verify whether the variables reference a list type?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers)) # <class 'list'>
print(type(table)) # <class 'dict'>

print(isinstance(numbers, list)) # True
print(isinstance(table, list)) # False

# The `is` keyword with the `type()` function also works.