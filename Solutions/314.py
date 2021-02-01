"""
Problem:

You are the technical director of WSPT radio, serving listeners nationwide. For
simplicity's sake we can consider each listener to live along a horizontal line
stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers, each placed at various
locations along this line, determine what the minimum broadcast range would have to be
in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In this case
the minimum range would be 5, since that would be required for the tower at position 15
to reach the listener at position 20.
"""

from sys import maxsize
from typing import List


def get_min_range(listeners: List[int], towers: List[int]) -> int:
    # distance map storing the distance of listener from the nearest tower
    listeners_distance = {listener: maxsize for listener in listeners}
    for listener in listeners:
        for tower in towers:
            listeners_distance[listener] = min(
                listeners_distance[listener], abs(tower - listener)
            )
    return max(listeners_distance.values())


if __name__ == "__main__":
    print(get_min_range([1, 5, 11, 20], [4, 8, 15]))


"""
SPECS:

TIME COMPLEXITY: O(listeners x towers)
SPACE COMPLEXITY: O(listeners)
"""
