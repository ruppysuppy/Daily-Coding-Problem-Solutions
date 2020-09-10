"""
Problem:

Pascal's triangle is a triangular array of integers constructed with the following
formula:

The first row consists of the number 1. For each subsequent row, each element is the
sum of the numbers directly above it, on either side. For example, here are the first
few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""

from typing import List


def get_pascal(k: int) -> List[int]:
    row = [1 for _ in range(k)]
    curr = 1
    for _ in range(k):
        # generating the value for each level
        last = 0
        for i in range(curr - 1):
            last, temp = row[i], last
            row[i] += temp
        curr += 1
    return row


if __name__ == "__main__":
    print(get_pascal(1))
    print(get_pascal(2))
    print(get_pascal(3))
    print(get_pascal(4))
    print(get_pascal(5))
    print(get_pascal(6))


"""
SPECS:

TIME COMPLEXITY: O(k ^ 2)
SPACE COMPLEXITY: O(k)
"""
