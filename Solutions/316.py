"""
Problem:

You are given an array of length N, where each element i represents the number of ways
we can produce i units of change. For example, [1, 0, 1, 1, 2] would indicate that
there is only one way to make 0, 2, or 3 units, and two ways of making 4 units.

Given such an array, determine the denominations that must be in use. In the case
above, for example, there must be coins with value 2, 3, and 4.
"""

from typing import List


def count_ways_to_generate_change(changes: List[int], target: int) -> int:
    length = len(changes)
    if not length:
        return 0
    table = [[0 for x in range(length)] for x in range(target + 1)]
    for i in range(length):
        table[0][i] = 1
    for i in range(1, target + 1):
        for j in range(length):
            if i - changes[j] >= 0:
                x = table[i - changes[j]][j]
            else:
                x = 0
            if j >= 1:
                y = table[i][j - 1]
            else:
                y = 0
            table[i][j] = x + y
    return table[target][length - 1]


def get_changes(num_ways_to_get_change: List[int]) -> List[int]:
    length = len(num_ways_to_get_change)
    changes_list = []

    for i in range(1, length):
        if num_ways_to_get_change[i] > 0:
            count = count_ways_to_generate_change(changes_list, i)
            if count == 0 or count + 1 == num_ways_to_get_change[i]:
                changes_list.append(i)
    return changes_list


if __name__ == "__main__":
    print(get_changes([1, 0, 1, 1, 2]))
    print(get_changes([1, 0, 1, 1, 2, 1, 3]))
    print(get_changes([1, 0, 1, 1, 2, 1, 4]))
    print(get_changes([1, 0, 1, 1, 2, 1, 4, 2]))
    print(get_changes([1, 0, 1, 1, 2, 1, 4, 3]))


"""
SPECS:
TIME COMPLEXITY: O(n ^ 3)
SPACE COMPLEXITY: O(n ^ 2)
[n = number of elements]
"""
