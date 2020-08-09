"""
Problem:

Given a string of words delimited by spaces, reverse the words in string. 
Follow-up: given a mutable string representation, can you perform this operation in-place?

Example:

Input = "hello world here"
Output = "here world hello"
"""

# FUNCTION TO PERFORM THE OPERATION
def rev(string):
    # spilting the string into the words, reversing the list of words and joining the words with spaces
    return " ".join(string.split()[::-1])


# DRIVER CODE
print(rev("hello world here"))
