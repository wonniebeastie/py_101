# Add "Dino" to the following list.

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# MY SOLUTION
# Lessons: 
# flintstones[6] = "Dino"
# Above results in an IndexError.
# Trying to assign "Dino" to an index that does not exist will do this.

# flintstones[6] == "Dino"
# Above results in another IndexError.
# You're trying to check to see if the value at index 6 in `flinstones`
# is equal to the value of "Dino".
# However, you are again, trying to access a value at an index that
# does not exist. 

flintstones = flintstones + ["Dino"]
print(flintstones) 
# ['Fred', 'Barney', 'Wilma', 'Betty', 'Bambam', 'Pebbles', 'Dino']

# Using the `+` operator on a mutable object is a non-mutating
# operation. 
# So doing that alone would not change the original `flinstones` list.
# But reassigning the variable `flintstones` with the result of that
# operation does work to change what `flinstones` points to.

# SOLUTION
# flintstones.append("Dino")
# This is a more succinct way to do it, as the `.append()` method 
# mutates `flinstones`.

