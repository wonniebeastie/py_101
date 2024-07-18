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

# Will this code ransack the Munster family's data?
mess_with_demographics(munsters)

# MY SOLUTION
# I think it will because `munsters` is a dictionary, which is a 
# mutable object, and the `.items()` method is able to mutate 
# dictionaries.