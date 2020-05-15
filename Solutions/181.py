'''
Problem:

Given a string, split it into as few strings as possible such that each string is a palindrome.

Example:

Input = "racecarannakayak"
Output = ["racecar", "anna", "kayak"]

Input = "abc"
Output = ["a", "b", "c"]
'''

# function to check if a string is palindrome
def is_palindrome(string):
    return (string and string == string[::-1])

# helper function to perform the computations
def split_into_strings_helper(string, current, previous):
    # base cases for recursion

    # the entire string has been partitioned into palindromes 
    # (previous contains the last palindrome)
    if (not string and not current):
        return previous
    # the string has been exhausted, but could not obtain a palindrome using the last characters 
    # (each character in the string is used as a palindrome)
    elif (not string):
        return previous + list(current)

    # generating temp
    temp = current + string[0]

    # checking if temp is a palindrome
    if (is_palindrome(temp)):
        # adding temp to the list of palindromes
        temp_arr_1 = split_into_strings_helper(string[1:], "", previous + [temp])
        # checking if a larger palindrome can be obtained
        temp_arr_2 = split_into_strings_helper(string[1:], temp, previous)

        # returning the shorter list
        return min(temp_arr_1, temp_arr_2, key=lambda List: len(List))
    
    # if the temp is not a palindrome, the search for a palindrome continues
    else:
        return split_into_strings_helper(string[1:], temp, previous)

# FUNCTION TO PERFORM THE OPERATION
def split_into_strings(string):
    # calling the helper function
    return split_into_strings_helper(string, "", [])

# DRIVER CODE
print(split_into_strings("racecarannakayak"))
print(split_into_strings("abc"))
print(split_into_strings("abbbc"))