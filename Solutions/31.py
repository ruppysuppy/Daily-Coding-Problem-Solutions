'''
Problem:

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
Given two strings, compute the edit distance between them.

Example:

Input = “kitten”, “sitting”
Output = 3
'''

# FUNCTION TO PERFORM THE OPERATION
def string_distance(str1, str2):
    # if the strings are same, the distance between the strings is 0 [BASE CASE FOR RECURSION]
    if (str1 == str2):
        return 0
    # if str1 is an empty string, distance is length of str2 (len(str2) characters have to be inserted) [BASE CASE FOR RECURSION]
    elif (not str1):
        return len(str2)
    # if str2 is an empty string, distance is length of str1 (len(str1) characters have to be inserted) [BASE CASE FOR RECURSION]
    elif (not str2):
        return len(str1)

    # if the 1st character are the same for both strings
    if (str1[0] == str2[0]):
        return string_distance(str1[1:], str2[1:])

    # if the 1st character are different, we choose the minimum distance for 1st character deletion, addition and modifying the charcter + 1 (due to the change in the character)
    return 1 + min(
        string_distance(str1[1:], str2),      # deletion from str1
        string_distance(str1, str2[1:]),      # addition to str1
        string_distance(str1[1:], str2[1:]))  # modification to str1

# DRIVER CODE
print(string_distance('kitten', 'sitting'))