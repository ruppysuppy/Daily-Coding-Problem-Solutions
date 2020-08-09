"""
Problem 74:

Suppose you have a multiplication table that is N by N. 
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

Example:

N = 6, X = 12
Output = 4 (since the multiplication table looks like this:
1	2	3	4	5	6
2	4	6	8	10	12
3	6	9	12	15	18
4	8	12	16	20	24
5	10	15	20	25	30
6	12	18	24	30	36
And there are 4 12's in the table)
"""

# FUNCTION TO PERFORM THE OPERATION
def freq_calc(n, x):
    # count stores the number of times x appears
    count = 0

    # looping from 1 to n
    for i in range(1, n + 1):
        # looping from 1 to i
        for j in range(1, i + 1):
            # if the product is eual to x, the value of count has to be increased
            if i * j == x:
                # if the value of i and j are same (i * i = x, it will be considered once)
                if i == j:
                    count += 1
                # if the value of i and j are different (i * j = x implies j * i = x, it will be considered twice)
                else:
                    count += 2

    return count


# DRIVER CODE
print(freq_calc(6, 12))
print(freq_calc(1, 1))
print(freq_calc(2, 4))
print(freq_calc(3, 6))
