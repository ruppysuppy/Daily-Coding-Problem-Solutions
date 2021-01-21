"""
Problem:

Given an undirected graph G, check whether it is bipartite. Recall that a graph is
bipartite if its vertices can be divided into two independent sets, U and V, such that
no edge connects vertices of the same set.
"""

from DataStructures.Graph import GraphUndirectedUnweighted


def is_bipartite(graph: GraphUndirectedUnweighted) -> bool:
    set_1, set_2 = set(), set()
    sorted_nodes = sorted(
        graph.connections.items(), key=lambda x: len(x[1]), reverse=True
    )

    for node, _ in sorted_nodes:
        if node in set_2:
            continue
        set_1.add(node)
        for other_node in graph.connections[node]:
            set_2.add(other_node)
    for node in set_2:
        for other_node in graph.connections[node]:
            if other_node in set_2:
                return False
    return True


if __name__ == "__main__":
    graph1 = GraphUndirectedUnweighted()

    graph1.add_edge(1, 2)
    graph1.add_edge(2, 3)
    graph1.add_edge(1, 4)

    print(is_bipartite(graph1))

    graph1.add_edge(1, 3)

    print(is_bipartite(graph1))

    graph2 = GraphUndirectedUnweighted()

    graph2.add_edge(1, 2)
    graph2.add_edge(2, 3)
    graph2.add_edge(3, 4)
    graph2.add_edge(4, 1)

    print(is_bipartite(graph2))


"""
SPECS:

TIME COMPLEXITY: O(v + e)
SPACE COMPLEXITY: O(v)
[e = edges, v = vertices]
"""
