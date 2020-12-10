"""
Problem:

Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""


def divide(dividend: int, divisor: int) -> int:
    quotient = 0
    while dividend > 0:
        dividend -= divisor
        if dividend >= 0:
            quotient += 1
    return quotient


if __name__ == "__main__":
    print(divide(1, 0))
    print(divide(1, 1))
    print(divide(0, 1))
    print(divide(12, 3))
    print(divide(13, 3))
    print(divide(25, 5))
    print(divide(25, 7))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
