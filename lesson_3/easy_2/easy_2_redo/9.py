# We have most of the Munster family in our ages dictionary:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# Add entries for Marilyn and Spot to the dictionary:
additional_ages = {'Marilyn': 22, 'Spot': 237}


# One by one, the default way using `[]` operator:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages['Marilyn'] = 22
ages['Spot'] = 237
print(ages)
# {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10, 'Marilyn': 22, 'Spot': 237}


# Using the `update()` dictionary method.
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)
# {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10, 'Marilyn': 22, 'Spot': 237}



# Using the `setdefault()` dictionary method.
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.setdefault('Marilyn', 22)
ages.setdefault('Spot', 237)
print(ages)
# {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10, 'Marilyn': 22, 'Spot': 237}
# This method returns the value of the item with the specified key.
# However, if the key doesn't exist, it inserts the sepcified key & value.