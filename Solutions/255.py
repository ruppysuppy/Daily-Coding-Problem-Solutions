"""
Problem:

The transitive closure of a graph is a measure of which vertices are reachable from
other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a
path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""


from typing import List, Set


def get_transitive_matrix_helper(
    origin: int,
    curr_node: int,
    graph: List[List[int]],
    transitive_matrix: List[List[int]],
    visited: Set[int],
) -> None:
    # helper function to generate the transitive matrix using dfs
    for node in graph[curr_node]:
        transitive_matrix[origin][node] = 1
        if node not in visited:
            visited.add(node)
            get_transitive_matrix_helper(
                origin, node, graph, transitive_matrix, visited
            )


def get_transitive_matrix(graph: List[List[int]]) -> List[List[int]]:
    num_nodes = len(graph)
    transitive_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for node in range(num_nodes):
        get_transitive_matrix_helper(node, node, graph, transitive_matrix, set([node]))
    return transitive_matrix


if __name__ == "__main__":
    graph = [[0, 1, 3], [1, 2], [2], [3]]

    for row in get_transitive_matrix(graph):
        print(*row)


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n ^ 2)
"""
