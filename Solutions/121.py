'''
Problem:

Given a string which we can delete at most k, return whether you can make a palindrome.

Example:

Input = 'waterrfetawx', 2
Output = True ('f' and 'x  can be deleted to yield 'waterretaw')
'''

# function to check if a string is palindrome
def is_palindrome(string):
    return (string == string[::-1])

# FUNCTION TO PERFORM THE OPERATION
def can_make_palindrome(string, k):
    # base case 1 for recursion: if the string is a palindrome, True is returned
    if (is_palindrome(string)):
        return True
    
    # base case 2 for recursion: if k = 0, False is returned
    if (not k):
        return False
    
    # iterating over the string
    for i in range(len(string)):
        # testing all string if they are palindrome (eleminating the i'th character) 
        # recursively called function, so all possible combinations of removing k characters will be found till one is palindrome
        # if a palindrome is encountered, True is returned
        if (can_make_palindrome(string[:i] + string[i+1:], k-1)):
            return True
    
    # if no palindrome can be formed, False is returned
    return False

# DRIVER CODE
print(can_make_palindrome("a", 0))
print(can_make_palindrome("aaa", 2))
print(can_make_palindrome("add", 0))
print(can_make_palindrome("waterrfetawx", 3))
print(can_make_palindrome("waterrfetawx", 2))
print(can_make_palindrome("waterrfetawx", 1))
print(can_make_palindrome("malayalam", 0))
print(can_make_palindrome("malayalam", 1))
print(can_make_palindrome("asdf", 5))
print(can_make_palindrome("asdf", 2))