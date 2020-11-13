"""
Problem:

Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

from typing import List, Tuple


def minimum_rooms_required(intervals: List[Tuple[int, int]]) -> int:
    delta_room_map = {}
    max_rooms = 0
    curr_rooms = 0
    # updating time map
    for start, end in intervals:
        if start not in delta_room_map:
            delta_room_map[start] = 0
        delta_room_map[start] += 1
        if end not in delta_room_map:
            delta_room_map[end] = 0
        delta_room_map[end] -= 1
    # generating the minimum number of rooms required
    sorted_events = sorted(delta_room_map.items(), key=lambda x: x[0])
    for _, rooms in sorted_events:
        curr_rooms += rooms
        max_rooms = max(max_rooms, curr_rooms)
    return max_rooms


if __name__ == "__main__":
    print(minimum_rooms_required([(30, 75), (0, 50), (60, 150)]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
