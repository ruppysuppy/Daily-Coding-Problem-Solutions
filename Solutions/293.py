"""
Problem:

You have N stones in a row, and would like to create from them a pyramid. This pyramid
should be constructed such that the height of each stone increases by one until
reaching the tallest stone, after which the heights decrease by one. In addition, the
start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height
by 1, as many times as necessary. Given this information, determine the lowest cost
method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to
create [0, 1, 2, 3, 2, 1].
"""

from typing import List


def get_min_pyramid_cost(arr: List[int]) -> int:
    length = len(arr)
    left = [0 for _ in range(length)]
    right = [0 for _ in range(length)]
    # calculate maximum height (left)
    left[0] = min(arr[0], 1)
    for i in range(1, length):
        left[i] = min(arr[i], min(left[i - 1] + 1, i + 1))
    # calculate maximum height (right)
    right[length - 1] = min(arr[length - 1], 1)
    for i in range(length - 2, -1, -1):
        right[i] = min(arr[i], min(right[i + 1] + 1, length - i))

    # find minimum possible among calculated values
    tot = [0 for _ in range(length)]
    for i in range(length):
        tot[i] = min(right[i], left[i])
    # find maximum height of pyramid
    max_ind = 0
    for i in range(length):
        if tot[i] > tot[max_ind]:
            max_ind = i

    # calculate cost of this pyramid
    cost = 0
    height = tot[max_ind]
    # calculate cost of left half
    for x in range(max_ind, -1, -1):
        cost += arr[x] - height
        height = max(0, height - 1)
    # calculate cost of right half
    height = tot[max_ind] - 1
    for x in range(max_ind + 1, length):
        cost += arr[x] - height
        height = max(0, height - 1)
    return cost


if __name__ == "__main__":
    print(get_min_pyramid_cost([1, 1, 3, 3, 2, 1]))
    print(get_min_pyramid_cost([1, 1, 1, 1, 1]))
    print(get_min_pyramid_cost([1, 1, 1, 5, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
