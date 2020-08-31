"""
Problem:

You are given an array representing the heights of neighboring buildings on a city
street, from east to west. The city assessor would like you to write an algorithm that
returns how many of these buildings have a view of the setting sun, in order to
properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top
floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the
west.

Can you do this using just one forward pass through the array?
"""

from sys import maxsize
from typing import List

from DataStructures.Stack import Stack


def get_view_sunset(arr: List[int]) -> int:
    # the buildings can view the sunset when the elements are chosen in-order, keeping
    # only the ones that allow decending order selection
    stack = Stack()
    for elem in arr:
        if not stack.is_empty():
            last = stack.peek()
            while not stack.is_empty() and last < elem:
                stack.pop()
                last = maxsize
                if not stack.is_empty():
                    last = stack.peek()
        if stack.is_empty() or stack.peek() > elem:
            stack.push(elem)
    return len(stack)


if __name__ == "__main__":
    print(get_view_sunset([3, 7, 8, 3, 6, 1]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
