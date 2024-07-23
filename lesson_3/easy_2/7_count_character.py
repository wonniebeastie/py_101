# Write on one-line: count the # of `t` in each string:
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

# MY SOLUTION
print(statement1.count('t'))  # 2
print(statement2.count('t'))  # 0

# SOLUTION
# Correct. 
# The `.count()` string method returns the number of non-overlapping 
# occuerences of a substring.