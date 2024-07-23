# What will the following two lines of code output?

# Don't look at the solution before you answer.

#A
print(0.3 + 0.6) # MY SOLUTION: 0.9

# B
print(0.3 + 0.6 == 0.9) # MY SOLUTION: False  


# SOLUTION:
# A is INCORRECT: It outputs 0.8999999999999999
# B is Correct.

# Python uses floating point numbers for ALL numeric operations.
# Most floating point representations used on computers lack a certain 
# amount of precision, and that can yield unexpected results like these.

# One way around the problem is to use the `math.isclose` function:

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))