'''
Problem:

You have 100 fair coins and you flip them all at the same time. 
Any that come up tails you set aside. The ones that come up heads you flip again. 
How many rounds do you expect to play before only one coin remains?
Write a function that, given 'n', returns the number of rounds you'd expect to play until one coin remains.
'''

# imports from the math module
from math import log2, ceil

# FUNCTION TO PERFORM THE OPERATION
def expectation(n):
    # since the number of coins is expected (mean) to be halved on each toss, we use log2
    # ceil is used to round it off to the next larger integer as number of tosses cannot be a fraction
    return ceil(log2(n))

# DRIVER CODE
print(expectation(1))
print(expectation(2))
print(expectation(100))
print(expectation(200))