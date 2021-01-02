"""
Problem:

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the
sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the
pre-processing step.
"""

from typing import List


class SubarraySumOptimizer:
    def __init__(self, arr: List[int]) -> None:
        # runs in O(n) time, O(n) space
        self.preprocessed_arr = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            self.preprocessed_arr[i + 1] = self.preprocessed_arr[i] + arr[i]

    def sum(self, start: int, end: int) -> int:
        # runs in O(1) time, O(1) space
        # NOTE: the sum is supposed to return the sum in the range [start, end)
        if (start < 0) or (end > len(self.preprocessed_arr) - 1) or (start > end):
            return 0
        return self.preprocessed_arr[end] - self.preprocessed_arr[start]


if __name__ == "__main__":
    sso = SubarraySumOptimizer([1, 2, 3, 4, 5])

    print(sso.sum(1, 3))
    print(sso.sum(0, 5))
    print(sso.sum(0, 4))
    print(sso.sum(3, 4))
