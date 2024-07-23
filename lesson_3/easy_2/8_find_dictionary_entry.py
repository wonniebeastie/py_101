# Does this dictionary contain an entry for 'Spot'?

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# MY SOLUTION
# `print(ages['Spot'])` results in a KeyError, as that key does not 
# exist within the `ages` dictionary.

print('Spot' in ages) # False