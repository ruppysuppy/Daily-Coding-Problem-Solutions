"""
Problem:

A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b. Whenever
a node receives a message, it immediately passes the message on to a neighboring node,
if possible.

Assuming all nodes are connected, determine how long it will take for every node to
receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take
that much time
"""

from sys import maxsize
from typing import Dict, Optional, Tuple

# Local Import from the DataStructure module
from DataStructures.Graph import GraphDirectedWeighted
from DataStructures.PriorityQueue import MinPriorityQueue


def dijkstras_algo(
    graph: GraphDirectedWeighted, start: int
) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """
    Dijkstras Single Source Shortest Path Algorithm
    """
    # intialization
    dist = {node: maxsize for node in graph.connections}
    parent = {node: None for node in graph.connections}
    dist[start] = 0
    priority_queue = MinPriorityQueue()
    [priority_queue.push(node, weight) for node, weight in dist.items()]
    # distance updation
    while not priority_queue.isEmpty():
        node = priority_queue.extract_min()
        for neighbour in graph.connections[node]:
            if dist[neighbour] > dist[node] + graph.connections[node][neighbour]:
                dist[neighbour] = dist[node] + graph.connections[node][neighbour]
                priority_queue.update_key(neighbour, dist[neighbour])
                parent[neighbour] = node
    return dist, parent


def get_propagation_time(edges):
    # graph generation from edges
    graph = GraphDirectedWeighted()
    for src, dest, wt in edges:
        graph.add_edge(src, dest, wt)
    # returning the greatest distance
    time, _ = dijkstras_algo(graph, 0)
    return max(time.values())


if __name__ == "__main__":
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (0, 5, 4),
        (1, 3, 8),
        (2, 3, 1),
        (3, 5, 10),
        (3, 4, 5),
    ]
    print(get_propagation_time(edges))
