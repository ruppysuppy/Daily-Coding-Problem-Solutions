"""
Problem:

A graph is minimally-connected if it is connected and there is no edge that can be
removed while still leaving the graph connected. For example, any binary tree is
minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to
represent the graph as either an adjacency matrix or adjacency list.
"""

from copy import deepcopy

from DataStructures.Graph import GraphUndirectedUnweighted
from DataStructures.Queue import Queue


def is_minimally_connected(graph: GraphUndirectedUnweighted) -> bool:
    graph_copy = GraphUndirectedUnweighted()
    graph_copy.connections, graph_copy.nodes = deepcopy(graph.connections), graph.nodes
    # getting a random node for starting the traversal
    for node in graph.connections:
        start = node
        break
    # running bfs and checking if a node is visited more than once
    # (redundant edges present => not a minimally connected graph)
    visited = set([start])
    queue = Queue()
    queue.enqueue(start)
    while not queue.is_empty():
        node = queue.dequeue()
        for neighbour in graph_copy.connections[node]:
            graph_copy.connections[neighbour].remove(node)
            queue.enqueue(neighbour)
            if neighbour in visited:
                return False
            visited.add(neighbour)
    return True


if __name__ == "__main__":
    graph = GraphUndirectedUnweighted()

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)

    print(graph)
    print(is_minimally_connected(graph))

    graph.add_edge(1, 4)

    print(graph)
    print(is_minimally_connected(graph))


"""
SPECS:

TIME COMPLEXITY: O(n x e)
SPACE COMPLEXITY: O(n + e)
"""
