# What will the following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()  # This creates a copy of `my_list1` and assigns it to `my_list2`.
my_list2[0]['first'] = 42  # This changes "value1" to 42.
print(my_list1)

# Try to answer without running the code.

# MY SOLUTION
# I think line 5 will output `[{"first": 42}, {"second": "value2"}, 3, 
# 4, 5]` because while `my_list2` refers to the reference to the 
# location in which a COPY of `my_list1` is stored, it seems that 
# dictionaries are treated the same as a nested object. 
# Meaning that the dictionary at index 0 of `my_list2` is a reference 
# to the same place that that dictionary in `my_list1` points to;
# So changes made to either one will reflect on the other.

# SOLUTION
# Correct.
# The `.copy()` list method creates shallow copies.
# Shallow copies only makes duplicates of the outermost values in an
# object. 
# We end up with two different lists but only one occurence each of 
# `{ first: 42 }` and `{ second: 'value2' }`.
# So both my_list1[0] and my_list2[0] point to the same dictionary in 
# memory.