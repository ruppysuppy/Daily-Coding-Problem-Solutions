"""
Problem:

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def calc_sum_of_digits(num: int) -> int:
    s = 0
    for digit in str(num):
        s += int(digit)
    return s


def get_nth_perfect_num_naive(n: int) -> int:
    num = 19
    count = 1
    while n > count:
        num += 1
        if calc_sum_of_digits(num) == 10:
            count += 1
    return num


if __name__ == "__main__":
    print(get_nth_perfect_num_naive(1))
    print(get_nth_perfect_num_naive(2))
    print(get_nth_perfect_num_naive(10))
