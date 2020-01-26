'''
Problem:

A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.

Example:

Input = 1
Output = 19

Input = 2
Output = 28
'''

# NOTE: I found several methods to perform the operation, but none of them work properly as the number grows larger
# Only the naive approach works properly for all numbers (but its painfully slow)

# importing log10
from math import log10

# my approach to solve the problem
def nth_perfect_num_mine(n):
    num = 19 + (9 * (n-1))
    outliers = n // 10
    num += (9 * outliers)

    return num

# method 1 to solve the problem
def nth_perfect_num_1(n):
    num = 19 + (9 * (n-1))
    outliers = int(log10(num)) - 1
    num += (9 * outliers)

    return num

# method 2 to solve the problem
def nth_perfect_num_2(n):
    tmp_sum = 0
    for char in str(n):
        tmp_sum += int(char)

    return (n * 10) + (10 - tmp_sum)

# function to calculate the sum of the digits of a number (takes string as input as its easier to parse)
def calc_sum(num):
    s = 0
    for i in num:
        s += int(i)
    return s

# naive approach to solve the problem
def nth_perfect_num_naive(n):
    # starting with default value of 19 for number & 1 for count
    num = 19
    count = 1

    # looping till we find n perfect numbers
    while (n > count):
        # incrementing num (to get the next number)
        num += 1

        # if the number is perfect, count is incremented
        if (calc_sum(str(num)) == 10):
            count += 1
    
    # finally the number is returned on loop termination
    return num

# displaying the error percent for my method
count = 0
for i in range(1, 500):
    num = calc_sum(str(nth_perfect_num_mine(i)))
    if (num != 10):
        count += 1
print('Errors (my method):\t[', count, ']', (count / 5), '%')

# displaying the error percent for method 1
count = 0
for i in range(1, 500):
    num = calc_sum(str(nth_perfect_num_1(i)))
    if (num != 10):
        count += 1
print('Errors (method 1):\t[', count, ']', (count / 5), '%')

# displaying the error percent for method 2
count = 0
for i in range(1, 500):
    num = calc_sum(str(nth_perfect_num_2(i)))
    if (num != 10):
        count += 1
print('Errors (method 2):\t[', count, ']', (count / 5), '%')

# displaying the error percent for method naive
count = 0
for i in range(1, 500):
    num = calc_sum(str(nth_perfect_num_naive(i)))
    if (num != 10):
        count += 1
print('Errors (naive): \t[', count, ']', (count / 5), '%')
