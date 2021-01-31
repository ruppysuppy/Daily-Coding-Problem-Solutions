"""
Problem:

MegaCorp wants to give bonuses to its employees based on how many lines of codes they
have written. They would like to give the smallest positive amount to each worker
consistent with the constraint that if a developer has written more lines of code than
their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how
much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""

from typing import List


def get_bonus(arr: List[int]) -> List[int]:
    length = len(arr)
    if length == 0:
        return []
    if length == 1:
        return [1]

    comparison = [None for _ in range(length)]
    for i in range(1, length):
        if arr[i] > arr[i - 1]:
            comparison[i] = "+"
        elif arr[i] < arr[i - 1]:
            comparison[i] = "-"
        else:
            comparison[i] = "="

    i = 0
    comparison[0] = comparison[1]
    result = [0 for _ in range(length)]
    while i < length:
        # case: current element is larger than the previous element
        if i < length and comparison[i] == "+":
            j = i + 1
            while j < length and comparison[j] == "+":
                j += 1
            j -= 1
            curr = 1
            for k in range(i, j + 1):
                result[k] = curr
                curr += 1
            i = j + 1
        # case: current element is smaller than the previous element
        elif i < length and comparison[i] == "-":
            j = i - 1
            while j > 0 and result[j] == 1:
                result[j] += 1
                j -= 1
            j = i + 1
            while j < length and comparison[j] == "-":
                j += 1
            j -= 1
            curr = 1
            for k in range(j, i - 1, -1):
                result[k] = curr
                curr += 1
            i = j + 1
        # case: current element is equal to the previous element
        else:
            result[i] = result[i - 1]
            i += 1
    return result


if __name__ == "__main__":
    print(get_bonus([1000]))
    print(get_bonus([10, 40, 200, 1000, 60, 30]))
    print(get_bonus([10, 40, 200, 1000, 900, 800, 30]))
    print(get_bonus([10, 40, 200, 1000, 900, 800, 30, 30]))
    print(get_bonus([10, 40, 200, 1000, 800, 800, 30]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
