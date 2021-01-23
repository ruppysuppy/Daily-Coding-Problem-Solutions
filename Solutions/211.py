"""
Problem:

Given a string and a pattern, find the starting indices of all occurrences of the
pattern in the string. For example, given the string "abracadabra" and the pattern
"abr", you should return [0, 7].
"""

from typing import List


def kmp_search(string: str, pattern: str) -> List[int]:
    pattern_length = len(pattern)
    string_length = len(string)
    lps = [0] * pattern_length
    result = []
    compute_lps(pattern, pattern_length, lps)

    j = 0
    i = 0
    while i < string_length:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        # entire pattern match
        if j == pattern_length:
            result.append(i - j)
            j = lps[j - 1]
        # mismatch after j positions
        elif i < string_length and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


def compute_lps(pattern: str, pattern_length: int, lps: List[int]) -> None:
    length = 0
    lps[0]
    i = 1
    while i < pattern_length:
        # match occours
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
            continue
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1


if __name__ == "__main__":
    print(kmp_search("abracadabra", "abr"))
    print(kmp_search("abracadabra", "xyz"))
    print(kmp_search("aaaa", "aa"))


"""
SPECS:

TIME COMPLEXITY: O(string_length + pattern_length)
SPACE COMPLEXITY: O(pattern_length)
"""
