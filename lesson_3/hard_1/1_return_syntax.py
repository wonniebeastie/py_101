# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# MY SOLUTION
# I think they will return the same result because you don't need a 
# colon for returns unlike something like `if` statements.

# SOLUTION 
# Incorrect.
# They DO NOT return the same thing. 

# `first()` returns the expected value of `{ prop1: "hi there" }`,
# but `second()` returns `None` without throwing any errors.

# If there's nothing after a `return` statement, the function will 
# return `None` in Python.

# The indented block after the `return` statement in `second()` is 
# unreachable and doesn't affect the return value. 