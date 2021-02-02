"""
Problem:

You are given a huge list of airline ticket prices between different cities around the
world on a given day. These are all direct flights. Each element in the list has the
format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to
their destination B. Find the cheapest fare possible for this journey and print the
itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our
input flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, the cheapest itinerary would be
JFK -> ATL -> ORD -> LAX, costing $440.
"""

from sys import maxsize
from typing import Dict, List, Optional, Tuple

from DataStructures.Graph import GraphDirectedWeighted
from DataStructures.PriorityQueue import MinPriorityQueue


def modified_dijkstra(
    graph: GraphDirectedWeighted, start: str, k: int
) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    dist = {node: maxsize for node in graph.connections}
    parent = {node: None for node in graph.connections}
    dist[start] = 0
    priority_queue = MinPriorityQueue()
    [priority_queue.push(node, weight) for node, weight in dist.items()]

    while not priority_queue.is_empty():
        node = priority_queue.extract_min()
        ancestors = 0
        parent_node = parent[node]
        # calculating ancestors
        while parent_node:
            ancestors += 1
            parent_node = parent[parent_node]
        # limiting distance update till k moves
        if ancestors <= k:
            for neighbour in graph.connections[node]:
                if dist[neighbour] > dist[node] + graph.connections[node][neighbour]:
                    dist[neighbour] = dist[node] + graph.connections[node][neighbour]
                    parent[neighbour] = node
                    priority_queue.update_key(neighbour, dist[neighbour])
    return dist, parent


def generate_path(
    flights: List[Tuple[str, str, int]], start: str, dest: str, k: int
) -> Tuple[int, List[str]]:
    # graph generation
    graph = GraphDirectedWeighted()
    for src, dest, wt in flights:
        graph.add_edge(src, dest, wt)
    # running dijkstra's algorithm
    dist, parent = modified_dijkstra(graph, start, k)
    # getting the cost and path
    if not parent[dest]:
        return []
    path, cost = [dest], dist[dest]
    curr = parent[dest]
    while curr:
        path.append(curr)
        curr = parent[curr]
    return cost, path[::-1]


if __name__ == "__main__":
    flights = [
        ("JFK", "ATL", 150),
        ("ATL", "SFO", 400),
        ("ORD", "LAX", 200),
        ("LAX", "DFW", 80),
        ("JFK", "HKG", 800),
        ("ATL", "ORD", 90),
        ("JFK", "LAX", 500),
    ]
    print(generate_path(flights, "JFK", "LAX", 3))


"""
SPECS:

TIME COMPLEXITY: O(e x v x log(v))
SPACE COMPLEXITY: O(v ^ 2)
[even though dijkstra's algorithm runs in O(e x log(v)) to lock maximum k moves, the
compleity increases to O(e x v x log(v))]
"""
