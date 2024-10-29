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
        print(f'key: {key}')
        print(f'value: {value}')
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail.
# Did the family's data get ransacked? Why or why not?


# MY SOLUTION

print(munsters)
# {
# 'Herman': {'age': 74, 'gender': 'other'}, 
# 'Lily': {'age': 72, 'gender': 'other'}, 
# 'Grandpa': {'age': 444, 'gender': 'other'}, 
# 'Eddie': {'age': 52, 'gender': 'other'}, 
# 'Marilyn': {'age': 65, 'gender': 'other'},
# }

# The family's data is now ransacked because the function mutates the
# dictionary in question by updating some of the values. 

# Python uses the pass-by-object-reference method when passing
# arguments to functions. This means that dictionaries, being mutable,
# have the possibility of being mutated by operations performed on them
# inside of functions, as it's the references to objects that gets
# passed to the function.
