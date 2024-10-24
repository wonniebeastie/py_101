# Given the following similar sets of code, what will each code 
# snippet print?

# A
def mess_with_vars(one, two, three):
    one = two  
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# MY SOLUTION
# Assignment (`=`) within a function is happening, which means local 
# variables are created.
# Now the LOCAL variable `one` refers to the same address as the 
# object that the global `two` is referencing (["two"]), and so on,
# but only from WITHIN the function. 

# So I think these will output:
# one is: ["one"]
# two is: ["two"]
# three is: ["three"]

# Because the `one`, `two`, and `three` variables that can be accessed 
# from outside the function are the global ones.


# SOLUTION
# Answer is correct but my understanding of it was incorrect. 

# The initialization of the parameters as local variables does NOT 
# happen on lines 6-8.

# It happens on line 5/when the function is called.

# The local variables `one`, `two`, and `three` are assigned the values 
# that are passed into the function as arguments.

# Meaning that although the addresses in which the new local variables
# themselves are stored is different from the global variables, the 
# reference they hold to where the objects they reference are stored are
# still the same as the originals. 

# So at this point, the names and values of the local & global
# variables look identical on the surface.

# But inside the function, on lines 6-8, those local variables are 
# reassigned with the values from the global variables (which can be
# accessed from within the function because they're global), but 
# mismatched to the original names.
# So now they refer to different objects than the originals.

# So when the print functions are called on lines 16-18, they output
# the values assigned to the global `one`, `two`, and `three`.


# B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# MY SOLUTION
# In this one, I think that again, since assignment is happening, the 
# `one`, `two`, `three` variables inside the function are local ones 
# as well.

# So I think these will output:
# one is: ["one"]
# two is: ["two"]
# three is: ["three"]


# SOLUTION
# Correct.
# The same goes as A except that the values being re-assigned to the 
# local variables are ones indicated from within the function, not 
# taken from the global variables.
# Which do not reflect in the outer/global variables.


# C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# MY SOLUTION
# I think this will output:
# one is: "two"
# two is: "three"
# three is: "one"

# I believe the `one`, `two`, and `three` global variables can be 
# modified from within the function without the `global` keyword 
# because the original objects are mutable objects and you're 
# reassigning an element at the index 0 for each one, not assigning 
# whole new variables.


# SOLUTION
# Answer correct but my understanding needed adjustment.

# Although it is correct that the changes were reflected in the
# original variables because lists in Python are mutable objects,
# it's not the global `one`, `two`, and `three` that were being 
# reassigned, they're still the local variables that are being 
# reassigned.

# The difference is that we are mutating the original objects,
# (so at the same memory address as the OGs) not giving entirely new
# values to these new local variables (which would make them point to
# an entirely different memory address) via reassignment.
