"""
Problem:

Recall that the minimum spanning tree is the subset of edges of a tree that connect all
its vertices with the smallest possible total edge weight. Given an undirected graph
with weighted edges, compute the maximum weight spanning tree.
"""

from typing import Set

from DataStructures.Graph import GraphUndirectedWeighted


def get_maximum_spanning_tree_helper(
    graph: GraphUndirectedWeighted,
    curr_node: int,
    remaining_nodes: Set[int],
    weight: int,
) -> int:
    if not remaining_nodes:
        return weight

    scores = []
    for destination in graph.connections[curr_node]:
        if destination in remaining_nodes:
            rem_cp = set(remaining_nodes)
            rem_cp.remove(destination)
            new_score = get_maximum_spanning_tree_helper(
                graph,
                destination,
                rem_cp,
                weight + graph.connections[curr_node][destination],
            )
            scores.append(new_score)
    return max(scores)


def get_maximum_spanning_tree(graph: GraphUndirectedWeighted) -> int:
    node_set = set(graph.connections.keys())
    start_node = node_set.pop()

    weight = get_maximum_spanning_tree_helper(graph, start_node, node_set, 0)
    return weight


if __name__ == "__main__":
    graph = GraphUndirectedWeighted()

    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 2)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 4, 3)
    graph.add_edge(2, 4, 4)

    print(graph)
    print(get_maximum_spanning_tree(graph))

    graph = GraphUndirectedWeighted()

    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(3, 2, 3)

    print(graph)
    print(get_maximum_spanning_tree(graph))


"""
SPECS:

TIME COMPLEXITY: O(n x e)
SPACE COMPLEXITY: O(n x e)
"""
