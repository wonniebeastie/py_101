# In Python, every object has a unique identifier that can be accessed
# using the `id()` function. This function returns the identity of an 
# object, which is guaranteed to be unique for the object's lifetime. 
# For certain basic immutable data types like short strings or 
# integers, Python might reuse the memory address for objects with the 
# same value. This is known as "interning".

# Given the following code, predict the output:
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# MY SOLUTION
# "True" because of object interning.

# This may be wrong, but:

# Since `id(a) == id(b)` is `True`, Python simply uses the memory 
# address of id(b) to do the comparison `id(b) == id(c)`.

# If it evaluated to `False`, then the second comparison would NOT made
# at all because of short circuiting. 


# SOLUTION
# Correct, it outputs `True`.
# `a` and `c` reference the same object in memory, so their `ids` are 
# the same. 
# `b` will have the same `id` as `a` & `c` due to interning.