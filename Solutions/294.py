"""
Problem:

A competitive runner would like to create a route that starts and ends at his house,
with the condition that the route goes entirely uphill at first, and then entirely
downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary
mapping paths between some of these locations to their corresponding distances, find
the length of the shortest route satisfying the condition above. Assume the runner's
home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
"""

from sys import maxsize
from typing import Dict, List, Set, Tuple


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    dist = [[elem for elem in row] for row in graph]
    nodes = len(graph)
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if (
                    dist[i][j] < maxsize
                    and dist[i][k] < maxsize
                    and dist[k][j] < maxsize
                ):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def generate_graph_adjacency_matix(
    paths: Dict[Tuple[int, int], int], nodes: int
) -> List[List[int]]:
    graph = [[maxsize for _ in range(nodes)] for _ in range(nodes)]
    for src, dest in paths:
        graph[src][dest] = paths[src, dest]
    return graph


def get_route_dfs_helper(
    curr_pos: int,
    target: int,
    acc_weight: int,
    visited: Set[int],
    graph: List[List[int]],
    flag: bool = False,
) -> int:
    # flag is used to bypass returning weight of 0 when we start (curr_pos and target
    # is 0)
    if curr_pos == target and flag:
        return acc_weight
    visited.add(curr_pos)
    distance = maxsize
    for neighbour, weight in enumerate(graph[curr_pos]):
        if weight < maxsize:
            distance = min(
                distance,
                get_route_dfs_helper(
                    neighbour, target, acc_weight + weight, visited.copy(), graph, True
                ),
            )
    return distance


def get_route(elevations: Dict[int, int], paths: Dict[Tuple[int, int], int]) -> int:
    graph = generate_graph_adjacency_matix(paths, len(elevations))
    dist = floyd_warshall(graph)
    return get_route_dfs_helper(0, 0, 0, set(), dist)


if __name__ == "__main__":
    elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
    paths = {
        (0, 1): 10,
        (0, 2): 8,
        (0, 3): 15,
        (1, 3): 12,
        (2, 4): 10,
        (3, 4): 5,
        (3, 0): 17,
        (4, 0): 10,
    }
    print(get_route(elevations, paths))


"""
SPECS:

TIME COMPLEXITY: O(v.e)
SPACE COMPLEXITY: O(v ^ 2)
"""
