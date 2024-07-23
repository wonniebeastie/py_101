# What is the output of this code? 
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) 

# print(answer) #42

# MY SOLUTION
# I think it will be `34` because passing `42` that is referenced by 
# `answer` as an argument to the `mess_with_it()` function does not
# affect the original object.

# You're merely passing the reference to where the object `42` is located 
# when you pass `answer` as an argument into the function.

# Whether the original object is changed or not within the function 
# depends on the object's mutability.

# In this case, `42` is an integer, and since integers are immutable,
# they cannot be changed.


# SOLUTION
# Correct.
# 34