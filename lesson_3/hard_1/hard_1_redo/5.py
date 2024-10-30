# What do you expect to happen when the greeting variable is referenced 
# in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# I expect this code to raise an exception because the `greeting` 
# variable is within the body of the `if` statement, which means that
# the code will not execute if the condition is not truthy.

# Since the value is falsy, it will not run the code, making it 
# unreachable. 


# Output: NameError: name 'greeting' is not defined


# SOLUTION
# In Python, referencing an uninitialized variable will result in a
# `NameError` being raised. This is because the `if` block is not
# executed due to the `False` condition, and hence, the `greeting` 
# variable is never initialized.