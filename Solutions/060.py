"""
Problem:

Given a multiset of integers, return whether it can be partitioned into two subsets
whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it
up into two subsets that add up to the same sum.
"""

from typing import List


def equal_sum_split_check_helper(
    arr: List[int], start: int, stop: int, sum_inner: int, sum_outer: int
) -> bool:
    if start >= stop:
        return False
    elif sum_inner == sum_outer:
        return True
    # checking for all possible splits
    return equal_sum_split_check_helper(
        arr, start + 1, stop, sum_inner - arr[start], sum_outer + arr[start]
    ) or equal_sum_split_check_helper(
        arr, start, stop - 1, sum_inner - arr[stop], sum_outer + arr[stop]
    )


def equal_sum_split_check(arr: List[int]) -> bool:
    # cases where the array cannot be split
    total_sum = sum(arr)
    if not arr or total_sum % 2 == 1:
        return False
    # sorting the array (pre-requisite for split_helper)
    arr.sort()
    return equal_sum_split_check_helper(arr, 0, len(arr) - 1, total_sum, 0)


if __name__ == "__main__":
    print(equal_sum_split_check([15, 5, 20, 10, 35, 15, 10]))
    print(equal_sum_split_check([15, 5, 20, 10, 35]))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n) [recursion depth]
"""
