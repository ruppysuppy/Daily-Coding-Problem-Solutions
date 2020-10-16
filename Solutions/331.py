"""
Problem:

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In
addition, you have an operation called flip, which changes a single x to y or vice
versa.

Determine how many times you would need to apply this operation to ensure that all x's
come before all y's. In the preceding example, it suffices to flip the second and sixth
characters, so you should return 2.
"""

from sys import maxsize


def get_minimum_flips(string: str) -> int:
    length = len(string)
    # lookup table for dp
    flips_from_left = [0 for i in range(length)]
    flips_from_right = [0 for i in range(length)]
    # updating flips from left
    flips = 0
    for i in range(length):
        if string[i] == "y":
            flips = flips + 1
        flips_from_left[i] = flips
    # updating flips from right
    flips = 0
    for i in range(length - 1, -1, -1):
        if string[i] == "x":
            flips = flips + 1
        flips_from_right[i] = flips
    # generating the minimum number of flips (using minimum flips is the minimum flips
    # on the left + minimum flips on the right)
    minFlips = maxsize
    for i in range(1, length):
        minFlips = min(minFlips, flips_from_left[i - 1] + flips_from_right[i])
    return minFlips


if __name__ == "__main__":
    print(get_minimum_flips("xyxxxyxyy"))
    print(get_minimum_flips("xyxxxyxxxxxxxxxxxyyyyyyyyyyyyyyyx"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
