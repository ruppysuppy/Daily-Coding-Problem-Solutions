"""
Problem:

A bridge in a connected (undirected) graph is an edge that, if removed, causes the
graph to become disconnected. Find all the bridges in a graph.
"""

from sys import maxsize
from typing import Dict, List, Optional, Tuple

# local import from the DataStructure module
from DataStructures.Graph import GraphUndirectedUnweighted


def get_bridges_helper(
    self,
    node: int,
    visited: set,
    parent: Dict[int, Optional[int]],
    low: Dict[int, int],
    disc: Dict[int, int],
    bridges: List[Tuple[int, int]],
) -> None:
    # DFS based helper function to find all bridges
    visited.add(node)
    disc[node] = self.time
    low[node] = self.time
    self.time += 1
    for neighbour in self.connections[node]:
        if neighbour not in visited:
            parent[neighbour] = node
            self.get_bridges_helper(neighbour, visited, parent, low, disc, bridges)
            # check if the subtree rooted with neighbour has a connection to one of the
            # ancestors of node
            low[node] = min(low[node], low[neighbour])
            # if the lowest vertex reachable from subtree under neighbour is below node
            # in DFS tree, then node-neighbour is a bridge
            if low[neighbour] > disc[node]:
                bridges.append((node, neighbour))
        elif neighbour != parent[node]:
            # update low value of node for parent function calls.
            low[node] = min(low[node], disc[neighbour])


def get_bridges(self) -> List[Tuple[int, int]]:
    # function to get all the bridges in a graph
    visited = set()
    disc = {node: maxsize for node in self.connections}
    low = {node: maxsize for node in self.connections}
    parent = {node: None for node in self.connections}
    bridges = []
    self.time = 0
    for node in self.connections:
        if node not in visited:
            self.get_bridges_helper(node, visited, parent, low, disc, bridges)
    return bridges


# adding the required methods and attributes to the graph class
setattr(GraphUndirectedUnweighted, "get_bridges_helper", get_bridges_helper)
setattr(GraphUndirectedUnweighted, "get_bridges", get_bridges)
setattr(GraphUndirectedUnweighted, "time", 0)


if __name__ == "__main__":
    g1 = GraphUndirectedUnweighted()
    g1.add_edge(1, 0)
    g1.add_edge(0, 2)
    g1.add_edge(2, 1)
    g1.add_edge(0, 3)
    g1.add_edge(3, 4)
    print("Bridges in first graph:")
    print(*g1.get_bridges())

    g2 = GraphUndirectedUnweighted()
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print("\nBridges in second graph:")
    print(*g2.get_bridges())

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
    print(*g3.get_bridges())
