"""
Problem:

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate. Find it in linear time and
space.
"""

from typing import List


def find_duplicate(arr: List[int]) -> int:
    seen_numbers = set()
    for num in arr:
        if num in seen_numbers:
            return num
        seen_numbers.add(num)


if __name__ == "__main__":
    print(find_duplicate([1, 2, 4, 6, 5, 3, 2]))
    print(find_duplicate([3, 1, 4, 2, 3]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
