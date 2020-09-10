"""
Problem:

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

# matplotlib is used to plt the distribution (not mandatory)
# randint is used to generate the random number
import matplotlib.pyplot as plt
from random import randint

# FUNCTION TO PERFORM THE OPERATION
def generate_num_not_in_data(n, data):
    # a random number is generated in the range [0, n-1]
    num = randint(0, n - 1)

    # if the number is not present in the supplied list, its returned; else the function is called recursively
    if num in data:
        return generate_num_not_in_data(n, data)

    return num


# DRIVER CODE
data = set([1, 3, 5])
results = {}

for i in range(100000):
    val = generate_num_not_in_data(7, data)

    if val in results:
        results[val] += 1
    else:
        results[val] = 1

x = []
y = []

for i in results:
    x.append(i)
    y.append(results[i])

plt.bar(x=x, height=y, edgecolor="black")
plt.show()
