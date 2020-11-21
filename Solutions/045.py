"""
Problem:

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform
probability, implement a function rand7() that returns an integer from 1 to 7
(inclusive).
"""

from random import randint
import matplotlib.pyplot as plt

# rand5 implementation
def rand5() -> int:
    return randint(1, 5)


def rand7() -> int:
    # generating 2 numbers between 1 and 5
    temp1 = rand5()
    temp2 = rand5()
    # generating a number temp between 1 and 25
    temp = 5 * temp1 + temp2 - 5
    # if the number is NOT in the range[1, 21], rand7 is called again
    # mod 7 over 1 to 21, yield all numbers from 0 to 6 with EQUAL probability
    if temp <= 21:
        return (temp % 7) + 1
    return rand7()


if __name__ == "__main__":
    results = []
    # executing rand7 100,000 times (for plotting on a graph)
    for _ in range(100_000):
        results.append(rand7())
    # plotting the distribution
    plt.hist(results, 7, edgecolor="black")
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
