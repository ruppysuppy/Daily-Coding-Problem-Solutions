"""
Problem:

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the other.
For example, the edit distance between "kitten" and "sitting" is three: substitute the
"k" for "s", substitute the "e" for "i", and append a "g".

Given two strings, compute the edit distance between them.
"""


def get_string_distance(str1: str, str2: str) -> int:
    n = len(str1)
    m = len(str2)
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)]
    # generating the look-up table in bottom up manner
    for i in range(n + 1):
        for j in range(m + 1):
            # str1 empty (insert all characters of second string)
            if i == 0:
                dp[i][j] = j
            # str2 empty (remove all characters of second string)
            elif j == 0:
                dp[i][j] = i
            # last characters are same (ignore last char and recurse for remaining
            # string)
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # last character are different (consider all possibilities and select the
            # minimum)
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],       # insertion
                    dp[i - 1][j],       # deletion
                    dp[i - 1][j - 1],   # replacement
                )
    return dp[n][m]


if __name__ == "__main__":
    print(get_string_distance("kitten", "sitting"))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
