"""
Problem:

You are given a circular lock with three wheels, each of which display the numbers 0
through 9 in order. Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you turn the
wheels to one of these combinations, the lock becomes stuck in that state and cannot be
opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either
direction. Given a lock initially set to 000, a target combination, and a list of dead
ends, write a function that returns the minimum number of moves required to reach the
target state, or None if this is impossible.
"""

from sys import maxsize
from typing import List, Tuple, Set


def turn_wheel_up(val: int) -> int:
    return (val + 1) % 10


def turn_wheel_down(val: int) -> int:
    return (val - 1 + 10) % 10


def get_min_moves_helper(
    curr: List[int],
    pattern: List[int],
    dead_ends: Set[Tuple[int, int, int]],
    seen: Set[str],
    accumulator: int = 0,
) -> int:
    if curr == pattern:
        return accumulator
    curr_val = "".join([str(x) for x in curr])
    if curr_val in seen:
        # if a loop back occours, the target pattern cannot be reached
        return maxsize
    seen.add(curr_val)

    moves = []
    for i in range(3):
        temp = curr.copy()
        if temp[i] != pattern[i]:
            temp[i] = turn_wheel_up(temp[i])
            if tuple(temp) not in dead_ends:
                moves.append(temp)
        temp = curr.copy()
        if temp[i] != pattern[i]:
            temp[i] = turn_wheel_down(temp[i])
            if tuple(temp) not in dead_ends:
                moves.append(temp)

    temp = maxsize
    for move in moves:
        temp = min(
            temp, get_min_moves_helper(move, pattern, dead_ends, seen, accumulator + 1),
        )
    return temp


def get_min_moves(pattern, dead_ends):
    result = get_min_moves_helper([0, 0, 0], pattern, dead_ends, set())
    if result == maxsize:
        return None
    return result


if __name__ == "__main__":
    print(get_min_moves([3, 4, 5], set([])))
    print(get_min_moves([3, 4, 5], set([(0, 0, 1), (0, 1, 0), (1, 0, 0)])))
    print(
        get_min_moves(
            [3, 4, 5],
            set([(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, 9), (0, 9, 0), (9, 0, 0)]),
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n ^ n)
SPACE COMPLEXITY: O(n ^ n)
[n = max(pattern)]
"""

