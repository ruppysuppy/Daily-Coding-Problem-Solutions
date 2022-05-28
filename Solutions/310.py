"""
Problem:

Write an algorithm that finds the total number of set bits in all integers between 1
and N.
"""

from math import log
from time import perf_counter


def get_set_bits(num: int) -> int:
    bin_num = bin(num)[2:]
    return sum([int(digit) for digit in bin_num])


def get_total_set_bits(N: int) -> int:
    result = 0
    for i in range(1, N + 1):
        result += get_set_bits(i)
    return result


def get_total_set_bits_optimized(N: int) -> int:
    if N < 1:
        return 0

    # Find the greatest power of 2 less than or equal to n
    exp = int(log(N, 2))
    pow = 2**exp

    # Initializations
    extra_ones = 0
    sum = 0
    while True:
        # Count the bits of the pow-many numbers starting from where we left off (or 1, if the first iteration)
        # The logic here is that each of the least significant exp-many bits occurs in half those numbers, i.e. pow/2 times. Plus all the more significant bits that are constantly set throughout
        sum += pow // 2 * exp + pow * extra_ones

        # All numbers above this will have an additional bit set
        extra_ones += 1

        # If n is a power of two, add its own bits and exit
        if pow == N:
            sum += extra_ones
            break

        # Now set n to be the remainder after counting pow numbers...
        N -= pow
        # ...and calculate the greatest power of 2 that is less than or equal to our new n
        while pow > N:
            pow //= 2
            exp -= 1

    return sum


if __name__ == "__main__":
    for i in list(range(6)) + [10**6]:
        for f in [get_total_set_bits, get_total_set_bits_optimized]:
            start = perf_counter()
            result = f(i)
            end = perf_counter()
            print(f"{result} ({end-start:.3} sec)")


"""
SPECS:

get_total_set_bits:
TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(1)

get_total_set_bits_optimized:
TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
