"""
Problem:

Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X
if every interval in X contains at least one point in P. Compute the smallest set of
points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return
[4, 9].
"""

from typing import List, Tuple


def get_stab(list_of_intervals: List[Tuple[int]]) -> Tuple[int, int]:
    start, end = zip(*list_of_intervals)
    return min(end), max(start)


if __name__ == "__main__":
    print(get_stab([(1, 4), (4, 5), (7, 9), (9, 12)]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[even though zip is a generator and takes O(1) space, destructuring the array takes
O(n) space]
"""
