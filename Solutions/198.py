"""
Problem:

Given a set of distinct positive integers, find the largest subset such that every pair
of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given
[1, 3, 6, 24], return [1, 3, 6, 24].
"""

from typing import List


def get_largest_subset_helper(
    arr: List[int],
    length: int,
    prev_num: int = 1,
    curr_ind: int = 0,
    prev_subset: List[int] = [],
) -> List[int]:
    if curr_ind == length:
        return prev_subset

    curr_elem = arr[curr_ind]
    res = get_largest_subset_helper(arr, prev_num, curr_ind + 1, prev_subset)
    if curr_elem % prev_num == 0:
        # generating the alternate result (with the element added)
        alternate_res = get_largest_subset_helper(
            arr, curr_elem, curr_ind + 1, prev_subset + [curr_elem]
        )
        return max(alternate_res, res, key=lambda result: len(result))
    return res


def get_largest_subset(arr: List[int]) -> List[int]:
    arr.sort()
    return get_largest_subset_helper(arr, len(arr), prev_subset=[])


if __name__ == "__main__":
    print(get_largest_subset([]))
    print(get_largest_subset([2]))
    print(get_largest_subset([2, 3]))
    print(get_largest_subset([3, 5, 10, 20, 21]))
    print(get_largest_subset([1, 3, 6, 24]))
    print(get_largest_subset([3, 9, 15, 30]))
    print(get_largest_subset([2, 3, 9, 15, 30]))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
