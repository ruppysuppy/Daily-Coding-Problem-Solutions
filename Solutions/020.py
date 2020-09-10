"""
Problem:

Given 2 Linked List, find out whether they share a common node. If there is a common node, find the common node.
"""

# Local Import from the datastructure module

from DataStructures.LinkedList import Node, Linked_list

# FUNCTION TO PERFORM THE OPERATION (checking for common node)
def common_node(LL1, LL2):
    # Traversing to the end of the 1st Linked List
    pos1 = LL1.head
    while pos1.next != None:
        pos1 = pos1.next

    # Traversing to the end of the 2nd Linked List
    pos2 = LL2.head
    while pos2.next != None:
        pos2 = pos2.next

    # If the location of the last nodes of the lists are same, then they must share a common node
    # NOTE: 'is' is used in place of '==' to check the location and not the object (as if the values are same, '==' will return True even when the nodes are different)
    # WORKING METHOD: if 2 Linked Lists share a node, the structure becomes like "Y", so the end node must be same
    if pos1 is pos2:
        return True
    else:
        return False


# FUNCTION TO PERFORM THE OPERATION (finds common node)
def common_node_pos(LL1, LL2):
    if common_node(LL1, LL2):

        # Getting the length of the Linked Lists
        len1 = len(LL1)
        len2 = len(LL2)

        # Pointers to hold the postions
        pos1 = LL1.head
        pos2 = LL2.head

        if len1 < len2:
            # If 2nd list is longer, traversing to the required location (len2 - len1 as their end are same)
            pos = len2 - len1
            for i in range(pos):
                pos2 = pos2.next

            # Checking whether each node is same (returns the common node), else moving to the next node
            for i in range(len1):
                if pos1 is pos2:
                    return pos1
                pos1 = pos1.next
                pos2 = pos2.next

        elif len1 == len2:
            # Checking whether each node is same (returns the common node), else moving to the next node
            for i in range(len1):
                if pos1 is pos2:
                    return pos1
                pos1 = pos1.next
                pos2 = pos2.next

        else:
            # If 1st list is longer, traversing to the required location (len1 - len2 as their end are same)
            pos = len1 - len2
            for i in range(pos):
                pos1 = pos1.next

            # Checking whether each node is same (returns the common node), else moving to the next node
            for i in range(len2):
                if pos1 is pos2:
                    return pos1
                pos1 = pos1.next
                pos2 = pos2.next

    else:
        return None


# DRIVER CODE (LL3 shares the last 2 nodes of LL1)
LL1 = Linked_list()
LL1.add(5)
LL1.add(6)
LL1.add(7)
LL1.add(8)

LL2 = Linked_list()
LL2.add(1)
LL2.add(2)
LL2.add(3)
LL2.add(4)

LL3 = Linked_list()
LL3.add(9)
LL3.rear.next = LL1.head.next.next
LL3.rear = LL3.rear.next.next
LL3.length = 3

print("Linked List 1:", LL1)
print("Linked List 2:", LL2)
print("Linked List 3:", LL3)

print(common_node_pos(LL1, LL2))
print(common_node_pos(LL1, LL3))
