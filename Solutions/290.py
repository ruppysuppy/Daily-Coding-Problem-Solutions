"""
Problem:

On a mysterious island there are creatures known as Quxes which come in three colors:
red, green, and blue. One power of the Qux is that if two of them are standing next to
each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after
any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a
single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""

from typing import List

from DataStructures.Stack import Stack


QUXES = set(["R", "G", "B"])


def generate_new_qux(qux1: str, qux2: str) -> str:
    if qux1 == qux2:
        raise ValueError("Cannot form new Qux")
    result = QUXES - set([qux1, qux2])
    return result.pop()


def get_transformation(arrangement: List[str]) -> List[str]:
    stack = Stack()
    for qux in arrangement:
        if stack.is_empty() or stack.peek() == qux:
            stack.push(qux)
        else:
            qux_last = stack.pop()
            while True:
                # backpropagating in case the previous quxes needs to be updated
                qux = generate_new_qux(qux_last, qux)
                if stack.is_empty() or stack.peek() == qux:
                    break
                qux_last = stack.pop()
            stack.push(qux)
    return stack


if __name__ == "__main__":
    print(get_transformation(["R", "G", "B", "G", "B"]))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
