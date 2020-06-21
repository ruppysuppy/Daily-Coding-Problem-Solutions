'''
Problem:

Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
'''

# local import from Datastructure module
from DataStructures.Graph import Graph_Directed_Unweighted


# FUNCTION TO PERFORM THE OPERATION
def reverse_direction(self):
    visited = set()

    for node in self.connections:
        # storing the nodes that require updation in to change as for loop doesn't 
        # support simultaneous updation
        visited.add(node)
        to_change = []

        for neighbour in self.connections[node]:
            if (neighbour not in visited):
                if (node not in self.connections[neighbour]):
                    to_change.append(neighbour)
        
        for neighbour in to_change:
            self.connections[neighbour].add(node)
            self.connections[node].remove(neighbour)


setattr(Graph_Directed_Unweighted, 'reverse_direction', reverse_direction)

# DRIVER CODE
graph = Graph_Directed_Unweighted()

graph.add_edge("A", "B")
graph.add_edge("B", "C")

print(graph)

graph.reverse_direction()

print(graph)