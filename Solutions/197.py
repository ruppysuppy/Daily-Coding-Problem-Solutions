"""
Problem:

Given an array and a number k that's smaller than the length of the array, rotate the
array to the right k elements in-place.
"""

from typing import List


def rotate_array_right(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    k = k % length
    # rotating array
    if k > 0:
        cache = arr[-k:]
        for i in range(length - k - 1, -1, -1):
            arr[k + i] = arr[i]
        arr[:k] = cache
    return arr


def rotate_array_right_optimized(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    k = k % length
    if k > 0:
        iteration_start_idx = 0
        moves_remaining = length
        while moves_remaining:
            # Rotate the element at iteration_start_idx, and every kth element thereafter including looping around as needed, k places right
            # First, memorize the element at iteration_start_idx
            iteration_start_elem = arr[iteration_start_idx]
            curr_idx = (iteration_start_idx - k) % length
            # Rotate the appropriate element into its place...then one into that one's place...etc.
            while curr_idx != iteration_start_idx:
                arr[(curr_idx + k) % length] = arr[curr_idx]
                moves_remaining -= 1
                curr_idx -= k
                curr_idx %= length
            # Finally, place the element origianlly at iteration_start_idx in its appropriate new location
            arr[(iteration_start_idx + k) % length] = iteration_start_elem
            moves_remaining -= 1
            # Move onto the next group of length/gcd(length, k) elements
            iteration_start_idx += 1
    return arr


if __name__ == "__main__":
    for arr, k in [
        ([(i + 1) for i in range(5)], 9),
        ([(i + 1) for i in range(5)], 3),
        ([(i + 1) for i in range(5)], 2),
        ([(i + 1) for i in range(5)], 1),
        ([(i + 1) for i in range(5)], 0),
        ([(i + 1) for i in range(5)], 5),
        ([(i + 1) for i in range(10)], 4),
        ([(i + 1) for i in range(15)], 4),
    ]:
        arr_copy = arr[:]
        print(rotate_array_right(arr, k))
        print(rotate_array_right_optimized(arr_copy, k))


"""
SPECS:

rotate_array_right:
TIME COMPLEXITY: originally said O(n ^ 2); in fact seeems O(n)
SPACE COMPLEXITY: O(n)

rotate_array_right_optimized:
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) (auxiliary)
"""
