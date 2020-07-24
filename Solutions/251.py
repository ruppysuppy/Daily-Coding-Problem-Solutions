'''
Problem:

Given an array of a million integers between zero and a billion, out of order, how can you efficiently sort it?
Assume that you cannot store an array of a billion elements in memory.
'''

from random import randint


def gen_arr():
    # function to generate the required array
    return [randint(0, 1_000_000_000) for _ in range(1_000_000)]


def countingSort(arr, exp, n):
    # output array elements to store the sorted arr
    output = [0] * n
    count = [0] * 10
    # updating count
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    # genrating the output array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    # updating arr with output arr
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort 
def radixSort(arr):
    length = len(arr)
    # find the number digits in the largest number (generalized for any array)
    digits = len(str(max(arr)))
    # perform counting sort for every digit
    exp = 1
    for _ in range(digits):
        countingSort(arr, exp, length)
        exp *= 10


# DRIVER CODE
radixSort(gen_arr())
