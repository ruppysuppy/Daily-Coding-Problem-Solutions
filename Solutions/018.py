"""
Problem:

Given an array of integers and a number k, where 1 <= k <= length of the array, compute
the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8],
since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do
not need to store the results. You can simply print them out as you compute them.
"""

from collections import deque
from typing import List


def calc_max_per_k_elems(arr: List[int], k: int) -> List[int]:
    length = len(arr)
    if not arr:
        return None
    if length <= k:
        return max(arr)
    # storing results (even though the problem states it can be directly printed)
    result = []
    dq = deque()
    # calculating the 1st element
    for i in range(k):
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
    result.append(arr[dq[0]])
    # generating the rest of the resultant elements
    for i in range(k, length):
        # removing all elements apart from the last k elements
        while dq and dq[0] <= i - k:
            dq.popleft()
        # removing the elements smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        result.append(arr[dq[0]])
    return result


if __name__ == "__main__":
    print(calc_max_per_k_elems([10, 5, 2, 7, 8, 7], 3))
    print(calc_max_per_k_elems([1, 91, 17, 46, 45, 36, 9], 3))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(k)
"""
