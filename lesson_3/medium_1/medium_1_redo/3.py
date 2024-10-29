# PROBLEM
# Alyssa was asked to write an implementation of a rolling buffer. You 
# can add and remove elements from a rolling buffer. However, once the 
# buffer becomes full, any new elements will displace the oldest 
# elements in the buffer.

# She wrote two implementations of the code for adding elements to the 
# buffer:

# def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
#     buffer.append(new_element)
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
#     buffer = buffer + [new_element]
#     if len(buffer) > max_buffer_size:
#         buffer.pop(0)
#     return buffer

# What is the key difference between these implementations?

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    print(f"before apppend: {buffer}") # [1, 2, 3, 4, 5]
    buffer.append(new_element)
    print(f"after apppend: {buffer}")  # [1, 2, 3, 4, 5, 8]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    print(f"before apppend: {buffer}") # [1, 2, 3, 4, 5]
    buffer = buffer + [new_element]
    print(f"after apppend: {buffer}")  # [1, 2, 3, 4, 5, 8]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer 

butter = [1, 2, 3, 4, 5]

print(add_to_rolling_buffer1(butter, 3, 8)) # [2, 3, 4, 5, 8]
print(add_to_rolling_buffer2(butter, 3, 8)) # [2, 3, 4, 5, 8]


# MY SOLUTION
# The key difference between these two implementations is that 
# `add_to_rolling_buffer1` mutates the reference to the list passed as
# the argument to achieve the desired effect; and the second one,
# `add_to_rolling_buffer2` does it by concatenating the list passed as
# the argument with `new_element`, as a list. Then reassigning `buffer`
# with the resulting list, which is a whole new object. 


# SOLUTION
# Yes, there is a difference. The first function 
# (`add_to_rolling_buffer1`) mutates the original list represented by
# `buffer`. The second function (`add_to_rolling_buffer2`) does not
# mutate the original list, but instead creates a new list and assigns
# it to `buffer`, whose value ultimately gets returned by the function.