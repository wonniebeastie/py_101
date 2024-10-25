# PROBLEM
# Determine whether the following dictionary of people and their age 
# contains an entry for `'Spot'`:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages) # False
# You can use the `in` membership operator to check if `'Spot'` exists
# as a value in the `ages` dictionary. This operator only checks for 
# keys, not values.

print(ages.get('Spot')) # None
# You can also use the `get()` dictionary method to fetch the value of 
# the specified key. It returns `None` because the key `'Spot'` cannot
# be found in the `ages` dictionary.
