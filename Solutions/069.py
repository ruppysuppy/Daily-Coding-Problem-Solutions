"""
Problem:

Given a list of integers, return the largest product that can be made by multiplying
any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's
-10 * -10 * 5.

You can assume the list has at least three integers.
"""

from typing import List


def largest_product_of_3(arr: List[int]) -> int:
    # tracking the smallest 2 and the largest 3 numbers and generating the largest
    # product using them
    negative_1, negative_2 = 0, 0
    positive_1, positive_2, positive_3 = 0, 0, 0
    for elem in arr:
        if elem < negative_1:
            negative_2 = negative_1
            negative_1 = elem
        elif elem < negative_2:
            negative_2 = elem
        elif elem > positive_1:
            positive_3 = positive_2
            positive_2 = positive_1
            positive_1 = elem
        elif elem > positive_2:
            positive_3 = positive_2
            positive_2 = elem
        elif elem > positive_3:
            positive_3 = elem
    return max(
        positive_1 * negative_1 * negative_2, positive_1 * positive_2 * positive_3
    )


if __name__ == "__main__":
    print(largest_product_of_3([-10, -10, 5, 2]))
    print(largest_product_of_3([10, -10, 5, 2]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
