'''
Problem:

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
'''

# Predefined
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implementation of the function 'car'
def car(f):
    z = lambda x, y: x
    return f(z)

# Implementation of the function 'cdr'
def cdr(f):
    z = lambda x, y: y
    return f(z)

# DRIVER CODE
temp = cons(1, 3)

print(car(temp))
print(cdr(temp))