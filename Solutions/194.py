"""
Problem:

Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0
and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments
connecting each point pi to qi. Write an algorithm to determine how many pairs of the
line segments intersect.
"""

from typing import List


def num_intersect(arr1: List[int], arr2: List[int]) -> int:
    segments = list(zip(arr1, arr2))
    count = 0

    for i in range(len(segments)):
        p1_start, p1_end = segments[i]
        # checking if any other points intersect it
        for p2_start, p2_end in segments[:i]:
            if (p1_start < p2_start and p1_end > p2_end) or (
                p1_start > p2_start and p1_end < p2_end
            ):
                count += 1
    return count


if __name__ == "__main__":
    print(num_intersect([1, 2, 3, 4], [3, 2, 3, 2]))
    print(num_intersect([1, 4, 5], [4, 2, 3]))
    print(num_intersect([1, 4, 5], [2, 3, 4]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
