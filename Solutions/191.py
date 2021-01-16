"""
Problem:

Given a collection of intervals, find the minimum number of intervals you need to
remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered
overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval
can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""

from typing import List


def num_overlap(arr: List[int]) -> int:
    time_slot_usage = [False for _ in range(max(arr, key=lambda x: x[1])[1] + 1)]
    overlap_count = 0

    for interval in arr:
        start, end = interval
        overlap_flag = True
        for i in range(start, end):
            if not time_slot_usage[i]:
                time_slot_usage[i] = True
            elif overlap_flag:
                overlap_count += 1
                overlap_flag = False
    return overlap_count


if __name__ == "__main__":
    print(num_overlap([[0, 1], [1, 2]]))
    print(num_overlap([(7, 9), (2, 4), (5, 8)]))
    print(num_overlap([(7, 9), (2, 4), (5, 8), (1, 3)]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = maximum ending time]
"""
