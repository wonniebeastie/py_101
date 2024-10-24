# PROBLEM
# Print a new version of the sentence given by advice that ends just 
# before the word house. Don't worry about spaces or punctuation: 
# remove everything starting from the beginning of house to the end 
# of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

# I & O
# I: given string
# O: the given string but everything from `'house'` onwards removed.

# BRAINSTORM
# - using the find or rfind method first and using that as the index
# - using slicing
# - replace method? with empty string?

# STEPS
# Find the index of where the string `'house'` starts from,
# store it in variable `index`
# Extract the string from the beginning to `index`

index = advice.find('house')

partial_advice = advice.replace(advice[39:], '')
print(repr(partial_advice)) # 'Few things in life are as important as ' 
# This one uses the `replace` method to replace the rest of the string 
# starting at index 39 to the end with an empty string

partial_advice = advice[:39] 
print(repr(partial_advice))  # 'Few things in life are as important as '
# This one uses slicing augmentation to extract from the beinning of the
# string to the end of the string, and assigns that extracted part 
# to a variable called `partial_advice`

# SOLUTION
print(advice.split("house")[0])

# When you use the `split` method with `"house"` as the argument, it 
# looks like this:
print(advice.split("house"))
# ['Few things in life are as important as ', ' training your pet dinosaur.']
# Then printing the string at index `0` prints what we want.