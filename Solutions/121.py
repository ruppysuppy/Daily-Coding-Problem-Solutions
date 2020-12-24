"""
Problem:

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get
'waterretaw'.
"""


def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def can_make_palindrome(string: str, k: int) -> bool:
    if is_palindrome(string):
        return True
    if not k:
        return False
    # checking all possible combinations of the string
    for i in range(len(string)):
        if can_make_palindrome(string[:i] + string[i + 1 :], k - 1):
            return True
    return False


if __name__ == "__main__":
    print(can_make_palindrome("a", 0))
    print(can_make_palindrome("aaa", 2))
    print(can_make_palindrome("add", 0))
    print(can_make_palindrome("waterrfetawx", 3))
    print(can_make_palindrome("waterrfetawx", 2))
    print(can_make_palindrome("waterrfetawx", 1))
    print(can_make_palindrome("malayalam", 0))
    print(can_make_palindrome("malayalam", 1))
    print(can_make_palindrome("asdf", 5))
    print(can_make_palindrome("asdf", 2))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(n)
"""
