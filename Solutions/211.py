"""
Problem:

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. 

Example:

String = "abracadabra"
Pattern = "abr"
Output = [0, 7]
"""

# FUNCTION TO PERFORM THE OPERATION
def KMPSearch(string, pattern):
    # using KMP algorithm for pattern matching
    # getting the length of the pattern and the string
    patten_length = len(pattern)
    string_length = len(string)
    # array to hold the longest prefix suffix values for pattern
    lps = [0] * patten_length
    # array to store the results
    result = []

    j = 0  # index for patten
    i = 0  # index for string

    # preprocessing the pattern (computing the lps array)
    compute_LPS(pattern, patten_length, lps)

    # iterating through the string
    while i < string_length:
        # if match occours i & j are incremented
        if pattern[j] == string[i]:
            i += 1
            j += 1

        # if the entire pattern matches
        if j == patten_length:
            # adding the position to result & going back to the required location
            # (based upon the pre-processed array)
            result.append(i - j)
            j = lps[j - 1]

        # mismatch after j matches
        elif i < string_length and pattern[j] != string[i]:
            # going back to the required location (based upon the pre-processed array) or incrementing i
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    # returning the result
    return result


# helper function to pre-process the array
def compute_LPS(pattern, patten_length, lps):
    # length of the previous longest prefix suffix (initialized as 0)
    length = 0
    # lps[0] is always 0
    lps[0]
    # index for patten
    i = 1

    # generating the lps array
    while i < patten_length:
        # match occours
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        # match doesn't occour
        else:
            # if the prefix match is postive its updated to the previous value in lps
            if length != 0:
                length = lps[length - 1]
            # if prefix match is 0, lps for the value is set to 0 and i incremented
            else:
                lps[i] = 0
                i += 1


# DRIVER CODE
print(KMPSearch("abracadabra", "abr"))
print(KMPSearch("abracadabra", "xyz"))
print(KMPSearch("aaaa", "aa"))
