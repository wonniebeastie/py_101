# One day, Spot was playing with the Munster family's home computer, 
# and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. 
# Did the family's data get ransacked? Why or why not?



# MY SOLUTION
# I think it will be ransacked because `munsters` is a dictionary, which is a 
# mutable object, and the `.items()` method is able to mutate 
# dictionaries.



# SOLUTION

print(munsters)
# {'Herman': {'age': 74, 'gender': 'other'}, 'Lily': {'age': 72, 
# 'gender': 'other'}, 'Grandpa': {'age': 444, 'gender': 'other'}, 
# 'Eddie': {'age': 52, 'gender': 'other'}, 'Marilyn': {'age': 65, 
# 'gender': 'other'}}

# Correct.

# Dictionaries are mutable.

# When passed to a function, a reference to the memory location of that
# dictionary is passed, not a copy (another reference to a new location).

# Spot's `demo_dict` starts off pointing to the `munsters` object.

# This means that changes made within the function will directly affect
# the `munsters` dictionary.

# Key aspect: the nested dictionaries (individual family member's data) 
# are the ones being mutated.
# Each one is accessed and modified.

# Since these nested dictionaries are a part of the larger `munsters` 
# dictionary, changes are reflected in the original.

