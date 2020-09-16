"""
Problem:

Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""


def longest_substring_k_unique(string: str, k: int) -> str:
    length = len(string)
    # start and end is used to create the moving window (end - start)
    start = 0
    end = 1
    longest_substring_till_now = string[0]
    char_freq = {string[0]: 1}
    num_unique = 1

    while end < length:
        if string[end] in char_freq and char_freq[string[end]] != 0:
            char_freq[string[end]] += 1
        else:
            char_freq[string[end]] = 1
            num_unique += 1
            # updating moving window
            if num_unique > k:
                while num_unique > k:
                    char_freq[string[start]] -= 1
                    if char_freq[string[start]] == 0:
                        num_unique -= 1
                    start += 1
        # updating the longest substring
        temp = string[start : end + 1]
        if num_unique <= k and len(temp) > len(longest_substring_till_now):
            longest_substring_till_now = temp
        end += 1
    return longest_substring_till_now


if __name__ == "__main__":
    print(longest_substring_k_unique("abcba", 2))
    print(longest_substring_k_unique("abcba", 20))
    print(longest_substring_k_unique("karappa", 2))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
