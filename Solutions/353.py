"""
Problem:

You are given a histogram consisting of rectangles of different heights. These heights
are represented in an input list, such that [1, 3, 2, 5] corresponds to the following
diagram:

      x
      x  
  x   x
  x x x
x x x x
Determine the area of the largest rectangle that can be formed only from the bars of
the histogram. For the diagram above, for example, this would be six, representing the
2 x 3 area at the bottom right.
"""

from typing import List

from DataStructures.Stack import Stack


def max_area_histogram(histogram: List[int]):
    stack = Stack()
    max_area = 0
    index = 0

    while index < len(histogram):
        if stack.is_empty() or histogram[stack.peek()] <= histogram[index]:
            stack.push(index)
            index += 1
        else:
            # if the current bar is lower than top of stack, the area of rectangle
            # needs to be calculated with the stack top as the smallest (or minimum
            # height) bar.
            top_of_stack = stack.pop()
            area = histogram[top_of_stack] * (
                (index - stack.peek() - 1) if not stack.is_empty() else index
            )
            max_area = max(max_area, area)
    # calculating the area formed by the indices still in the stack
    while not stack.is_empty():
        top_of_stack = stack.pop()
        area = histogram[top_of_stack] * (
            (index - stack.peek() - 1) if not stack.is_empty() else index
        )
        max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    print(max_area_histogram([1, 3, 2, 5]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
