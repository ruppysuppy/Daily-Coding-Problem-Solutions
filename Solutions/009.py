"""
Problem:

Given a list of integers, write a function that returns the largest sum of non-adjacent
numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should
return 10, since we pick 5 and 5.
"""

from typing import List


def max_nonadjacent_sum(arr: List[int]) -> int:
    including = 0
    excluding = 0
    for elem in arr:
        # updating maximum sum including and excluding the current element
        including, excluding = max(excluding + elem, elem), max(excluding, including)
    return max(including, excluding)


if __name__ == "__main__":
    print(max_nonadjacent_sum([2, 4, 6, 8]))
    print(max_nonadjacent_sum([5, 1, 1, 5]))
    print(max_nonadjacent_sum([-5, 1, 1, -5]))
    print(max_nonadjacent_sum([5, 5, 10, 100, 10, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
