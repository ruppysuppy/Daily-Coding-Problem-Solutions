"""
Problem:

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route:
100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""


from typing import Tuple


def get_closest_factors(num: int) -> Tuple[int, int]:
    a, b = 1, num
    factor_1, factor_2 = 1, 1
    while b > a:
        if num % a == 0:
            factor_1, factor_2 = a, num // a
        b = num / a
        a += 1
    return (factor_1, factor_2)


def get_step_size(num: int, steps: int = 0) -> int:
    if num < 1:
        raise ValueError(f"Cannot reach 1 from {num}")
    if num == 1:
        return steps
    # generating the sequence to get the least number of steps
    largest_factor = max(get_closest_factors(num))
    if largest_factor == num:
        return get_step_size(num - 1, steps + 1)
    return min(
        get_step_size(num - 1, steps + 1), get_step_size(largest_factor, steps + 1)
    )


if __name__ == "__main__":
    print(get_step_size(100))  # 100 -> 10 -> 9 -> 3 -> 2 -> 1
    print(get_step_size(64))  # 64 -> 8 -> 4 -> 2 -> 1


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n) [considering call-stack]
"""
