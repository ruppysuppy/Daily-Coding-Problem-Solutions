"""
Problem:

Given a list of integers S and a target number k, write a function that returns a
subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list
are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it
sums up to 24.
"""

from typing import List, Optional


def target_sum(arr: List[int], k: int) -> Optional[List[int]]:
    if not arr:
        return None
    elem = arr[0]
    if elem == k:
        return [elem]
    # generating the subset
    possible_subset = target_sum(arr[1:], k - elem)
    if possible_subset is not None:
        return [elem] + possible_subset
    return target_sum(arr[1:], k)


if __name__ == "__main__":
    print(target_sum([12, 1, 61, 5, 9, 2], 24))
    print(target_sum([12, 1, 61, 5, 9, 2], 61))
    print(target_sum([12, 1, 61, 5, -108, 2], -106))
    print(target_sum([12, 1, 61, 5, -108, 2], 1006))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 3)
SPACE COMPLEXITY: O(n ^ 2)
"""
