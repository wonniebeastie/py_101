# PROBLEM
# Let's do some "ASCII Art": a stone-age form of nerd artwork from back
# in the days before computers had video screens.

# For this practice problem, write a program that outputs `The 
# Flintstones Rock!`` 10 times, with each line prefixed by one more
# hyphen than the line above it. The output should start out like this:

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#     ...

# MY SOLUTION
def prefix(txt):
    for each in range(1, 11):
        print('-' * each + txt)

prefix('The Flintstones Rock!')

# My solution uses a `for` loop with a `range` object to print the
# given text 10 times, each line prefixed with one more hyphen than the
# last using multiplication with each number in the range then 
# concatenating that with the given text.


# SOLUTION
for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')

# LS's solution also uses a `for` loop with a `range` object like mine
# - the only difference is the use of an f-string.
