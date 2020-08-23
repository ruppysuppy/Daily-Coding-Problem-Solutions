"""
Problem:

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010
10101100. The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1
bytes all start with 10. Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and
returns whether it is a valid UTF-8 encoding.
"""

from re import compile
from typing import List

# acceptable expressions
EXPRESSIONS = [
    compile("0.{7}"),
    compile("110.{5}10.{6}"),
    compile("1110.{4}10.{6}10.{6}"),
    compile("11110.{3}10.{6}10.{6}10.{6}"),
]


def is_utf8(bin_num: str) -> bool:
    # using regular expression to match the input string
    for expression in EXPRESSIONS:
        if expression.match(bin_num):
            return True
    return False


def is_arr_utf8(arr: List[int]) -> bool:
    # the array cannot hold an utf8 symbol if the length of the array is more than 4 or
    # if any of the elements is larger than 255 (binary number contains more than 8
    # characters)
    if len(arr) > 4 or any([elem > 255 for elem in arr]):
        return False
    # generating the binary number
    bin_num = ""
    for elem in arr:
        num = bin(elem)[2:]
        bin_num += num.zfill(8)
    return is_utf8(bin_num)


if __name__ == "__main__":
    print(is_arr_utf8([127]))
    print(is_arr_utf8([226, 130, 172]))
    print(is_arr_utf8([226, 127, 172]))
    print(is_arr_utf8([256, 130, 172]))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
[its constant as the maximum size is 32 characters (constant)]
"""
