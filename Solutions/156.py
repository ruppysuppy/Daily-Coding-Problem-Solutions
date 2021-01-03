"""
Problem:

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
"""


def min_square_num(num: int, accumulator: int = 0) -> int:
    if num == 0:
        return accumulator
    elif num == 1:
        return accumulator + 1

    largest_square_divisor = int(num ** 0.5) ** 2
    num = num - largest_square_divisor
    accumulator += 1
    return min_square_num(num, accumulator)


if __name__ == "__main__":
    print(min_square_num(25))  # (5 ^ 2)
    print(min_square_num(13))  # (2 ^ 2) + (3 ^ 2)
    print(min_square_num(27))  # (5 ^ 2) + (1 ^ 2) + (1 ^ 2)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
