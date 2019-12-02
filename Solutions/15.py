'''
Problem:

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

# Library imports
from random import random, randint
import matplotlib.pyplot as plt 
# note to use matplotlib, you need to have it installed (run cmd as admin and run 'pip install matplotlib')

# Generator function to simulate a stream of elements too large to store in memory
def generator():
    while True:
        rand_float = random()
        yield int(10000 * rand_float)

# FUNCTION TO PERFORM THE OPERATION
def random_selector():
    # using the generator function (created globally)
    global gen

    # an array to store 10 elements
    arr = [0 for i in range(10)]
    
    # generating 10 elements (equivalent to getting 10 elements from the stream of elements)
    for i in range(10):
        arr[i] = next(gen)
    
    # selecting a random element from the array of 10 elements
    pos = randint(0, 9)
    return arr[pos]

# DRIVER CODE
# creating the generator
gen = generator()

# list of values to plot and check if the distribution is uniform
check = []

# populating the list
for i in range(100000):
    check.append(random_selector())

# plotting the histogram of frequencies of the elements
plt.hist(check, edgecolor="black")
plt.show()