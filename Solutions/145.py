"""
Problem:

Given the head of a singly linked list, swap every two nodes and return its head.

Example:

Input = 1 -> 2 -> 3 -> 4
Output = 2 -> 1 -> 4 -> 3
"""

# local import from the Datastructure module
from DataStructures.LinkedList import Node, Linked_list

# FUNCTION TO PERFORM THE OPERATION
def swap_nodes(self):
    # creating pointers for the 2 nodes
    node1 = self.head
    node2 = self.head.next

    # looping till all nodes have been processed
    while True:
        try:
            # swapping the values of the nodes
            node1.val, node2.val = node2.val, node1.val

            # moving on to the next set of nodes
            node1 = node1.next.next
            node2 = node2.next.next

        except:
            break

    # returning the head
    return self.head


# adding the swap_node function to Linked List
setattr(Linked_list, "swap_nodes", swap_nodes)

# DRIVER CODE
LL = Linked_list()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)

print(LL)

print(LL.swap_nodes())
