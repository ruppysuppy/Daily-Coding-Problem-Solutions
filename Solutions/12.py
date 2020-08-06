'''
Problem:

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a
time. Given N, write a function that returns the number of unique ways you can climb
the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any
number from a set of positive integers X? For example, if X = {1, 3, 5}, you could
climb 1, 3, or 5 steps at a time.
'''

from typing import List


def count_ways(steps: int, permissable_steps: List[int] = [1, 2]) -> int:
    # dynamic array to store the number of ways a step can be reached
    num_ways = [0 for i in range(steps+1)]
    # base case
    num_ways[0] = 1
    # calculating using the formula steps_i = sum(steps_i(i - j))
    # i ε [0, steps); j ε permissable_steps
    for pos in range(steps + 1):
        for step in permissable_steps:
            temp_pos = pos - step
            if temp_pos >= 0:
                num_ways[pos] += num_ways[temp_pos]
    return num_ways[steps]


# DRIVER CODE
print(count_ways(4))
print(count_ways(1, [1, 3, 5]))
print(count_ways(2, [1, 3, 5]))
print(count_ways(3, [1, 3, 5]))
print(count_ways(4, [1, 3, 5]))
print(count_ways(5, [1, 3, 5]))
print(count_ways(6, [1, 3, 5]))


'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = number of steps]
'''
