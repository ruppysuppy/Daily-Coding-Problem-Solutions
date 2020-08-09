"""
Problem:

Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

Example:

"aabcdcb" => "bcdcb"
"bananas" => "anana"
"""

# Function to check if a string is a palindrome
def palindrome_check(string):
    return string == string[::-1]


# FUNCTION TO PERFORM THE OPERATION
def longest_palindrome_substring(string):
    # if the string is a palindrome, it is returned (BASE CASE FOR RECURSION)
    if palindrome_check(string):
        return string

    # string1 removes the 1st character in the string and calls the function recursively
    # string2 removes the last character in the string and calls the function recursively
    string1 = longest_palindrome_substring(string[1:])
    string2 = longest_palindrome_substring(string[:-1])

    # The longer palindromic substring is returned
    if len(string1) > len(string2):
        return string1
    else:
        return string2


# DRIVER CODE
print(longest_palindrome_substring("aabcdcb"))
print(longest_palindrome_substring("bananas"))
