"""
Problem:

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.
For a pattern to be valid, it must satisfy the following:
* All of its keys must be distinct.
* It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

from copy import deepcopy
from typing import Set


class Dialpad:
    def __init__(self) -> None:
        self.nodes = set(range(1, 10))
        self.edges = {}
        self.edges[1] = {2, 4, 5, 6, 8}
        self.edges[2] = {1, 3, 4, 5, 6, 7, 9}
        self.edges[3] = {2, 4, 5, 6, 8}
        self.edges[4] = {1, 2, 3, 5, 7, 8, 9}
        self.edges[5] = {1, 2, 3, 4, 6, 7, 8, 9}
        self.edges[6] = {1, 2, 3, 5, 7, 8, 9}
        self.edges[7] = {2, 4, 5, 6, 8}
        self.edges[8] = {1, 4, 3, 5, 6, 7, 9}
        self.edges[9] = {2, 4, 5, 6, 8}

    def update_connections(self, curr: int) -> None:
        if 2 == curr:
            self.edges[1].add(3)
            self.edges[3].add(1)
        elif 4 == curr:
            self.edges[1].add(7)
            self.edges[7].add(1)
        elif 6 == curr:
            self.edges[9].add(3)
            self.edges[3].add(9)
        elif 8 == curr:
            self.edges[7].add(9)
            self.edges[9].add(7)
        elif 5 == curr:
            self.edges[1].add(9)
            self.edges[9].add(1)
            self.edges[7].add(3)
            self.edges[3].add(7)
            self.edges[2].add(8)
            self.edges[8].add(2)
            self.edges[4].add(6)
            self.edges[6].add(4)


def count_code_helper(dp: Dialpad, code_length: int, curr: int, seen: Set[int]) -> int:
    # helper function to trace the patterns and get the number of combinations
    if code_length == 0:
        return 1
    seen_cp = deepcopy(seen)
    seen_cp.add(curr)

    copied_dp = deepcopy(dp)
    copied_dp.update_connections(curr)
    nodes = dp.edges[curr]
    sub_count = 0

    for node in nodes:
        if node not in seen_cp:
            sub_count += count_code_helper(copied_dp, code_length - 1, node, seen_cp)
    return sub_count


def count_codes_of_n_length(dp: Dialpad, code_length: int) -> int:
    if code_length == 1:
        return len(dp.nodes)
    count = 0
    for node in dp.nodes:
        count += count_code_helper(dp, code_length, node, set())
    return count


def get_number_of_valid_unlock_patterns() -> int:
    dp = Dialpad()
    result = 0
    for n in range(1, 10):
        result += count_codes_of_n_length(dp, n)
    return result


if __name__ == "__main__":
    # NOTE: computationally intensive operation as the number of patterns is really high
    print(get_number_of_valid_unlock_patterns())


"""
SPECS:

TIME COMPLEXITY: O((nodes ^ 2) x (code length ^ 2))
SPACE COMPLEXITY: O((nodes ^ 2) x code length)
"""
