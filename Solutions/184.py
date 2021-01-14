"""
Problem:

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

from math import gcd as gcd_of_2
from typing import List


def gcd(nums: List[int]) -> int:
    if not nums:
        return None

    result = nums[0]
    for num in nums[1:]:
        result = gcd_of_2(result, num)
    return result


if __name__ == "__main__":
    print(gcd([42, 56, 14]))
    print(gcd([3, 5]))
    print(gcd([9, 15]))


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(1)
"""
