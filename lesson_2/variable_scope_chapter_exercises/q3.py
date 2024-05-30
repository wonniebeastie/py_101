# What will the following code print and why? Don't run it until you 
# have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# It will print `10`, as using the `global` keyword indicates to Python 
# that the `num` variable you're referring to within the function 
# `my_func` is the global variable `num`.
# So this will modify the global `num`, not create a new local variable
# also called `num`. 

# SOLUTION: 
# This prints 10. The variable num is initialized to 5 on line 1. On 
# line 4 we use global keyword inside the function to reference the 
# global variable num initialized on line 1. For that reason, on line 
# 5 we are reassigning global variable num to 10 and on line 8 printing
# that value.