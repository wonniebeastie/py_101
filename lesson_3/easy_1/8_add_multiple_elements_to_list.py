# Relates to the previous problem.

# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

# MY SOLUTION
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
flintstones.extend(["Dino", "Hoppy"]) # This mutates the list.

print(flintstones)
# ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino', 'Hoppy']

# SOLUTION
# Correct.