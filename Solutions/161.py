'''
Problem:

Given a 32-bit integer, return the number with its bits reversed.

Example:

Input = 1111 0000 1111 0000 1111 0000 1111 0000
Output = 0000 1111 0000 1111 0000 1111 0000 1111
'''

# FUNCTION TO PERFORM THE OPERATION
def complement_1s(num):
    # res stores the resultant number
    res = ""

    # iterating through the number and getting each digit
    for i in num:
        # inverting the number and adding it to the result
        res += str(int(not int(i)))
    
    # returning the result
    return res

# DRIVER CODE
print(complement_1s("11110000111100001111000011110000"))