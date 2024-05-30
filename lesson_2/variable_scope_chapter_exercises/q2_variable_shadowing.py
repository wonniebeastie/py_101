# What will the following code print and why? Don't run it until you 
# have tried to answer.

num = 5

def my_func():
    num = 10

my_func()  # Returns None but does not print without print().

print(num)  # 5

# It will print `5` because any time there is an assignment operator 
# within a function, Python will treat it as a local variable that 
# creates its own scope. 
# So the `num` at the end only has access to the global variable `num`.
# This is an example of variable shadowing. 