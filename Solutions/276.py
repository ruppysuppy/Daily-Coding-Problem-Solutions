"""
Problem:

Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k, write a program that
searches for the pattern in the string with less than O(N * k) worst-case time
complexity.

If the pattern is found, return the start index of its location. If not, return False.
"""

from typing import List, Union


def kmp_search(text: str, pattern: str) -> Union[int, bool]:
    # modified kmp search to return the first match only
    len_pattern = len(pattern)
    len_text = len(text)
    lps = compute_lps(pattern, len_pattern)

    j = 0
    i = 0
    while i < len_text:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len_pattern:
                return i - j
        elif i < len_text and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def compute_lps(pattern: str, len_pattern: int) -> List[int]:
    # computing the Longest Prefix which is also a Suffix
    lps = [0 for _ in range(len_pattern)]
    length = 0
    i = 1
    while i < (len_pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
        else:
            lps[i] = length
        i += 1
    return lps


if __name__ == "__main__":
    print(kmp_search("abcabcabcd", "abcd"))
    print(kmp_search("abcabcabc", "abcd"))


"""
SPECS:

[n = length of text, m = length of pattern]
TIME COMPLEXITY: O(n + m)
SPACE COMPLEXITY: O(m)
"""
