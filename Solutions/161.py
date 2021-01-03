"""
Problem:

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return
0000 1111 0000 1111 0000 1111 0000 1111.
"""


def complement_1s(num: str) -> str:
    result = ""
    for digit in num:
        result += str(int(not int(digit)))
    return result


if __name__ == "__main__":
    print(complement_1s("11110000111100001111000011110000"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
