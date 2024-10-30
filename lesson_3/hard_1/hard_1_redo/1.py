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

# Try to answer without running the code or looking at the solution.

# MY SOLUTION
# They won't return the same results.

# Line 13 will return:
# ```
# {'prop1': 'hi there'}
# ```

# Line 14 will raise an exception.

# SOLUTION
# First part is right, second part not right. 
# Line 14 (`print(second())`) will not raise an exception - instead,
# it will return `None`. Python expects something to be there after
# a `return` statement, but since the indented block after it is
# unreachable, it will just return `None`, the default return value
# for functions.
