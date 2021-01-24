"""
Problem:

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between
0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0
itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""

from typing import List

ACCEPTABLE_NUMBERS = set([str(i) for i in range(256)])


def get_ip_combinations_helper(
    string: str, curr: List[str], accumulator: List[List[str]]
) -> None:
    if not string and len(curr) == 4:
        accumulator.append(list(curr))
        return
    elif len(curr) > 4:
        return

    curr_part = ""
    for char in string:
        curr_part += char
        length = len(curr_part)
        if length > 3:
            return
        if curr_part in ACCEPTABLE_NUMBERS:
            get_ip_combinations_helper(
                string[length:], list(curr) + [curr_part], accumulator
            )


def get_ip_combinations(string: str) -> List[str]:
    accumulator = []
    get_ip_combinations_helper(string, [], accumulator)
    return [".".join(combination) for combination in accumulator]


if __name__ == "__main__":
    print(get_ip_combinations("2542540123"))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(2 ^ n)
"""
