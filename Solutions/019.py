"""
Problem:

A builder is looking to build a row of N houses that can be of K different colors. He
has a goal of minimizing cost while ensuring that no two neighboring houses are of the
same color.

Given an N by K matrix where the nth row and kth column represents the cost to build
the nth house with kth color, return the minimum cost which achieves this goal.
"""

from typing import List

Matrix = List[List[int]]


def minimize_color_cost_helper(
    color_matrix: Matrix,
    results: List,
    curr_house: int,
    prev_color: int,
    curr_cost: int,
    n: int,
    k: int,
):
    if curr_house == n:
        results.append(curr_cost)
        return
    # generating all the possible combinations
    for curr_color in range(k):
        # avoiding two neighboring houses having the same color
        if curr_color != prev_color:
            minimize_color_cost_helper(
                color_matrix,
                results,
                curr_house + 1,
                curr_color,
                curr_cost + color_matrix[curr_house][curr_color],
                n,
                k,
            )


def minimize_color_cost(color_matrix: Matrix) -> int:
    sequence = []
    n, k = len(color_matrix), len(color_matrix[0])
    minimize_color_cost_helper(color_matrix, sequence, 0, -1, 0, n, k)
    # returning the minimum cost
    return min(sequence)


if __name__ == "__main__":
    print(minimize_color_cost([[1, 5, 2], [2, 3, 1], [7, 3, 5], [6, 2, 3]]))
    print(minimize_color_cost([[1, 5, 2], [2, 3, 1], [7, 3, 5], [6, 3, 2]]))


"""
SPECS:

TIME COMPLEXITY: O(n x k!)
SPACE COMPLEXITY: O(n x k!)
"""
