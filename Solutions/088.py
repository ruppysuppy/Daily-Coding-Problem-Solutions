"""
Problem:

Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
"""


def divide(dividend: int, divisor: int) -> int:
    # Handle error cases
    if divisor == 0:
        raise ZeroDivisionError("Division by zero")
    elif dividend < 0 or divisor < 0:
        raise ValueError("Both dividend and divisor must be non-negative integers")

    # Speed up trivial cases
    if dividend == divisor:
        return 1
    elif dividend < divisor:
        return 0

    # Initialize variables
    quotient = 0
    temp_divisor = divisor

    # Align the divisor with the highest bit of the dividend
    bit_position = dividend.bit_length() - divisor.bit_length()

    # Divide using bitwise operations
    while bit_position >= 0:
        if (temp_divisor << bit_position) <= dividend:
            quotient += 1 << bit_position
            dividend -= temp_divisor << bit_position
        bit_position -= 1

    return quotient


if __name__ == "__main__":
    try:
        print(divide(1, 0)),  # Divide by zero test case (should throw error)
    except ZeroDivisionError as e:
        print(e)
    try:
        print(divide(-1, 1)),  # Negative test case (should throw error)
    except ValueError as e:
        print(e)

    print(divide(1, 1)),
    print(divide(0, 1)),
    print(divide(12, 3))
    print(divide(13, 3))
    print(divide(25, 5))
    print(divide(25, 7))
    print(divide(123456, 123))
    print(divide(987654321, 12345))
    print(divide(2**31 - 1, 1)),  # Maximum positive value for a 32-bit signed int
    print(divide(2**31 - 1, 2**30)),
    print(divide(10**10, 10**5)),  # Over 32-bit integer limit into Python bigints
    print(divide(10**25, 10**12)),


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
