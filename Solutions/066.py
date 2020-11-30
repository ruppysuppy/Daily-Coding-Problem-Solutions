"""
Problem:

Assume you have access to a function toss_biased() which returns 0 or 1 with a
probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of
the coin.

Write a function to simulate an unbiased coin toss.
"""

from random import random
import matplotlib.pyplot as plt


def toss_biased():
    # toss with 30-70 bias
    value = random()
    if value < 0.3:
        return 0
    return 1


def toss_unbiased():
    # getting the biased toss value twice
    toss1 = toss_biased()
    toss2 = toss_biased()
    # as long as we dont get different values, we keep tossing
    while toss1 == toss2:
        toss1 = toss_biased()
        toss2 = toss_biased()
    return toss1


if __name__ == "__main__":
    biased = [toss_biased() for i in range(100_000)]
    unbiased = [toss_unbiased() for i in range(100_000)]

    # displaying biased distribution
    plt.title("Biased Distribution")
    plt.hist(biased, bins=2, edgecolor="black")
    plt.show()

    # displaying unbiased distribution
    plt.title("Unbiased Distribution")
    plt.hist(unbiased, bins=2, edgecolor="black")
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
[for toss_unbiased function]
"""
