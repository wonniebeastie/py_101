my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42

print(my_list1)

# PROBLEM
# What will the following code output?
# Try to answer without running the code.


# MY SOLUTION

# This will print:
# ```
# [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# ```

# Line 2 creates a shallow copy of `my_list1` and assigns it to the
# variable `my_list2`. This means that the list assigned to `my_list2`
# is a new object, separate from the one assigned to `my_list1`.

# Then on line 3, we change the value paired with the key `"first"`
# at index `0` of `my_list2`.

# But this change does not affect the original list, as demonstrated
# on line 5. 