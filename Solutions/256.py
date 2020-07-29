'''
Problem:

Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.
'''

from DataStructures.LinkedList import Node, Linked_list


def rearrange(self):
    # getting the nodes in sorted format
    nodes = [int(node) for node in self]
    nodes.sort()
    # interleaving the nodes to form alternating pattern (low -> high -> low ...)
    for i in range(2, len(nodes), 2):
        nodes[i], nodes[i - 1] = nodes[i - 1], nodes[i]
    # updating the linked list
    curr = self.head
    for i in range(len(nodes)):
        curr.val = nodes[i]
        curr = curr.next


# adding the rearrange method to the class
setattr(Linked_list, 'rearrange', rearrange)


# DRIVER CODE
LL = Linked_list()

for i in range(1, 6):
    LL.add(i)

print(LL)

LL.rearrange()

print(LL)
