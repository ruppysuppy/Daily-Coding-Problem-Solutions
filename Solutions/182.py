"""
Problem:

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. 
For example, any binary tree is minimally-connected.
Given an undirected graph, check if the graph is minimally-connected. 
You can choose to represent the graph as either an adjacency matrix or adjacency list.
"""

# importing deepcopy to generate a deep copy of a dictionary
from copy import deepcopy

# local import for graph class from Datastructures module
from DataStructures.Graph import Graph_Undirected_Unweighted

# FUNCTION TO PERFROM THE OPERATION
def is_minimally_connected(self):
    # creating a copy for the graph
    graph_copy = Graph_Undirected_Unweighted()
    graph_copy.connections = deepcopy(self.connections)

    # getting a random node to start from
    # (the graph is undirected, so random selection is not a problem)
    for node in self.connections:
        start = node
        break

    # running bfs and checking if a node is visited more than once
    # (redundant edges present => not a minimally connected graph)
    visited = set([start])
    queue = [start]

    while queue:
        node = queue.pop(0)

        for child_node in graph_copy.connections[node]:
            graph_copy.connections[child_node].remove(node)
            queue.append(child_node)

            if child_node in visited:
                return False
            else:
                visited.add(child_node)

    return True


# adding the function to the graph class
setattr(Graph_Undirected_Unweighted, "is_minimally_connected", is_minimally_connected)

# DRIVER CODE
graph = Graph_Undirected_Unweighted()

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)

print(graph)
print(graph.is_minimally_connected())

graph.add_edge(1, 4)

print(graph)
print(graph.is_minimally_connected())
