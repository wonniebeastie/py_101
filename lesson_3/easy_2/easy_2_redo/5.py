# PROBLEM
# How would you verify whether the data structures assigned to the 
# variables `numbers` and `table` are of type `list`?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list) # True
print(type(table) is list) # False

# We can use the `type()` built-in function to check what data type
# an object is. You can also use with the `is` identity operator to
# directly check if the object is a `list`.

print(isinstance(numbers, list))
print(isinstance(table, list))

# We can also use the `isinstance()` built-in function, which takes two
# parameteres, the first one the object, then the second one the type or
# class that you want the object to be checked for.