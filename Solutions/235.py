'''
Problem:

Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.
'''


def getMinMax(arr):
    if (not arr):
        return (None, None)

    length = len(arr)

    if (length % 2 == 0):
        max_elem = max(arr[0], arr[1])
        min_elem = min(arr[0], arr[1])
        start = 2
    else:
        max_elem = min_elem = arr[0]
        start = 1

    for i in range(start, length, 2):
        # reducing the number of comparisons by comparing the array elements with
        # themselves and then comparing the larger with max_elem and smaller with
        # min_elem (effective comparison = 3 for every 2 elements)
        if (arr[i] < arr[i + 1]):
            max_elem = max(max_elem, arr[i + 1])
            min_elem = min(min_elem, arr[i])
        else:
            max_elem = max(max_elem, arr[i])
            min_elem = min(min_elem, arr[i + 1])

    return (min_elem, max_elem) 


print(getMinMax([1000, 11, 445, 1, 330, 3000]))
print(getMinMax([1000, 11, 445, 1, -330]))