"""
Problem:

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). 
You do not know the bias of the coin.
Write a function to simulate an unbiased coin toss.
"""

# library imports
# matplotlib is not mandatory, its used to plot the distribution of results
from random import randint
import matplotlib.pyplot as plt

# biased toss function
def toss_biased():
    # getting a random number between 1 to 100
    temp = randint(1, 100)

    # if the number is less than 30, 0 is returned else 1 (30-70 bias)
    if temp < 30:
        return 0
    else:
        return 1


# unbiased toss function
def toss_unbiased():
    # getting the biased toss value twice
    temp1 = toss_biased()
    temp2 = toss_biased()

    # as long as we dont get different values, we keep tossing
    while temp1 == temp2:
        temp1 = toss_biased()
        temp2 = toss_biased()

    # when different values are achieved, any 1 can be returned (here the 1st one is returned)
    return temp1


# DRIVER CODE
biased = [toss_biased() for i in range(100000)]
unbiased = [toss_unbiased() for i in range(100000)]

# displaying biased distribution
plt.title("Biased Distribution")
plt.hist(biased, bins=2, edgecolor="black")
plt.show()

# displaying unbiased distribution
plt.title("Unbiased Distribution")
plt.hist(unbiased, bins=2, edgecolor="black")
plt.show()
