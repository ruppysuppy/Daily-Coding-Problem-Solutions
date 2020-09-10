"""
Problem:

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. 
You can assume b can only be 1 or 0.
"""

# FUNCTION TO PERFORM THE OPERATION
def switch_on_int(x, y, b):
    # returning the necessary number based on the value of b, abs(-1)=1, so if b=0, y is returned, else x is returned
    return (x * b) + (y * abs(b - 1))


# DRIVER CODE
print(switch_on_int(6, 8, 1))
print(switch_on_int(6, 8, 0))
