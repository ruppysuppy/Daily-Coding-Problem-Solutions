"""
Problem:

Given an array of integers, return a new array where each element in the new array is
the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

from typing import List


def get_smaller_elements_arr(arr: List[int]) -> List[int]:
    smaller_elements_arr = []
    length = len(arr)

    for i in range(length):
        smaller_elements = 0
        for j in range(i + 1, length):
            if arr[i] > arr[j]:
                smaller_elements += 1
        smaller_elements_arr.append(smaller_elements)
    return smaller_elements_arr


if __name__ == "__main__":
    print(get_smaller_elements_arr([3, 4, 9, 6, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
