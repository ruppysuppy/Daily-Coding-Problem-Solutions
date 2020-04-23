'''
Problem:

Given a string, return the first recurring character in it, or null if there is no recurring chracter.

Example:

Input = "acbbac"
Output = "b"

Input = "abcdef"
Output = null
'''

# FUNCTION TO PERFORM THE OPERATION
def get_first_recurring(string):
    # seen set to hold the previously seen characters
    seen = set()

    # iterating through the string
    for char in string:
        # if a previously seen character is encountered, its returned
        if (char in seen):
            return char
        
        # the current character is added to the set
        seen.add(char)

    # if there is no recurring character, None is returned
    return None

# DRIVER CODE
print(get_first_recurring("acbbac"))
print(get_first_recurring("abcdef"))