# Check each string separately for "Dino"
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# MY SOLUTION
def find_string(string):
    return 'Dino' in string 

print(find_string(str1))  # False
print(find_string(str2))  # True

# SOLUTION
# 'Dino' in str1  # False
# 'Dino' in str2  # True
# Correct, although I took the extra step to do it within a function.