"""
Problem:

An XOR linked list is a more memory efficient doubly linked list. Instead of each node
holding next and prev fields, it holds a field named both, which is an XOR of the next
node and the previous node. Implement an XOR linked list; it has an add(element) which
adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have
access to get_pointer and dereference_pointer functions that converts between nodes
and memory addresses.
"""


# Solution copied from:
# https://github.com/r1cc4rdo/daily_coding_problem/blob/master/problems/06


"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which
is a XOR of the next node and the previous node. Implement a XOR linked list; it has an
add(element) which adds the element to the end, and a get(index) which returns the node
at index.

NOTE: python does not have actual pointers (id() exists but it is not an actual pointer
in all implementations). For this reason, we use a python list to simulate memory.
Indexes are the addresses in memory. This has the unfortunate consequence that the
travel logic needs to reside in the List class rather than the Node one.
"""

from typing import Tuple


class XORLinkedListNode:
    def __init__(self, val: int, prev: int, next: int) -> None:
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_idx: int) -> int:
        return self.both ^ prev_idx

    def prev_node(self, next_idx: int) -> int:
        return self.both ^ next_idx


class XORLinkedList:
    def __init__(self) -> None:
        self.memory = [XORLinkedListNode(None, -1, -1)]

    def head(self) -> Tuple[int, int, XORLinkedListNode]:
        # head node index, prev node index, head node
        return 0, -1, self.memory[0]

    def add(self, val: int) -> None:
        current_node_index, previous_node_index, current_node = self.head()
        while True:
            # walk down the list until the end is found
            next_node_index = current_node.next_node(previous_node_index)
            if next_node_index == -1:
                # the end is reached
                break
            previous_node_index, current_node_index = (
                current_node_index,
                next_node_index,
            )
            current_node = self.memory[next_node_index]
        # allocation
        new_node_index = len(self.memory)
        current_node.both = previous_node_index ^ new_node_index
        self.memory.append(XORLinkedListNode(val, current_node_index, -1))

    def get(self, index: int) -> int:
        current_index, previous_index, current_node = self.head()
        for _ in range(index + 1):
            previous_index, current_index = (
                current_index,
                current_node.next_node(previous_index),
            )
            current_node = self.memory[current_index]
        return current_node.val


if __name__ == "__main__":
    xor_linked_list = XORLinkedList()

    xor_linked_list.add(1)
    xor_linked_list.add(2)
    xor_linked_list.add(3)
    xor_linked_list.add(4)

    print(xor_linked_list.get(0))
    print(xor_linked_list.get(1))
    print(xor_linked_list.get(2))
    print(xor_linked_list.get(3))
