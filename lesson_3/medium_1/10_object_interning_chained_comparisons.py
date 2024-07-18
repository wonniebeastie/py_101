# Predict the output.
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# "True" because of object interning.

# This may be wrong, but:

# Since `id(a) == id(b)` is `True`, Python simply uses the memory 
# address of id(b) to do the comparison `id(b) == id(c)`.

# If it evaluated to `False`, then the second comparison is NOT made
# at all because of short circuiting. 