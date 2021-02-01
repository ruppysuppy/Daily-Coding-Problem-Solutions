"""
Problem:

Given an undirected graph, determine if it contains a cycle.
"""

from typing import Set

from DataStructures.Graph import GraphUndirectedUnweighted


def get_components_helper(
    graph: GraphUndirectedUnweighted,
    node: int,
    component: Set[int],
    visited: Set[int],
    degree: int = 0,
) -> int:
    # function to get the degree of the component
    # generating the degree recursively using dfs
    visited.add(node)
    component.add(node)
    for neighbour in graph.connections[node]:
        degree += 1
        if neighbour not in visited:
            degree += get_components_helper(graph, neighbour, component, visited)
    return degree


def is_cyclic(graph: GraphUndirectedUnweighted) -> bool:
    visited = set()
    for node in graph.connections:
        if node not in visited:
            component = set()
            component_degree = get_components_helper(graph, node, component, visited)
            if component_degree > 2 * (len(component) - 1):
                return False
    return True


if __name__ == "__main__":
    graph = GraphUndirectedUnweighted()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    print(is_cyclic(graph))

    graph.add_edge(2, 4)

    print(is_cyclic(graph))


"""
SPECS:

TIME COMPLEXITY: O(n + e)
SPACE COMPLEXITY: O(n)
[n = nodes, e = edges]
"""
