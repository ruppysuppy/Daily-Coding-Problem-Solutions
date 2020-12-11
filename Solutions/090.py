"""
Problem:

Given an integer n and a list of integers l, write a function that randomly generates a
number from 0 to n-1 that isn't in l (uniform).
"""

import matplotlib.pyplot as plt
from random import randint
from typing import List


def generate_num_not_in_data(n: int, data: List[int]) -> int:
    num = randint(0, n - 1)
    if num in data:
        return generate_num_not_in_data(n, data)
    return num


if __name__ == "__main__":
    data = [1, 3, 5]
    results = {}
    for i in range(100_000):
        val = generate_num_not_in_data(7, data)
        if val in results:
            results[val] += 1
        else:
            results[val] = 1

    x, y = [], []
    for i in results:
        x.append(i)
        y.append(results[i])
    plt.bar(x=x, height=y, edgecolor="black")
    plt.show()


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
