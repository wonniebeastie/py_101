# PROBLEM
# Programmatically determine whether 42 lies between 10 and 100, 
# inclusive. Do the same for the values 100 and 101.

print(42 in range(10, 101))  # True
print(100 in range(10, 101)) # True
print(101 in range(10, 101)) # False

# We used the `in` membership operator with a range object to solve this.
# Since the stopping value for ranges is exclusive, 101 was what was used
# used to accommodate the directions to make `100` inclusive.