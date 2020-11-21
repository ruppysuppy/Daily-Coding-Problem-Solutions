"""
Problem:

Given a string, find the longest palindromic contiguous substring. If there are more
than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest
palindromic substring of "bananas" is "anana".
"""


def is_palindrome(string: str) -> bool:
    # helper function to check if a string is a palindrome
    return string == string[::-1]


def get_longest_palindrome_substring(string: str) -> str:
    if is_palindrome(string):
        return string
    # generating the longest palindromic substring
    string1 = get_longest_palindrome_substring(string[1:])
    string2 = get_longest_palindrome_substring(string[:-1])
    return max(string1, string2, key=lambda s: len(s))


if __name__ == "__main__":
    print(get_longest_palindrome_substring("aabcdcb"))
    print(get_longest_palindrome_substring("bananas"))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
