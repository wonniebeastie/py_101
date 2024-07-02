# Check each string separately for "Dino"

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def find_string(string):
    return 'Dino' in string 

print(find_string(str1))
print(find_string(str2))