'''
Problem:

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.

Example:
2, 10 => 1024
'''

# FUNCTION TO PERFORM THE OPERATION
def pow(base, power):
    # this function implements a method similar to binary search, the effective complexity is O(log(n))
    # base case [x^0 = 1]
    if (power == 0):
        return 1
    # if the exponent is odd, the result is given by [base ^ exp = ((base * base) ^ floor(exp / 2)) * base]
    elif (power % 2 != 0):
        return (pow((base*base), power//2) * base)
    # if the exponent is even, the result is given by [base ^ exp = (base * base) ^ floor(exp / 2)]
    else:
        return pow((base*base), power//2)

# DRIVER CODE
print(pow(2, 10))
print(pow(3, 4))