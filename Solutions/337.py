"""
Problem:

Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space
over time?
"""

from random import randint

from DataStructures.LinkedList import Node, LinkedList


def shuffle(ll: LinkedList) -> LinkedList:
    # base case, no shuffling possible
    length = len(ll)
    if length in (0, 1):
        return ll
    # shuffling values
    for _ in range(length):
        # generating 2 random positions
        pos1, pos2 = randint(0, length - 1), randint(0, length - 1)
        node1, node2 = ll.head, ll.head
        # positioning the pointers at the proper poitions
        for _ in range(pos1):
            node1 = node1.next
        for _ in range(pos2):
            node2 = node2.next
        # swaping values
        node1.val, node2.val = node2.val, node1.val
    return ll


if __name__ == "__main__":
    ll = LinkedList()

    for i in range(1, 6):
        ll.add(i)

    print(ll)

    shuffle(ll)

    print(ll)


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(1)
"""
