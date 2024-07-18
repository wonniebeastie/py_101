# A
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# B
def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# MY SOLUTION
# The difference between the two may be that "A" mutates the original
# `buffer` while "B" does not. 
# Instead, "B" performs a non-mutating addition of the new element,
# creating a new list, and reassigns `buffer` with the result and 
# returns it. 
# Doing this from within a function will not mutate the original.