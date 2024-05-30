# What will the following code print and why? Don't run it until you have 
# tried to answer.

num = 5

def my_func():
    print(num)

my_func() 

# It will print `5` because the variable `num` has global scope, so it can be 
# accessed from within functions. 

# SOLUTION: 
# This prints 5. The variable num initialized to 5 on line 1 is accessible 
# within the scope of the my_func function. When that function is invoked, 5 
# is printed.

