"""
Problem:

Given a string, determine whether any permutation of it is a palindrome.

Example:

Input = carrace 
Output = true (since it can be rearranged to form racecar, which is a palindrome) 

Input = daily
Output = false (since there's no rearrangement that can form a palindrome)
"""

# FUNCTION TO PERFORM THE OPERATION
def palindrome_permutation(string):
    # creating a character set
    char_set = set()

    # iterating through the string
    for char in string:
        # deleting the charater upon encountering it again
        if char in char_set:
            char_set.remove(char)
        # adding the character to the set if its not present in the set
        else:
            char_set.add(char)

    # getting the number of elements in char_set
    length = len(char_set)

    # if the number of elements is 0 or 1, a palindrome permutation is possible
    if length == 1 or length == 0:
        return True
    else:
        return False


# DRIVER CODE
print(palindrome_permutation("carrace"))
print(palindrome_permutation("daily"))
