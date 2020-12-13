"""
Problem:

Given a number represented by a list of digits, find the next greater permutation of a
number, in terms of lexicographic ordering. If there is not greater permutation
possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return
[2,1,3]. The list [3,2,1] should return [1,2,3]

Can you perform the operation without allocating extra memory (disregarding the input
memory)?
"""

from typing import List


def get_next(arr: List[int]) -> List[int]:
    length = len(arr)
    if length < 2:
        return arr
    # finding the last element arranged in ascending order
    for index in range(length - 1, -1, -1):
        if index > 0 and arr[index - 1] < arr[index]:
            break
    # if index is 0, arr is sorted in descending order
    if index == 0:
        arr.reverse()
        return arr
    # finding the next permutation
    for k in range(length - 1, index - 1, -1):
        if arr[k] > arr[index - 1]:
            arr[k], arr[index - 1] = arr[index - 1], arr[k]
            break
    # arranging the other elements in proper order
    size = (length - 1) + index
    for i in range(index, (size + 1) // 2):
        arr[i], arr[size - i] = arr[size - i], arr[i]
    return arr


if __name__ == "__main__":
    print(get_next([1, 2, 3]))
    print(get_next([1, 3, 2]))
    print(get_next([2, 1, 3]))
    print(get_next([2, 3, 1]))
    print(get_next([3, 1, 2]))
    print(get_next([3, 2, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
