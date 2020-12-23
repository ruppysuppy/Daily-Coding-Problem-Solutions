"""
Problem:

Given a set of closed intervals, find the smallest set of numbers that covers all the
intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers
that covers all these intervals is {3, 6}.
"""

from typing import List, Optional, Tuple


def get_spanning_interval(intervals: List[List[int]]) -> Optional[Tuple]:
    if not intervals:
        return
    start = intervals[0][1]
    end = start
    pos = 1
    # updating start
    for interval in intervals[1:]:
        interval_start, interval_end = interval
        if interval_start < start and interval_end < start:
            start = interval_end
            pos += 1
        else:
            break
    # updating end
    for interval in intervals[pos:]:
        interval_start, _ = interval
        if interval_start > end:
            end = interval_start
    return start, end


if __name__ == "__main__":
    print(get_spanning_interval([[0, 3]]))
    print(get_spanning_interval([[0, 3], [2, 6]]))
    print(get_spanning_interval([[0, 3], [2, 6], [3, 4]]))
    print(get_spanning_interval([[0, 3], [2, 6], [3, 4], [6, 7]]))
    print(get_spanning_interval([[0, 3], [2, 6], [3, 4], [6, 9]]))
    print(get_spanning_interval([[0, 3], [2, 6], [3, 4], [6, 100]]))
    print(get_spanning_interval([[0, 4], [1, 2], [5, 6]]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
