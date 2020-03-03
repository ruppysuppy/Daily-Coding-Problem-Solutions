'''
Problem:

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

Example:

Input = abcde, cdeab
Output = true

Input = abc, acb
Output = false
'''

# FUNCTION TO PERFORM THE OPERATION
def can_shift(str_A, str_B):
    # if the strings are not empty and have equal length, the returned value is whether B can be found in twice A (due to shifting)
    if ((str_A and str_B) and (len(str_A) == len(str_B))):
        return (str_B in (str_A * 2))
    
    # otherwise False is returned
    return False

# DRIVER CODE
print(can_shift("abcde", "cdeab"))
print(can_shift("abc", "acb"))