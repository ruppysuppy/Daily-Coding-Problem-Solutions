"""
Problem:

Determine whether there exists a one-to-one character mapping from one string s1 to
another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c
and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""


def check(s1: str, s2: str) -> bool:
    l1, l2 = len(s1), len(s2)
    # checking if each character in s1 maps to 1 character in s2
    d = {}
    for i in range(l1):
        if s1[i] in d and d[s1[i]] != s2[i]:
            return False
        d[s1[i]] = s2[i]
    # checking if each character in s2 maps to 1 character in s1
    d = {}
    for i in range(l2):
        if s2[i] in d and d[s2[i]] != s1[i]:
            return False
        d[s2[i]] = s1[i]
    return True


if __name__ == "__main__":
    print(check("abc", "bcd"))
    print(check("abc", "foo"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
[n = number of characters in the strings]
"""
