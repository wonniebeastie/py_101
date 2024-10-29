# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8  

new_answer = mess_with_it(answer) # 50

print(answer - 8) # 34

# MY SOLUTION
# This code will output:
# ```
# 34
# ```

# This is because despite `answer` being passed as an argument, and
# an operation performed with it, because integers are immutable,
# the original cannot be changed/mutated. 

# Line 10 prints the result of `8` subtracted from `answer`, which 
# still has the value `42` assigned to it. 