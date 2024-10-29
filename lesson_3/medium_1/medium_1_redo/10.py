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
# I predict that the output will be `True`.

# Line 9 initializes the variable `a` with the value `42`.
# Line 10 initializes the variable `b` also with `42`. Because integers
# from `-5` to `256` are automatically interned, this means that `b`
# refers to the same object in memory.
# Line 11 initializes the variable `c` with the same reference to the
# object that `a` points to. 

# All in all, this means that all three variables point to the same
# object in memory.