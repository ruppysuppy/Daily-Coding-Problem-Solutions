'''
Problem:

Implement division of two positive integers without using the division, multiplication, or modulus operators. 
Return the quotient as an integer, ignoring the remainder.
'''

# FUNCTION TO PERFORM THE OPERATION
def div(dividend, divisor):
    # if the divisor is 0, division is not possible
    if (divisor == 0):
        return None
    
    # quotient stores the result of the division
    quotient = 0

    # while the dividend is larger than 0, it might be divided my the divisor
    while (dividend > 0):
        # divisor is subtracted from the dividend
        dividend -= divisor

        # if the dividend is still larger than 0, the quotient is incremented
        if (dividend >= 0):
            quotient += 1
    
    # the quotient is returned
    return quotient

# DRIVER CODE
print(div(1, 0))
print(div(1, 1))
print(div(0, 1))
print(div(12, 3))
print(div(13, 3))
print(div(25, 5))
print(div(25, 7))