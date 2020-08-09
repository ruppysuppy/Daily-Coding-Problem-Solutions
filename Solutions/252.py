"""
Problem:

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
"""

from fractions import Fraction
from math import ceil


def get_egyptian_frac(frac, prev_frac=list()):
    # base case for recursion
    if frac.numerator == 1:
        prev_frac.append(frac)
        return prev_frac
    # generating the next fraction
    egyptian_frac = Fraction(1, ceil(frac.denominator / frac.numerator))
    prev_frac.append(egyptian_frac)
    # calling the function recursively
    return get_egyptian_frac(frac - egyptian_frac, prev_frac)


# DRIVER CODE
print(get_egyptian_frac(Fraction(4, 13)))
