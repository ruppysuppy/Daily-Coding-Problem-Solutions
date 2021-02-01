"""
Problem:

An imminent hurricane threatens the coastal town of Codeville. If at most two people
can fit in a rescue boat, and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of
200, the smallest number of boats required will be three.
"""

from typing import List


def calculate_boats(arr: List[int], k: int) -> int:
    length = len(arr)
    arr.sort()

    ptr1 = 0
    ptr2 = length - 1
    result = 0
    while ptr1 < ptr2:
        if arr[ptr2] > k:
            # weight greater than boat weight limit
            raise ValueError(f"Cannot accomodate {arr[ptr2]} within limit of {k}")
        elif arr[ptr2] + arr[ptr1] > k:
            # 2 people CANNOT be accomodated in 1 boat
            result += 1
            ptr2 -= 1
        else:
            # 2 people CAN be accomodated in 1 boat
            result += 1
            ptr1 += 1
            ptr2 -= 1
    if ptr1 == ptr2:
        result += 1
    return result


if __name__ == "__main__":
    print(calculate_boats([100, 200, 150, 80], 200))


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(1)
"""

