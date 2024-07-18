# Write a program that outputs "The Flintstones Rock!" 10 times;
# Each line prefixed bh one more hyphen than the line above it.

# Input: "The Flintstones Rock!"
# Output: 
# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#    ... (10x)

# PSEUDOCODE
# Assign "The Flintstones Rock!" to variable `line`

# Create function `add_hyphen(message)`
#     Add `-` to `message` - reassign `message` with result 
#     Return `message`

# Create function `display_message(string)`
#     Create loop 
#     Loop 10 times 
#         Call `add_hyphen(string)` - reassign `string` with the result
#         Print `string`

# Call `display_message()` on `line`

line = 'The Flintstones Rock!'

def add_hyphen(message):
    message = '-' + message
    return message

def display_message(string):
    for _ in range(10):
        string = add_hyphen(string)
        print(string)

display_message(line)


# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
# ----The Flintstones Rock!
# -----The Flintstones Rock!
# ------The Flintstones Rock!
# -------The Flintstones Rock!
# --------The Flintstones Rock!
# ---------The Flintstones Rock!
# ----------The Flintstones Rock!
