"""
Problem:

Gray code is a binary code where each successive value differ in only one bit, as well
as when wrapping around. Gray code is common in hardware so that we don't see temporary
spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""

from typing import List


def get_grey_code(n: int) -> List[str]:
    if n == 0:
        return [""]
    # generating grey code
    previous_grey_code = get_grey_code(n - 1)
    base0 = ["0" + val for val in previous_grey_code]
    base1 = ["1" + val for val in previous_grey_code[::-1]]
    return base0 + base1


if __name__ == "__main__":
    print(get_grey_code(0))
    print(get_grey_code(1))
    print(get_grey_code(2))
    print(get_grey_code(3))
    print(get_grey_code(4))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(2 ^ n)
[there are (2 ^ n) grey codes of length n]
"""
