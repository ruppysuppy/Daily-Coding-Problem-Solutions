"""
Problem:

You are given a list of N numbers, in which each number is located at most k places
away from its sorted position. For example, if k = 1, a given element at index 4 might
end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
"""

from typing import List

from DataStructures.Heap import MinHeap


def k_sort(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    heap = MinHeap()
    [heap.insert(elem) for elem in arr[: k + 1]]
    # updating the values of the array (to hold sorted elements)
    curr_index = 0
    for index in range(k + 1, length):
        arr[curr_index] = heap.extract_min()
        heap.insert(arr[index])
        curr_index += 1
    # updating the last k positions in the array by emptying the heap
    while heap:
        arr[curr_index] = heap.extract_min()
        curr_index += 1
    return arr


if __name__ == "__main__":
    print(k_sort([1, 0, 2, 4, 3], 2))
    print(k_sort([6, 5, 3, 2, 8, 10, 9], 3))
    print(k_sort([10, 9, 8, 7, 4, 70, 60, 50], 4))


"""
SPECS:

TIME COMPLEXITY: O(n log(k))
SPACE COMPLEXITY: O(k)
"""
