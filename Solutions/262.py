"""
Problem:

A bridge in a connected (undirected) graph is an edge that, if removed, causes the
graph to become disconnected. Find all the bridges in a graph.
"""

from sys import maxsize
from typing import Dict, List, Optional, Set, Tuple

from DataStructures.Graph import GraphUndirectedUnweighted


def get_bridges_helper(
    graph: GraphUndirectedUnweighted,
    node: int,
    visited: Set[int],
    parent: Dict[int, Optional[int]],
    low: Dict[int, int],
    disc: Dict[int, int],
    bridges: List[Tuple[int, int]],
) -> None:
    # find all bridges using dfs
    visited.add(node)
    disc[node] = graph.time
    low[node] = graph.time
    graph.time += 1
    for neighbour in graph.connections[node]:
        if neighbour not in visited:
            parent[neighbour] = node
            get_bridges_helper(graph, neighbour, visited, parent, low, disc, bridges)
            # check if the subtree rooted with neighbour has a connection to one of the
            # ancestors of node
            low[node] = min(low[node], low[neighbour])
            # if the lowest vertex reachable from subtree under neighbour is below node
            # in DFS tree, then node-neighbour is a bridge
            if low[neighbour] > disc[node]:
                bridges.append((node, neighbour))
        elif neighbour != parent[node]:
            low[node] = min(low[node], disc[neighbour])


def get_bridges(graph: GraphUndirectedUnweighted) -> List[Tuple[int, int]]:
    visited = set()
    disc = {node: maxsize for node in graph.connections}
    low = {node: maxsize for node in graph.connections}
    parent = {node: None for node in graph.connections}
    bridges = []
    graph.time = 0
    for node in graph.connections:
        if node not in visited:
            get_bridges_helper(graph, node, visited, parent, low, disc, bridges)
    return bridges


if __name__ == "__main__":
    g1 = GraphUndirectedUnweighted()
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print("Bridges in first graph:")
    print(*get_bridges(g1))

    g2 = GraphUndirectedUnweighted()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print("\nBridges in second graph:")
    print(*get_bridges(g2))

    g3 = GraphUndirectedUnweighted()
    g3.add_edge(0, 1)
    g3.add_edge(1, 2)
    g3.add_edge(2, 0)
    g3.add_edge(1, 3)
    g3.add_edge(1, 4)
    g3.add_edge(1, 6)
    g3.add_edge(3, 5)
    g3.add_edge(4, 5)
    print("\nBridges in third graph:")
    print(*get_bridges(g3))


"""
SPECS:

TIME COMPLEXITY: O(v + e)
SPACE COMPLEXITY: O(v)
"""
