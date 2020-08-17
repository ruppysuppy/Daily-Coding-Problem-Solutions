"""
Problem:

Given a sorted list of integers of length N, determine if an element x is in the list
without performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
"""

from typing import List


def fibo_search(arr: List[int], val: int) -> int:
    # fibo search to search an element in a sorted array in O(log(n)) time [without
    # multiplication, division, or bit-shift operations]
    length = len(arr)
    if length == 0:
        return 0
    fib_N_2 = 0
    fib_N_1 = 1
    fibNext = fib_N_1 + fib_N_2

    while fibNext < len(arr):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2

    index = -1
    while fibNext > 1:
        i = min(index + fib_N_2, (length - 1))
        if arr[i] == val:
            return i
        fibNext = fib_N_1
        if arr[i] < val:
            fib_N_1 = fib_N_2
            index = i
        elif arr[i] > val:
            fib_N_1 = fib_N_1 - fib_N_2
        fib_N_2 = fibNext - fib_N_1

    if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
        return index + 1
    return -1


if __name__ == "__main__":
    print(fibo_search([1, 3, 5, 7, 9], 3))
    print(fibo_search([1, 3, 5, 7, 9], 1))
    print(fibo_search([1, 3, 5, 7, 9], 7))

    print(fibo_search([1, 3, 5, 7, 9], 6))
    print(fibo_search([1, 3, 5, 7, 9], 0))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
