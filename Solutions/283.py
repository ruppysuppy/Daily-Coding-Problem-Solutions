"""
Problem:

A regular number in mathematics is defined as one which evenly divides some power of
60. Equivalently, we can say that a regular number is one whose only prime divisors are
2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to
tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular
numbers.
"""

from typing import List, Set


def get_prime_factors(num: int) -> Set[int]:
    factors = set()
    curr = 2
    while num > 1:
        while num > 1 and num % curr == 0:
            num = num // curr
            factors.add(curr)
        curr += 1
    return factors


def get_regular_numbers(N: int) -> List[int]:
    # using Sieve of Eratosthenes Method to optimally find the required numbers
    total_range = 2 * N
    SoE = [False for _ in range(total_range)]
    result = []
    count = 0
    factors = set([2, 3, 5])

    for factor in factors:
        for i in range(factor, total_range, factor):
            if not SoE[i] and not (get_prime_factors(i) - factors):
                SoE[i] = True

    for index, value in enumerate(SoE):
        if value:
            result.append(index)
            count += 1
            if count == N:
                break
    return result


if __name__ == "__main__":
    print(get_regular_numbers(10))


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(n)
"""
