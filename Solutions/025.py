"""
Problem:

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element That is, implement a
function that takes in a string and a valid regular expression and returns whether or
not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function
should return true. The same regular expression on the string "raymond" should return
false.

Given the regular expression ".*at" and the string "chat", your function should return
true. The same regular expression on the string "chats" should return false.
"""


def is_regex_match(pattern: str, text: str) -> bool:
    n, m = len(text), len(pattern)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    # populating the 1st row of the lookup table
    for i in range(1, m + 1):
        if pattern[i - 1] == "*":
            dp[0][i] = dp[0][i - 2]
    # populating the remaining lookup table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == "." or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if pattern[j - 2] == "." or pattern[j - 2] == text[i - 1]:
                    dp[i][j] = dp[i][j] | dp[i - 1][j]
    return dp[n][m]


if __name__ == "__main__":
    print(is_regex_match("r.y", "ray"))
    print(is_regex_match("ra.", "rays"))
    print(is_regex_match(".*at", "chat"))
    print(is_regex_match(".*at", "chats"))
    print(is_regex_match(".*", "random-word"))
    print(is_regex_match(".*a", "random-word"))


"""
SPECS:

TIME COMPLEXITY: O(n x m)
SPACE COMPLEXITY: O(n x m)
"""
