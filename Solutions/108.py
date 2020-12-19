"""
Problem:

Given two strings A and B, return whether or not A can be shifted some number of times
to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb,
return false.
"""


def can_shift(A: str, B: str) -> bool:
    return (A and B) and (len(A) == len(B)) and (B in A * 2)


if __name__ == "__main__":
    print(can_shift("abcde", "cdeab"))
    print(can_shift("abc", "acb"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
