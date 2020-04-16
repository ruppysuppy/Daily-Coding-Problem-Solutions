'''
Problem:

You are given n numbers as well as n probabilities that sum up to 1. 
Write a function to generate one of the numbers with its corresponding probability.
You can generate random numbers between 0 and 1 uniformly.

Example:

Input = [1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2] 
Output = your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
'''

from random import random
import matplotlib.pyplot as plt

class RandomGenerator:
    def __init__(self, numbers, probabilities):
        self.numbers = numbers
        self.probabilities = probabilities

    def generate(self):
        temp = random()
        cumulative = 0
        
        for pos in range(len(self.probabilities)):
            cumulative += self.probabilities[pos]

            if (cumulative >= temp):
                return self.numbers[pos]

generator = RandomGenerator([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])
res = []

for _ in range(1, 100000):
    res.append(generator.generate())

plt.hist(res)
plt.show()