"""
Problem:

A permutation can be specified by an array P, where P[i] represents the location of the
element at i in the permutation. For example, [2, 1, 0] represents the permutation
where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example,
given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

from typing import List


def permute(arr: List[str], p: List[int]) -> List[str]:
    for i in range(len(p)):
        p[i] = arr[p[i]]
    return p


if __name__ == "__main__":
    print(permute(["a", "b", "c"], [2, 1, 0]))
    print(permute(["a", "b", "c", "d"], [3, 0, 1, 2]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
