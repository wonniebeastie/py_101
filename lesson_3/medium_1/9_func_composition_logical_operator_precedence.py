def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?
bar(foo())

# MY SOLUTION
# I think it will result in an error because no arguments were provided.

# SOLUTION
# Wrong. You can call a function without an argument if it already has
# a default parameter set. 
# This evaluates to "no" because `and` has higher operator precedence 
# than `or`.