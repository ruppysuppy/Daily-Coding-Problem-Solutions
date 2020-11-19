"""
Problem:

The area of a circle is defined as r^2. Estimate pi to 3 decimal places using a Monte
Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

from random import random
from typing import Tuple


def coordinate_gen() -> Tuple[float, float]:
    # Helper function to generate a random coordinate in the square bounded by
    # x = -1, x = 1 and y = -1, y = 1
    return random(), random()


def pi_approx(iterations: int = 1_000_000) -> float:
    circle_area = 0
    for _ in range(iterations):
        x, y = coordinate_gen()
        if pow(x, 2) + pow(y, 2) <= 1:
            circle_area += 1
    # Using Monte Carlo approximation [pi = 4 x (Area of circle / Area of square)]
    # [Area of circle = number of points in circle,
    #  Area of square = total number of points]
    return round(4 * circle_area / iterations, 3)


if __name__ == "__main__":
    print(pi_approx())


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
