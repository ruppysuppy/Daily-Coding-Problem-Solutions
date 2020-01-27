'''
Problem:

You have a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability.
Implement a function rand5() that returns an integer from 1 to 5 (inclusive).
'''

# library imports (pyplot is not mandatory, its used to plot the distribution)
from random import randint
import matplotlib.pyplot as plt

# rand7 function
def rand7():
    return randint(1, 7)

# rand5 function
def rand5():
    # generating a random number between 1 to 7
    val = rand7()
    # if the generated number is in the range [1, 5], its returned
    if (val <= 5):
        return val
    # if the number is outside the range, rand5 is called again recursively
    return rand5()

# code to plot the distribution by generating 10000 numbers
res = []

for i in range(10000):
    res.append(rand5())

plt.hist(res, bins=5, edgecolor='black')
plt.show()