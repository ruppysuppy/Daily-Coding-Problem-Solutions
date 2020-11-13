"""
Problem:

Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""

from typing import List


def product_of_arr_except_ith_elem(arr: List[int]) -> int:
    length = len(arr)
    result = [1 for _ in range(length)]
    # multiplying all the elements on the left of the ith element in the 1st pass
    # and all the elements on the right of the ith element in the 2nd pass
    prod = 1
    for i in range(length):
        result[i] *= prod
        prod *= arr[i]
    prod = 1
    for i in range(length - 1, -1, -1):
        result[i] *= prod
        prod *= arr[i]
    return result


if __name__ == "__main__":
    print(product_of_arr_except_ith_elem([1, 2, 3, 4, 5]))
    print(product_of_arr_except_ith_elem([3, 2, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
