"""
Problem:

Create an algorithm to efficiently compute the approximate median of a list of numbers.

More precisely, given an unordered list of N numbers, find an element whose rank is
between N / 4 and 3 * N / 4, with a high level of certainty, in less than O(N) time.
"""

# checkout the following link for complexity analysis:
# https://www.geeksforgeeks.org/randomized-algorithms-set-3-12-approximate-median/

from math import log10
from random import randint
from typing import List


def get_approx_median(arr: List[int]) -> int:
    length = len(arr)
    elements = min(int(10 * log10(length)), length)
    unique_elems = set()
    # selecting random log(n) * 10 elements
    for _ in range(elements):
        unique_elems.add(arr[randint(0, length - 1)])
    # getting the median of the selected elements
    sorted_unique_elems = sorted(list(unique_elems))
    return sorted_unique_elems[len(sorted_unique_elems) // 2]


if __name__ == "__main__":
    print(
        get_approx_median(
            [3, 4, 3, 2, 4, 3, 1, 4, 3, 4, 2, 3, 4, 3, 0, 4, 0, 0, 1, 1, 0, 1, 2]
        )
    )
    print(get_approx_median([1, 3, 2, 4, 5, 6, 8, 7]))


"""
Time: O(log(n) x log(log(n)))
Space: O(log(n))
"""
