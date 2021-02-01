"""
Problem:

A fixed point in an array is an element whose value is equal to its index. Given a
sorted array of distinct elements, return a fixed point, if one exists. Otherwise,
return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should
return False.
"""

from typing import List, Union


def get_fixed_point(arr: List[int]) -> Union[int, False]:
    for index, value in enumerate(arr):
        if value == index:
            # fixed point found
            return value
        elif value > index:
            # since the array is sorted and has distinct elements, once the value
            # exceeds the index, the index can never be equal to the value at any
            # position
            break
    return False


if __name__ == "__main__":
    print(get_fixed_point([-6, 0, 2, 40]))
    print(get_fixed_point([1, 5, 7, 8]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
