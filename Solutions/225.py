"""
Problem:

There are N prisoners standing in a circle, waiting to be executed. The executions are
carried out starting with the kth person, and removing every successive kth person
going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order
to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so
you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

from typing import Optional


def find_last_executed(n: int, k: int) -> Optional[int]:
    prisoners = [i for i in range(1, n + 1)]
    last_executed = None
    curr_pos = 0

    while prisoners:
        curr_pos = (curr_pos + k - 1) % len(prisoners)
        last_executed = prisoners[curr_pos]
        prisoners = prisoners[:curr_pos] + prisoners[curr_pos + 1 :]
    return last_executed


if __name__ == "__main__":
    print(find_last_executed(5, 2))
    print(find_last_executed(3, 2))
    print(find_last_executed(5, 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
