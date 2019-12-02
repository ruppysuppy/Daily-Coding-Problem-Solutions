'''
Problem:

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
'''

# Library import (generate random numbers in [0, 1))
from random import random

# Helper function to generate a random coordinate in the square bounded by x=-1, x=1 and y=-1, y=1
def coordinate_gen():
    return (random(), random())

# FUNCTION TO PERFORM THE OPERATION
def pi_approx(iterations=1000000):
    # Circle area represents the number of points inside the circle
    circle_area = 0

    # Looping over a certain number of iterations and checking if the generated point is inside or outside the circle
    for _ in range(iterations):
        coordinate = coordinate_gen()

        if ((coordinate[0] ** 2 + coordinate[1] ** 2) <= 1):
            circle_area += 1
    
    # Using Monte Carlo approximation (pi = 4 x (Area of circle / Area of square)) 
    # [Area of circle = number of pts in circle, Area of square = total number of points]
    return (4*circle_area/iterations)

# DRIVER CODE
print("{:.3f}".format(pi_approx()))