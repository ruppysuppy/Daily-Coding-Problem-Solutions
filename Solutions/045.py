"""
Problem:

You have a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability.
Implement a function rand7() that returns an integer from 1 to 7 (inclusive) using rand5().
"""

# Library Imports (matplotlib is not mandatory, it is used to plot the distribution of the generated random numbers from 1 to 7)
from random import randint

# You can either install matplotlib using 'pip install matplotlib' in CMD/Terminal/PowerShell
# or comment out any line containing 'plt'
import matplotlib.pyplot as plt

# rand5 function (returns a random number between 1 and 5 inclusive)
def rand5():
    return randint(1, 5)


# FUNCTION TO PERFORM THE OPERATION
def rand7():
    # Generating 2 numbers between 1 and 5
    temp1 = rand5()
    temp2 = rand5()

    # generating a number temp between 1 and 25
    temp = 5 * temp1 + temp2 - 5

    # if the number is NOT in the range[1, 21], rand7 is called and the result returned (as in 1 to 21, mod 7 yield all numbers from 0 to 6 with equal probability)
    # else (temp % 7) gives a number between 0 to 6, and the incremented result (range: 1 to 7) is returned
    if temp <= 21:
        return (temp % 7) + 1
    return rand7()


# This Section is just for displaying the distribution, it can be commented out
# result stores the result of the rand7 function
result = []

# Execution rand7 100000 times
for i in range(100000):
    result.append(rand7())

# Plotting the distribution
plt.hist(result, 7, edgecolor="black")
plt.show()
