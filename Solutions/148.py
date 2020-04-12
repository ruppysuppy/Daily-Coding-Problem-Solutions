'''
Problem:

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. 
Gray code is common in hardware so that we don't see temporary spurious values during transitions.
Given a number of bits n, generate a possible gray code for it.

Example:

Input = 2
Output = [00, 01, 11, 10]
'''

# FUNCTION TO PERFORM THE OPERATION
def grey_code_gen(n):
    # if n is 0, a list with an empty string is returned (base case for recursion)
    if (n == 0):
        return ['']
    
    # getting the numbers for n-1 digits
    get_prev_GC = grey_code_gen(n-1)

    # getting the numbers where the first digit is 0 and 1 respectively
    base0 = ['0' + val for val in get_prev_GC]
    base1 = ['1' + val for val in get_prev_GC[::-1]]

    # returning the concatinated list
    return base0 + base1

# DRIVER CODE
print(grey_code_gen(0))
print(grey_code_gen(1))
print(grey_code_gen(2))
print(grey_code_gen(3))
print(grey_code_gen(4))