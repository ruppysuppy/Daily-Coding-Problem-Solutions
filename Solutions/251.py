"""
Problem:

Given an array of a million integers between zero and a billion, out of order, how can
you efficiently sort it? Assume that you cannot store an array of a billion elements in
memory.
"""

from random import randint
from typing import List


def gen_arr() -> List[int]:
    return [randint(0, 1_000_000_000) for _ in range(1_000_000)]


def counting_sort(arr: List[int], exp: int, n: int) -> int:
    # output array elements to store the sorted arr
    output = [0] * n
    count = [0] * 10
    # updating count
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    # genrating the output array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    # updating arr with output arr
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr: List[int]) -> None:
    length = len(arr)
    digits = len(str(max(arr)))
    exp = 1
    for _ in range(digits):
        counting_sort(arr, exp, length)
        exp *= 10


if __name__ == "__main__":
    radix_sort(gen_arr())


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(range of the numbers)
"""
