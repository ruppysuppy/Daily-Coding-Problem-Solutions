"""
Problem:

Given an array of numbers and an index i, return the index of the nearest larger number
of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are equal, then return any one of them. If the array
at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""

from typing import Dict, List


def preprocess(arr: List[int]) -> Dict[int, int]:
    preprocessed_indices = {}
    length = len(arr)
    sorted_tuples = [(value, index) for index, value in enumerate(arr)]
    sorted_tuples.sort(key=lambda tup: tup[0])
    # generating the minimum distance index
    for k, (_, i) in enumerate(sorted_tuples[:-1]):
        min_dist = length
        for m in range(k + 1, length):
            dist_temp = abs(i - sorted_tuples[m][1])
            if dist_temp < min_dist:
                min_dist = dist_temp
                preprocessed_indices[i] = sorted_tuples[m][1]
    return preprocessed_indices


def nearest_larger_value_index(arr: List[int], index: int) -> int:
    preprocessed_indices = preprocess(arr)
    if index not in preprocessed_indices:
        return None
    return preprocessed_indices[index]


if __name__ == "__main__":
    print(nearest_larger_value_index([4, 1, 3, 5, 6], 0))
    print(nearest_larger_value_index([4, 1, 3, 5, 6], 1))
    print(nearest_larger_value_index([4, 1, 3, 5, 6], 4))
    print(nearest_larger_value_index([4, 1, 3, 5, 6], 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
[O(n ^ 2) is for preprocessing, after which it's complexity is O(1)]
"""
