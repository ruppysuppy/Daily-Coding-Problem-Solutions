"""
Problem:

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall
that a Pythogorean triplet (a, b, c) is defined by the equation a^2 + b^2 = c^2.
"""

from math import sqrt
from typing import List, Optional, Tuple


def get_pythogorean_triplet(
    arr: List[int],
) -> Tuple[Optional[int], Optional[int], Optional[int]]:
    length = len(arr)
    if length < 3:
        return False
    # generating the set of squared values for O(1) access
    squared_arr = [elem * elem for elem in arr]
    value_set = set(squared_arr)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if squared_arr[i] + squared_arr[j] in value_set:
                return (
                    int(sqrt(squared_arr[i])),
                    int(sqrt(squared_arr[j])),
                    int(sqrt(squared_arr[i] + squared_arr[j])),
                )
    return None, None, None


if __name__ == "__main__":
    print(get_pythogorean_triplet([3, 4, 5, 6, 7]))
    print(get_pythogorean_triplet([3, 5, 6, 7]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
