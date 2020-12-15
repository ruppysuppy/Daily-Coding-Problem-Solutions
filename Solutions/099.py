"""
Problem:

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is
[1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

from typing import List


def longest_consecutive_elements_sequence(arr: List[int]) -> int:
    length = len(arr)
    arr_elems_set = set(arr)
    longest_sequence = 0
    # generating the longest sequence length
    for i in range(length):
        if (arr[i] - 1) not in arr_elems_set:
            # current element is the starting element of a sequence
            j = arr[i]
            while j in arr_elems_set:
                j += 1
            # update longest sequence length
            longest_sequence = max(longest_sequence, j - arr[i])
    return longest_sequence


if __name__ == "__main__":
    print(longest_consecutive_elements_sequence([100, 4, 200, 1]))
    print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3]))
    print(longest_consecutive_elements_sequence([100, 4, 200, 2, 3]))
    print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_elements_sequence([100, 4, 200, 1, 3, 2, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
