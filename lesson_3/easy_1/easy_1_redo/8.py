# PROBLEM
# In the previous problem, our first answer added `'Dino'` to the list like this:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")

# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)
# The extend list method allows you to add the items of any iterable to
# the end of a list, meaning you can use it to add multiple values to
# the `flintstones` list.

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
print(flintstones + ['Dino', 'Hoppy'])
# ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino']
# Concatenating using the `+` operator also works to concatenate another
# list to the `flintstones` list.