"""
Problem:

Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight. 
Given an undirected graph with weighted edges, compute the maximum weight spanning tree.
"""

from DataStructures.Graph import Graph_Undirected_Weighted


def get_max_span_helper(graph, start, remaining, score):
    if not remaining:
        return score

    scores = []

    for dest in graph.connections[start]:
        if dest in remaining:
            rem_cp = set(remaining)
            rem_cp.remove(dest)

            new_score = get_max_span_helper(
                graph, dest, rem_cp, score + graph.connections[start][dest]
            )

            scores.append(new_score)

    return max(scores)


def get_max_span(graph):
    node_set = set(graph.connections.keys())
    start_node = node_set.pop()

    score = get_max_span_helper(graph, start_node, node_set, 0)
    return score


# DRIVER CODE
graph = Graph_Undirected_Weighted()

graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 2)
graph.add_edge(3, 2, 1)
graph.add_edge(3, 4, 3)
graph.add_edge(2, 4, 4)

print(graph.connections)
print(get_max_span(graph))

graph = Graph_Undirected_Weighted()

graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 2)
graph.add_edge(3, 2, 3)

print(graph.connections)
print(get_max_span(graph))
