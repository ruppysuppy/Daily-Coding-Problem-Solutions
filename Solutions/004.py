"""
Problem:

Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in
the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

from typing import List


def first_missing_positive_integer(arr: List[int]) -> int:
    # placing the positive elements (< length) in their proper position
    # proper position index = element - 1
    # if after the palcement is complete, index of the 1st element not in its proper
    # position is the answer
    length = len(arr)
    for i in range(length):
        correctPos = arr[i] - 1
        while 1 <= arr[i] <= length and arr[i] != arr[correctPos]:
            arr[i], arr[correctPos] = arr[correctPos], arr[i]
            correctPos = arr[i] - 1
    # finding the first missing positive integer
    for i in range(length):
        if i + 1 != arr[i]:
            return i + 1
    return length + 1


if __name__ == "__main__":
    print(first_missing_positive_integer([3, 4, 2, 1]))
    print(first_missing_positive_integer([3, 4, -1, 1]))
    print(first_missing_positive_integer([1, 2, 5]))
    print(first_missing_positive_integer([-1, -2]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)

NOTE: Even though there is a nested loop it is a O(n) algorithm as the cap on the
      maximum iterations is 2 * n [Amortised analysis]
"""
