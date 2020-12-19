"""
Problem:

Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
"""

from typing import List


def can_reach_end(arr: List[int]) -> bool:
    length = len(arr)
    curr_position, last_index = 0, length - 1
    while curr_position < length:
        if curr_position == last_index:
            return True
        elif arr[curr_position] == 0:
            return False
        curr_position += arr[curr_position]
    return False


if __name__ == "__main__":
    print(can_reach_end([2, 0, 1, 0]))
    print(can_reach_end([1, 1, 0, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
