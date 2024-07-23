# Consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# What will the following function invocation return?
bar(foo())

# MY SOLUTION
# I think it will result in an error because no arguments were provided.

# SOLUTION
# Incorrect.
# It will return "no".
# You can call a function without an argument if it already has
# a default parameter set. 

# 1: `foo()` is called, which returns "yes".

# 2: So `bar()` is called with "yes" as the argument -> bar("yes")

# 3: For this part:
# param == "no" and foo() or "no"
# `and` has higher operator precedence than `or`. 
# So `param == "no" and foo()` will be evaluated first.
# Since `param` does NOT equal "no" at this time, `param == "no"` 
# is False.

# 4: Since `and` needs both sides to be True, the operation short-
# circuits and the rest (`foo()`) is not executed.

# 5: Now it looks like: `False or "no"`.
# Since `or` only needs one of the two to be True, Python evaluates 
# and returns the right side of the `or`, which "no".

# This is because the value returned by `foo` will always be "yes", and
# `"yes" == "no"` will be False.