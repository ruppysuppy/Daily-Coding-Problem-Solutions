"""
Problem:

Given an undirected graph G, check whether it is bipartite. 
Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.
"""

# local import from the Datastructure module
from DataStructures.Graph import Graph_Undirected_Unweighted

# FUNCTION TO PERFORM THE OPERATION
def check_bipartite(self):
    # declaring the sets
    set_1, set_2 = set(), set()

    # getting the nodes (sorted in reversed order)
    sorted_nodes = sorted(
        self.connections.items(), key=lambda x: len(x[1]), reverse=True
    )

    # iterating through the sorted nodes
    for node, _ in sorted_nodes:
        # if the node is in the 2nd set, we skip the loop
        if node in set_2:
            continue

        # else we add it to the 1st set
        set_1.add(node)

        # adding the nodes the current node is connected to, to the 2nd set
        for other_node in self.connections[node]:
            set_2.add(other_node)

    # checking if all the node in the 2nd set has their connections only in the 1st set
    for node in set_2:
        for other_node in self.connections[node]:
            if other_node in set_2:
                return False

    # returning True if the graph is bi-partite
    return True


# adding the function to the graph
setattr(Graph_Undirected_Unweighted, "check_bipartite", check_bipartite)

# DRIVER CODE
graph1 = Graph_Undirected_Unweighted()

graph1.add_edge(1, 2)
graph1.add_edge(2, 3)
graph1.add_edge(1, 4)

print(graph1.check_bipartite())

graph1.add_edge(1, 3)

print(graph1.check_bipartite())

graph2 = Graph_Undirected_Unweighted()

graph2.add_edge(1, 2)
graph2.add_edge(2, 3)
graph2.add_edge(3, 4)
graph2.add_edge(4, 1)

print(graph2.check_bipartite())
