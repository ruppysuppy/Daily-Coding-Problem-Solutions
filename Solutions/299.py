"""
Problem:

A group of houses is connected to the main water plant by means of a set of pipes. A
house can either be connected by a set of pipes extending directly to the plant, or
indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows
represent pipes: A <--> B <--> C <--> plant

Each pipe has an associated cost, which the utility company would like to minimize.
Given an undirected graph of pipe connections, return the lowest cost configuration of
pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A,
plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
"""

from sys import maxsize
from typing import Dict, Optional, Tuple

from DataStructures.Graph import GraphUndirectedWeighted
from DataStructures.PriorityQueue import MinPriorityQueue


def dijkstra(
    graph: GraphUndirectedWeighted, start: str
) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    # dijkstra's algorithm for single source shortest path
    dist = {node: maxsize for node in graph.connections}
    parent = {node: None for node in graph.connections}
    dist[start] = 0
    priority_queue = MinPriorityQueue()
    [priority_queue.push(node, weight) for node, weight in dist.items()]
    # running dijkstra's algorithm
    while not priority_queue.isEmpty():
        node = priority_queue.extract_min()
        for neighbour in graph.connections[node]:
            if dist[neighbour] > dist[node] + graph.connections[node][neighbour]:
                dist[neighbour] = dist[node] + graph.connections[node][neighbour]
                priority_queue.update_key(neighbour, dist[neighbour])
                parent[neighbour] = node
    return dist, parent


def tree_weight_sum(dist: Dict[str, int], parent: Dict[str, Optional[str]]) -> int:
    # function to calculate the total weight of the dijkstra's minimum spanning tree
    weight_sum = 0
    for node in dist:
        if parent[node]:
            weight_sum += dist[node] - dist[parent[node]]
    return weight_sum


def get_minimum_cost(pipes: Dict[str, Dict[str, int]]) -> int:
    # function to get the minimum configuration distance of the pipes
    # graph generation
    graph = GraphUndirectedWeighted()
    for src in pipes:
        for dest in pipes[src]:
            graph.add_edge(src, dest, pipes[src][dest])
    # minimum cost calculation
    dist, parent = dijkstra(graph, "plant")
    return tree_weight_sum(dist, parent)


if __name__ == "__main__":
    print(
        get_minimum_cost(
            pipes={
                "plant": {"A": 1, "B": 5, "C": 20},
                "A": {"C": 15},
                "B": {"C": 10},
                "C": {},
            }
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(e + n.log(n))
SPACE COMPLEXITY: O(n + e)
[n = number of nodes, e = number of edges]
"""
