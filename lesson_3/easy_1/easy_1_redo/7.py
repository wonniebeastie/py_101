# PROBLEM
# How can we add the family pet, "Dino", to the following list?

# Using `+` operator to concatenate a list value
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
print(flintstones + ['Dino'])
# ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino']

# Using the append method
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')
print(flintstones)
# ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino']

# Using extend method
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(['Dino'])
print(flintstones)

# Using insert method with length of list as the position
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.insert(len(flintstones), "Dino")
print(flintstones)
# This method works because the length of `flinstones` is 6; And since
# lists have zero-based index, it starts from 0, meaning this list goes
# from 0 to 5. 