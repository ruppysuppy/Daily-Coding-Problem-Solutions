"""
Problem:

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle
numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

from typing import List


from DataStructures.Heap import MaxHeap, MinHeap


def get_running_medians(arr: List[int]) -> List[int]:
    min_heap = MinHeap()
    max_heap = MaxHeap()
    medians = []
    for elem in arr:
        # current median value generation
        min_heap.insert(elem)
        if len(min_heap) > len(max_heap) + 1:
            smallest_large_element = min_heap.extract_min()
            max_heap.insert(smallest_large_element)
        if len(min_heap) == len(max_heap):
            median = (min_heap.peek_min() + max_heap.peek_max()) / 2
        else:
            median = min_heap.peek_min()
        medians.append(median)
    return medians


if __name__ == "__main__":
    print(get_running_medians([]))
    print(get_running_medians([2, 5]))
    print(get_running_medians([3, 3, 3, 3]))
    print(get_running_medians([2, 1, 5, 7, 2, 0, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
"""
