"""
Problem:

Given an unsigned 8-bit integer, swap its even and odd bits. 
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
Bonus: Can you do this in one line?

Example:

Input = 10101010 
Output = 01010101

Input = 11100010 
Output = 11010001
"""

# FUNCTION TO PERFORM THE OPERATION
def swap_bits(num):
    # displaying the number in binary
    print("Num:", bin(num))

    # 85 is the filter '01010101'
    filter_mask = 85
    # (using the mask to get the digits at odd position and left shifting) BITWISE-OR (using the mask to get the digits at even position and right shifting)
    return ((num & filter_mask) << 1) | ((num & (filter_mask << 1)) >> 1)


# DRIVER CODE
print("Swapped:", bin(swap_bits(0)))
print("Swapped:", bin(swap_bits(255)))
print("Swapped:", bin(swap_bits(210)))
print("Swapped:", bin(swap_bits(170)))
print("Swapped:", bin(swap_bits(226)))
