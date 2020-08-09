"""
Problem:

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

Example:

Input = ["code", "edoc", "da", "d"]
Output = [(0, 1), (1, 0), (2, 3)]
"""

# functio to check if a string is palindrome
def palindrome_check(string):
    return string == string[::-1]


# FUNCTION TO PERFORM THE OPERATION
def get_all_concatenated_palindrome(string_list):
    # res stores the result
    res = []
    # getting the length of the string
    length = len(string_list)

    # iterating through the array
    for i in range(length):
        # checking for all combinations (brute force)
        for j in range(i + 1, length):
            # checking if the concatination yields a palindrome and adding the indices to the result array
            if palindrome_check(string_list[i] + string_list[j]):
                res.append((i, j))
            if palindrome_check(string_list[j] + string_list[i]):
                res.append((j, i))

    return res


# DRIVER CODE
print(get_all_concatenated_palindrome(["code", "edoc", "da", "d"]))
