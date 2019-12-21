'''
Problem:

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

Example:
"race" => "ecarace"
"google" => "elgoogle"
'''

# FUNCTION TO PERFORM THE OPERATION
def nearest_palindrome(string):
    # Getting the length of the string
    length = len(string)

    # if the passed string is already a palindrome, the string is returned
    if (string[::-1] == string):
        return string

    # if the first and last characters are same, the function is called recursively on the string without the first and last charater
    # this is allowed as insertion anywhere in the word is allowed
    if (string[0] == string[-1]):
        return (string[0] + nearest_palindrome(string[1:length-1]) + string[0])
    
    else:
        # if the first and last characters are different, the resultant strings are calculated by adding the 1st character (pal_1) and last charcter (pal_2)
        pal_1 = string[0] + nearest_palindrome(string[1:]) + string[0]
        pal_2 = string[-1] + nearest_palindrome(string[:length-1]) + string[-1]
        
        # if one of the string is shorter, it is returned
        if (len(pal_1) > len(pal_2)):
            return pal_2
        elif (len(pal_1) < len(pal_2)):
            return pal_1

        # if both strings have the same length, the lexicographically earliest one is returned
        if (pal_1 < pal_2):
            return pal_1
        else:
            return pal_2

# DRIVER CODE
print(nearest_palindrome("race"))
print(nearest_palindrome("google"))