"""
Problem:

Find the maximum of two numbers without using any if-else statements, branching, or
direct comparisons.
"""


def get_max(num1: int, num2: int) -> int:
    return num1 ^ ((num1 ^ num2) & -(num1 < num2))


if __name__ == "__main__":
    print(get_max(1, 5))
    print(get_max(4, 3))
    print(get_max(-3, 6))
    print(get_max(5, -4))
    print(get_max(-4, -2))
    print(get_max(-3, -6))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
