"""
Problem:

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform
probability, implement a function rand5() that returns an integer from 1 to 5
(inclusive).
"""

from random import randint
import matplotlib.pyplot as plt


# rand7 implementation
def rand7() -> int:
    return randint(1, 7)


def rand5() -> int:
    val = rand7()
    if val <= 5:
        return val
    return rand5()


if __name__ == "__main__":
    values = []
    for i in range(100_000):
        values.append(rand5())
    plt.hist(values, bins=5, edgecolor="black")
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
