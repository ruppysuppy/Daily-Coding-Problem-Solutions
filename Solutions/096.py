"""
Problem:

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

from copy import deepcopy
from typing import List, Optional


def generate_all_permutations(
    arr: List[int], l: int = 0, r: Optional[int] = None, res: List[List[int]] = []
) -> List[List[int]]:
    if r is None:
        r = len(arr) - 1
    if l == r:
        res.append(list(arr))
        return res
    # generating all permutation using backtracking
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]
        generate_all_permutations(arr, l + 1, r, res)
        arr[l], arr[i] = arr[i], arr[l]
    return res


if __name__ == "__main__":
    print(generate_all_permutations([1, 2, 3], res=[]))
    print(generate_all_permutations([1, 2], res=[]))
    print(generate_all_permutations([1], res=[]))
    print(generate_all_permutations([], res=[]))


"""
SPECS:

TIME COMPLEXITY: O(n!)
SPACE COMPLEXITY: O(n!)
[there are n! permutions for an array with n elements]
"""
