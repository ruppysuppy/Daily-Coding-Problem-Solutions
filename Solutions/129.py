"""
Problem:

Given a real number n, find the square root of n. For example, given n = 9, return 3.
"""

TOLERENCE = 10 ** (-6)


def almost_equal(num1: float, num2: float) -> bool:
    return num1 - TOLERENCE < num2 < num1 + TOLERENCE


def get_sqrt(num: int) -> float:
    # using binary search to get the sqaure-root
    high, low = num, 0
    while True:
        mid = (high + low) / 2
        mid_square = mid * mid
        if almost_equal(mid_square, num):
            return round(mid, 6)
        elif mid_square < num:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == "__main__":
    print(get_sqrt(100))
    print(get_sqrt(9))
    print(get_sqrt(3))
    print(get_sqrt(2))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
