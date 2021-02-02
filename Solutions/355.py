"""
Problem:

You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded
up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

The rounded sums of both arrays should be equal.
The absolute pairwise difference between elements is minimized. In other words,
|x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better
than [1, 2, 5], which has an absolute difference of
|1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
"""

from typing import List, Tuple


def get_fraction_from_tuple(tup: Tuple[int, float]) -> float:
    _, elem = tup
    return elem - int(elem)


def round_arr(arr: List[float]) -> List[int]:
    rounded_arr = [round(elem) for elem in arr]
    sum_arr = int(sum(arr))
    sum_rounded_arr = sum(rounded_arr)
    # if the sums are equal, the rounding has been properly implemented
    if sum_arr == sum_rounded_arr:
        return rounded_arr
    # eqalizing the sums
    should_increment = sum_arr > sum_rounded_arr
    num_map = sorted(
        [(index, elem) for index, elem in enumerate(arr)],
        key=get_fraction_from_tuple,
        reverse=should_increment,
    )
    # incrementing and decrementing the values as per requirement (while minimizing the
    # pair-wise sum)
    for i in range(sum_arr - sum_rounded_arr):
        index, _ = num_map[i]
        rounded_arr[index] = (
            rounded_arr[index] + 1 if should_increment else rounded_arr[index] - 1
        )
    return rounded_arr


if __name__ == "__main__":
    print(round_arr([1.3, 2.3, 4.4]))
    print(round_arr([1.8, 2.8, 4.4]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
