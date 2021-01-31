"""
Problem:

You are given an string representing the initial conditions of some dominoes. Each
element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a
domino receives a force from the left and right side simultaneously, it will remain
upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

from typing import List


def get_config_helper(dominos: List[str], length: int) -> List[str]:
    has_been_updated = False
    updated_dominos = dominos.copy()
    for i in range(length):
        if (
            dominos[i] == "L"
            and i > 0
            and dominos[i - 1] == "."
            and ((i > 1 and dominos[i - 2] != "R") or i <= 1)
        ):
            updated_dominos[i - 1] = "L"
            has_been_updated = True
        elif (
            dominos[i] == "R"
            and i < length - 1
            and dominos[i + 1] == "."
            and ((i < length - 2 and dominos[i + 2] != "L") or i >= length - 2)
        ):
            updated_dominos[i + 1] = "R"
            has_been_updated = True
    if has_been_updated:
        return get_config_helper(updated_dominos, length)
    return dominos


def get_config(initial_state: str) -> str:
    dominoes = list(initial_state)
    return "".join(get_config_helper(dominoes, len(dominoes)))


if __name__ == "__main__":
    print(get_config(".L.R....L"))
    print(get_config("..R...L.L"))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n ^ 2)
[each iteration takes O(n) in both time & space and there can be n such iterations]
"""
