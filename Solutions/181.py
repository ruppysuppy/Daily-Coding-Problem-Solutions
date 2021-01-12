"""
Problem:

Given a string, split it into as few strings as possible such that each string is a
palindrome.

For example, given the input string "racecarannakayak", return
["racecar", "anna", "kayak"].

Given the input string "abc", return ["a", "b", "c"].
"""

from typing import List


def is_palindrome(string: str) -> bool:
    return string and string == string[::-1]


def split_into_string_list_helper(
    string: str, current: str, palindrome_list: List[str]
) -> List[str]:
    if not string and not current:
        return palindrome_list
    elif not string:
        return palindrome_list + list(current)
    # generating the palindrome list
    curr = current + string[0]
    if is_palindrome(curr):
        # adding curr to the list of palindromes
        palindrome_list_1 = split_into_string_list_helper(
            string[1:], "", palindrome_list + [curr]
        )
        # checking if a larger palindrome can be obtained
        palindrome_list_2 = split_into_string_list_helper(
            string[1:], curr, palindrome_list
        )
        return min(palindrome_list_1, palindrome_list_2, key=lambda List: len(List))
    return split_into_string_list_helper(string[1:], curr, palindrome_list)


def split_into_string_list(string: str) -> List[str]:
    return split_into_string_list_helper(string, "", [])


if __name__ == "__main__":
    print(split_into_string_list("racecarannakayak"))
    print(split_into_string_list("abc"))
    print(split_into_string_list("abbbc"))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
