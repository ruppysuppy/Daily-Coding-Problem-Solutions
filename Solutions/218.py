"""
Problem:

Write an algorithm that computes the reversal of a directed graph. For example, if a
graph consists of A -> B -> C, it should become A <- B <- C.
"""

from DataStructures.Graph import GraphDirectedUnweighted


def reverse_direction(graph: GraphDirectedUnweighted) -> None:
    visited = set()
    for node in graph.connections:
        # storing the nodes that require updation in to change as for loop doesn't
        # support simultaneous updation
        visited.add(node)
        to_change = []
        for neighbour in graph.connections[node]:
            if neighbour not in visited:
                if node not in graph.connections[neighbour]:
                    to_change.append(neighbour)
        for neighbour in to_change:
            graph.connections[neighbour].add(node)
            graph.connections[node].remove(neighbour)


if __name__ == "__main__":
    graph = GraphDirectedUnweighted()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    print(graph)

    reverse_direction(graph)

    print(graph)


"""
SPECS:

TIME COMPLEXITY: O(v + e)
SPACE COMPLEXITY: O(v)
"""
