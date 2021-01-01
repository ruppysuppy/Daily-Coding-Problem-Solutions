"""
Problem:

Given a list, sort it using this method: reverse(lst, i, j), which sorts lst from i to
j.
"""

from typing import List


def reverse(lst: List[int], i: int, j: int) -> None:
    lst[i : j + 1] = lst[i : j + 1][::-1]


def bubble_sort(lst: List[int]) -> List[int]:
    length = len(lst)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                reverse(lst, j, j + 1)
    return lst


if __name__ == "__main__":
    print(bubble_sort([0, 6, 4, 2, 5, 3, 1]))
    print(bubble_sort([0, 6, 4, 2, 5, 3, 1, 10, 9]))
    print(bubble_sort([0, 6, 4, 2, 5, 3, 1, 2, 3]))
    print(bubble_sort([0, 6, 4, 2, 5, 3, 1, 11]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1) [since reverse() is being used on adjacent indices]
"""
