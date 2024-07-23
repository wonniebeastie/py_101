# We have most of the Munster family in our ages dictionary:
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# Add entries for Marilyn and Spot to the dictionary:
additional_ages = {'Marilyn': 22, 'Spot': 237}

# MY SOLUTION
ages.update(additional_ages)

print(ages) 
# {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10, 'Marilyn': 22, 'Spot': 237}

# The `.update()` dictionary method inserts specified items to a
# dictionary. 