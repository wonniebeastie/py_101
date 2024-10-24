# What do you expect to happen when the greeting variable is referenced 
# in the last line of the code below?

if False:
    greeting = "hello world"

print(greeting)

# MY SOLUTION
# I thought it would print "hello world" because `if` statements don't 
# create their own scopes in Python, but upon putting the code in the
# editor, the variable is greyed out.

# SOLUTION
# In Python, referencing an uninitialized variable will result in a 
# NameError.
# This is because the `if` block is NOT executed due to the `False` 
# condition, and hence, `greeting` the variable is never initialized.