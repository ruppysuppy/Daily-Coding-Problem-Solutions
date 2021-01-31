"""
Problem:

Given a linked list, rearrange the node values such that they appear in alternating
low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you
should return 1 -> 3 -> 2 -> 5 -> 4.
"""

from DataStructures.LinkedList import Node, LinkedList


def rearrange(ll: LinkedList) -> None:
    nodes_count = len(ll)
    nodes = [int(node) for node in ll]
    nodes.sort()

    for i in range(2, nodes_count, 2):
        nodes[i], nodes[i - 1] = nodes[i - 1], nodes[i]

    curr = ll.head
    for i in range(nodes_count):
        curr.val = nodes[i]
        curr = curr.next


if __name__ == "__main__":
    LL = LinkedList()

    for i in range(1, 6):
        LL.add(i)

    print(LL)
    rearrange(LL)
    print(LL)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
