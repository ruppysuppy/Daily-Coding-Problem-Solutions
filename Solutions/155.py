"""
Problem:

Given a list of elements, find the majority element, which appears more than half the
times (> floor(len(lst) / 2.0)).

You can assume that such an element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""

from typing import List, Optional


def majority_element(arr: List[int]) -> Optional[int]:
    length = len(arr)
    if not length:
        return
    elif length < 3:
        return arr[0]
    # getting the majority element by generating the frequencies
    frequency = {}
    for elem in arr:
        if elem not in frequency:
            frequency[elem] = 0
        frequency[elem] += 1
    for elem in frequency:
        if frequency[elem] > (length // 2):
            return elem


if __name__ == "__main__":
    print(majority_element([1, 2, 1, 1, 1, 4, 0]))
    print(majority_element([1, 1, 1, 3, 3, 3, 4, 1, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
