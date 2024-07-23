# Print a new version of the sentence given by advice that ends just 
# before the word `house`. Don't worry about spaces or punctuation: 
# remove everything starting from the beginning of house to the end of 
# the sentence.

# MY SOLUTION
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice[0:38]) # Few things in life are as important as
# I used the slicing syntax to achieve this:
# the first number `0` is the index at which I want to start the 
# extraction & the second number `38` is one index number past the
# index # of where I want the extraction to end.

# SOLUTION 
# print(advice.split("house")[0])
# The `.split()` method splits a string into a list.
# In this solution, we are accessing the very first value in the list
# that was created using `house` as the break-off point at which to 
# break up the string into separate items on the list.