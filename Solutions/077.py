"""
Problem:

Given a list of possibly overlapping intervals, return a new list of intervals where
all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
[(1, 3), (4, 10), (20, 25)].
"""

from typing import List, Tuple


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    start = intervals[0][0]
    end = intervals[0][1]
    # generating the merged intervals
    for interval in intervals[1:]:
        curr_start, curr_end = interval
        if end < curr_start:
            merged_intervals.append((start, end))
            start = curr_start
            end = curr_end
        elif end < curr_end and end > curr_start:
            end = curr_end
    # adding the last interval
    merged_intervals.append((start, end))
    return merged_intervals


if __name__ == "__main__":
    print(merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
    print(merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25), (6, 12)]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
