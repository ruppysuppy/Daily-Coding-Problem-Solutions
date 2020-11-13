"""
Problem:

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last
element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4))
returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
"""

from typing import Callable


# given implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# car implementation
def car(f: Callable) -> int:
    z = lambda x, y: x
    return f(z)


# cdr implementation
def cdr(f: Callable) -> int:
    z = lambda x, y: y
    return f(z)


if __name__ == "__main__":
    pair = cons(1, 3)

    print(car(pair))
    print(cdr(pair))


"""
SPECS:

car:
TIME COMPLEXITY: O(1) 
SPACE COMPLEXITY: O(1)

cdr:
TIME COMPLEXITY: O(1) 
SPACE COMPLEXITY: O(1)
"""
