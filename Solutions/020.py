"""
Problem:

Given 2 Linked List, find out whether they share a common node. If there is a common
node, find the common node.
"""

from typing import Optional

from DataStructures.LinkedList import Node, LinkedList


def common_node(ll1: LinkedList, ll2: LinkedList) -> bool:
    # traversing to the end of the Linked Lists and comparing the nodes
    pos1 = ll1.head
    while pos1.next != None:
        pos1 = pos1.next
    pos2 = ll2.head
    while pos2.next != None:
        pos2 = pos2.next
    # if the location of the last nodes of the lists are same, then they must share a
    # common node
    return pos1 is pos2


def common_node_pos(ll1: LinkedList, ll2: LinkedList) -> Optional[Node]:
    if common_node(ll1, ll2):
        len1, len2 = len(ll1), len(ll2)
        pos1, pos2 = ll1.head, ll2.head
        smaller_len = min(len1, len2)
        # traversing to the position where the intersection may occour in the longer
        # Linked List
        if len1 < len2:
            pos = len2 - len1
            for _ in range(pos):
                pos2 = pos2.next
        elif len1 > len2:
            pos = len1 - len2
            for _ in range(pos):
                pos1 = pos1.next
        # checking for intersecting node
        for _ in range(smaller_len):
            if pos1 is pos2:
                return pos1
            pos1 = pos1.next
            pos2 = pos2.next
    # no intersection
    return None


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.add(5)
    ll1.add(6)
    ll1.add(7)
    ll1.add(8)

    ll2 = LinkedList()
    ll2.add(1)
    ll2.add(2)
    ll2.add(3)
    ll2.add(4)

    ll3 = LinkedList()
    ll3.add(9)
    ll3.rear.next = ll1.head.next.next
    ll3.rear = ll3.rear.next.next
    ll3.length = 3

    print("Linked List 1:", ll1)
    print("Linked List 2:", ll2)
    print("Linked List 3:", ll3)

    print(common_node_pos(ll1, ll2))
    print(common_node_pos(ll1, ll3).val)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
