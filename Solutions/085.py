"""
Problem:

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only
mathematical or bit operations. You can assume b can only be 1 or 0.
"""


def switch_on_int(x: int, y: int, b: int) -> int:
    return (x * b) + (y * abs(b - 1))


if __name__ == "__main__":
    print(switch_on_int(6, 8, 1))
    print(switch_on_int(6, 8, 0))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
