"""
Problem:

Given an even number (greater than 2), return two prime numbers whose sum will be equal
to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

numut: 4 Output: 2 + 2 = 4 If there are more than one solution possible, return the
lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
if a < c or a==c and b < d.
"""

from typing import Tuple


def is_prime(num: int) -> bool:
    # time complexity: O(log(n))
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_prime_sum(num: int) -> Tuple[int, int]:
    if num > 2 and is_prime(num - 2):
        return 2, num - 2
    if num > 3 and is_prime(num - 3):
        return 3, num - 3
    # all prime numbers are of the form (6n + 1) or (6n - 1)
    for i in range(6, num // 2, 6):
        if is_prime(i - 1) and is_prime(num - i + 1):
            return (i - 1), (num - i + 1)
        elif is_prime(i + 1) and is_prime(num - i - 1):
            return (i + 1), (num - i - 1)


if __name__ == "__main__":
    num = 4
    num_1, num_2 = get_prime_sum(num)
    print(f"{num} = {num_1} + {num_2}")

    num = 10
    num_1, num_2 = get_prime_sum(num)
    print(f"{num} = {num_1} + {num_2}")

    num = 100
    num_1, num_2 = get_prime_sum(num)
    print(f"{num} = {num_1} + {num_2}")


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(1)
"""
