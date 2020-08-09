"""
Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from typing import List


def check_target_sum(arr: List[int], target: int) -> bool:
    # using hash list to store the previously seen values to get access to them in O(1)
    previous = set()
    for elem in arr:
        if (target - elem) in previous:
            return True
        previous.add(elem)
    return False


if __name__ == "__main__":
    print(check_target_sum([], 17))
    print(check_target_sum([10, 15, 3, 7], 17))
    print(check_target_sum([10, 15, 3, 4], 17))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
