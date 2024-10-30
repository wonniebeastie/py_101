# Given the following similar sets of code, what will each code snippet 
# print? Why? What concepts are demonstrated by these code snippets?

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


# B
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


# C
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

# CODE A prints:
# ```
# one is: ['one']
# two is: ['two']
# three is: ['three']
# ```
# When the arguments are passed to the function when the function is
# called, the parameter `one` get assigned the value `"[one]"`, `two`
# with `["two"]` and so on. 
#
# They are now variables local to the function `mess_with_vars`.
#
# Inside the function, the local variables `one`, `two`, and
# `three` are reassigned different values. This does not affect the 
# global `one`, `two`, and `three` as it can be seen in the output
# produced by lines 16-18.


# CODE B prints:
# ```
# one is: ['one']
# two is: ['two']
# three is: ['three']
# ```
# Something similar to code A happens here. The local variables are 
# initialized with the values passed to the function. Then, inside the
# body, the local variables are reassigned new values.
#
# As lines 33-35 demonstrates, the global `one`, `two`, and `three` has
# not been modified. The `one`, `two`, and `three` inside the function
# are entirely different variables from the global ones, they just 
# share the same names.

# The concept demonstrated by the codes A & B are examples of variables
# scoping rules in Python & how local variables are initialized and re-
# assigned.

# (Note: Variable shadowing is not happening here because it doesn't
# show how the local variables are casting a "shadow" over the global
# ones, making them inaccessible from inside the function.
# It's also not a demonstration of mutability as the global variables
# were not changed by the operations inside the function body at this
# point in the code.)

# CODE C prints:
# ```
# one is: ['two']
# two is: ['three']
# three is: ['one']
# ```
# Now this is an example of how mutability of the objects passed to the
# function works in the pass-by-object-reference method used by Python.
# 
# The local variables are again initialized with the values from the
# global variables. But this time, we're mutating the references passed
# to the function by reassignment of the elements at index `0`. 
# 
# So lines 50-52 shows this is the case by printing the modified lists
# in the global scope. 



# SOLUTION
# In all three scenarios, the variables one, two, and three inside the
# `mess_with_vars` function are local to the function. They are not
# the same as the variables one, two, and three defined outside the
# function. 

# This is known as variable shadowing, where the local variables 
# inside the function overshadow the variables outside the function
# with the same names.


# NOTES
# My understanding of variable shadowing needed an adjustment. I had
# thought that it was when the local variable with the same name as
# a variable in the outer scope prevented the one in the outer scope
# from being accessed, but it turns out it's just when variables In
# an inner scope are declared with the same name as the variables in 
# the outer scope.