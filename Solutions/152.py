"""
Problem:

You are given n numbers as well as n probabilities that sum up to 1. Write a function
to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of
the time.

You can generate random numbers between 0 and 1 uniformly.
"""

import matplotlib.pyplot as plt
from random import random
from typing import List


class RandomGenerator:
    def __init__(self, numbers: List[int], probabilities: List[float]) -> None:
        self.numbers = numbers
        self.probabilities = probabilities

    def generate(self) -> int:
        check = random()
        cumulative = 0
        for pos in range(len(self.probabilities)):
            cumulative += self.probabilities[pos]
            if cumulative >= check:
                return self.numbers[pos]


if __name__ == "__main__":
    generator = RandomGenerator([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
    nums = []
    for _ in range(1, 100_000):
        nums.append(generator.generate())
    plt.hist(nums)
    plt.show()
