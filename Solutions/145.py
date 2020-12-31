"""
Problem:

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

from DataStructures.LinkedList import Node, LinkedList


def swap_nodes(ll: LinkedList) -> Node:
    node1 = ll.head
    node2 = ll.head.next
    while True:
        try:
            node1.val, node2.val = node2.val, node1.val
            node1, node2 = node1.next.next, node2.next.next
        except:
            break
    return ll.head


if __name__ == "__main__":
    LL = LinkedList()

    LL.add(1)
    LL.add(2)
    LL.add(3)
    LL.add(4)

    print(LL)
    print(swap_nodes(LL))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
