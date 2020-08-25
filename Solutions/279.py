"""
Problem:

A classroom consists of N students, whose friendships can be represented in an
adjacency list. For example, the following descibes a situation where 0 is friends
with 1 and 2, 3 is friends with 6, and so on.

{
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}
Each student can be placed in a friend group, which can be defined as the transitive
closure of that student's friendship relations. In other words, this is the smallest
set such that no student in the group has any friends outside this group. For the
example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups
in the class.
"""

from typing import Dict, List, Set

from DataStructures.Graph import GraphUndirectedUnweighted


# graph functions
def dfs_components_helper(
    graph: GraphUndirectedUnweighted, node: int, component: Set[int], visited: Set[int]
) -> None:
    # function to get all nodes in a component using dfs
    visited.add(node)
    component.add(node)
    for neighbour in graph.connections[node]:
        if neighbour not in visited:
            dfs_components_helper(graph, neighbour, component, visited)


def get_components(graph: GraphUndirectedUnweighted) -> List[Set[int]]:
    # function to generate the components
    components = []
    visited = set()
    for node in graph.connections:
        if node not in visited:
            component = set()
            dfs_components_helper(graph, node, component, visited)
            components.append(component)
    return components


# function to generate the transitive closure
def friendship_transitive_closure(
    friendship_list: Dict[int, List[int]],
) -> List[Set[int]]:
    graph = GraphUndirectedUnweighted()
    for node in friendship_list:
        graph.add_node(node)
        for neighbour in friendship_list[node]:
            graph.add_edge(node, neighbour)
    return get_components(graph)


if __name__ == "__main__":
    print(
        friendship_transitive_closure(
            {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n + e)
SPACE COMPLEXITY: O(n)
[n = nodes, e = edges]
"""
