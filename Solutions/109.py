"""
Problem:

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should
be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def swap_bits(num: int) -> int:
    # (left shift digits at odd position) BITWISE-OR (right shift digits at even
    # position)
    # NOTE: If the value of filter mask is placed in the expression, it reduces to one
    # liner
    filter_mask = 85
    return ((num & filter_mask) << 1) | ((num & (filter_mask << 1)) >> 1)


if __name__ == "__main__":
    print("Swapped:", bin(swap_bits(0)))
    print("Swapped:", bin(swap_bits(255)))
    print("Swapped:", bin(swap_bits(210)))
    print("Swapped:", bin(swap_bits(170)))
    print("Swapped:", bin(swap_bits(226)))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
