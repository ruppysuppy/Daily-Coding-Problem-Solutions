"""
Problem:

Given an array of positive integers, divide the array into two subsets such that the
difference between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which
has a difference of 5, which is the smallest possible difference.
"""

from typing import List, Tuple


def smallest_difference_sets(
    arr: List[int], set1: List[int] = [], set2: List[int] = []
) -> Tuple[List[int], List[int]]:
    if not arr:
        return set1, set2
    # generating the possible lists
    temp = arr.pop()
    temp1_1, temp2_1 = smallest_difference_sets(list(arr), set1 + [temp], list(set2))
    temp1_2, temp2_2 = smallest_difference_sets(list(arr), list(set1), set2 + [temp])
    # returning the lists with smaller difference
    diff1 = abs(sum(temp1_1) - sum(temp2_1))
    diff2 = abs(sum(temp1_2) - sum(temp2_2))
    if diff1 < diff2:
        return temp1_1, temp2_1
    return temp1_2, temp2_2


if __name__ == "__main__":
    print(smallest_difference_sets([5, 10, 15, 20, 25], [], []))
    print(smallest_difference_sets([5, 10, 15, 20], [], []))
    print(smallest_difference_sets([500, 10, 15, 20, 25], [], []))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n ^ 2)
"""
