"""
Problem:

The ancient Egyptians used to express fractions as a sum of several terms where each
numerator is one. For example, 4 / 13 can be represented as
1 / (4 + 1 / (18 + (1 / 468))).

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian
fraction.
"""

from fractions import Fraction
from math import ceil
from typing import List


def get_egyptian_frac(
    fraction: Fraction, previous_fraction: List[Fraction] = list()
) -> List[Fraction]:
    if fraction.numerator == 1:
        previous_fraction.append(fraction)
        return previous_fraction

    egyptian_fraction = Fraction(1, ceil(fraction.denominator / fraction.numerator))
    previous_fraction.append(egyptian_fraction)
    return get_egyptian_frac(fraction - egyptian_fraction, previous_fraction)


if __name__ == "__main__":
    print(get_egyptian_frac(Fraction(4, 13)))


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(log(n))
"""
