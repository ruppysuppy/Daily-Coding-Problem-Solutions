"""
Problem:

Given a stream of elements too large to store in memory, pick a random element from the
stream with uniform probability.
"""

from random import randint
import matplotlib.pyplot as plt
from typing import Generator


def element_stream() -> Generator[int, None, None]:
    # generator function to simulate a stream of elements too large to store in memory
    while True:
        yield randint(1, 10_000)


def random_selector(generator: Generator[int, None, None]) -> int:
    # getting 10 elements from the stream of elements
    arr = [0 for i in range(10)]
    for i in range(10):
        arr[i] = next(generator)
    # selecting a random element from the array of 10 elements
    pos = randint(0, 9)
    return arr[pos]


if __name__ == "__main__":
    generator = element_stream()
    # storing the selected elements for plotting a graph
    values = []
    for i in range(100_000):
        values.append(random_selector(generator))
    # plotting the histogram of frequencies of the selected elements
    plt.hist(values, edgecolor="black")
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
