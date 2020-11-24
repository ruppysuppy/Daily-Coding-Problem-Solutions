"""
Problem:

Given an undirected graph represented as an adjacency matrix and an integer k, write a
function to determine whether each vertex in the graph can be colored such that no two
adjacent vertices share the same color using at most k colors.
"""

from typing import List


def can_color(adjacency_matrix: List[List[int]], k: int) -> bool:
    minimum_colors_required = 0
    vertices = len(adjacency_matrix)
    # generating the minimum number of colors required to color the graph
    for vertex in range(vertices):
        colors_required_for_current_vertex = sum(adjacency_matrix[vertex]) + 1
        minimum_colors_required = max(
            minimum_colors_required, colors_required_for_current_vertex
        )
    return minimum_colors_required <= k


if __name__ == "__main__":
    adjacency_matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
    ]

    print(can_color(adjacency_matrix, 4))
    print(can_color(adjacency_matrix, 3))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
