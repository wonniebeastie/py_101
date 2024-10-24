# PROBLEM
# Determine whether the name Dino appears in the strings below -- check 
# each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

# I & O
# I: string
# O: True or False

# BRAINSTORM
# - rfind method
# - find method

print('Dino' in str1) # False
print('Dino' in str2) # True


def check_dino(txt):
    return 'Dino' in txt

print(check_dino(str1)) # False
print(check_dino(str2)) # True


def check_dino_2(txt):
    if txt.count('Dino') > 0:
        return True
    else:
        return False

print(check_dino_2(str1)) # False
print(check_dino_2(str2)) # True


def check_dino_3(txt):
    if txt.find('Dino') == -1:
        return False
    else:
        return True

print(check_dino_3(str1)) # False
print(check_dino_3(str2)) # True