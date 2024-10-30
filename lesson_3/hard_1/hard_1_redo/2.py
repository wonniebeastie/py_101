# What does the last line in the following code output?
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# Try to answer without running the code or looking at the solution.

# MY SOLUTION
# This will output:
# ``` 
# [1, 2]
# {'first': [1]}
# ```

# Line 3 assigns the value paired with the key `'first'` in the
# dictionary `dictionary`, which is `[1]` to the variable `num_list`.
# Then on line 4, the mutating list method, `append()` is called on
# `my_list`, appending the element `2` to the end of the list assigned
# to `my_list`.

# `my_list` is a new object, separate from `dictionary`.
# This is why the first output on line 6 is `[1, 2]`.

# The second output on line 7 shows that `dictionary` is as it was
# when it was originally initialized. 

# This is because `dictionary` and `num_list` are separate objects.

# AFTER RUNNING THE CODE
dictionary = {'first': [1]}

print(id(dictionary))          # 4342255808 (dictionary object)
print(id(dictionary['first'])) # 4342256832 (list object), LINE 4

num_list = dictionary['first']

print(num_list)     # [1]
print(id(num_list)) # 4342256832 (same list object as LINE 4)

num_list.append(2) # Mutate same list object as LINE 4

print(num_list)   # [1, 2]
print(dictionary) # {'first': [1, 2]}

# I did not read the question carefully enough again - it asks what
# THE LAST LINE outputs, not what the code outputs. So should have
# just put the output of the last line!

# It looks like I was wrong. 

# It actually outputs:
# ```
# [1, 2]
# {'first': [1, 2]}
# ```

# My next guess is that the value of `'first'` was mutated because It
# is the reference to the value (a mutable value in this case) is what
# is assigned to the variable `num_list`. `num_list` is an alias for
# the value `[1]` of the key `'first'` in `dictionary`.

# So using a mutating method has affected the original list.
