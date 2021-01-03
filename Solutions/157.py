"""
Problem:

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar,
which is a palindrome. daily should return false, since there's no rearrangement that
can form a palindrome.
"""


def is_permutation_palindrome(string: str) -> str:
    char_set = set()

    for char in string:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)
    length = len(char_set)
    if length in (1, 0):
        return True
    return False


if __name__ == "__main__":
    print(is_permutation_palindrome("carrace"))
    print(is_permutation_palindrome("daily"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
