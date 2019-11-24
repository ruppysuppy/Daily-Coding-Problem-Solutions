# This program was not written by me, but this shows the implementation of a XOR Linked List in a well defined manner
# For more details check out: https://en.wikipedia.org/wiki/XOR_linked_list
# NOTE: XOR Linked List is not very practical to use as unlike Double Linked List you have to traverse from the end, even when you have access to a middle node. Python doesn't allow XOR operations on memory locations either.

"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is a XOR of the next node
and the previous node. Implement a XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.
Example:
>>> l = coding_problem_6()
>>> for cnt in xrange(0, 4):
...     l.add(cnt)
>>> l.get(2) == 2
True
Note: python does not have actual pointers (id() exists but it is not an actual pointer in all implementations).
For this reason, we use a python list to simulate memory. Indexes are the addresses in memory. This has the
unfortunate consequence that the travel logic needs to reside in the List class rather than the Node one.
"""

class XORLinkedListNode(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_idx):
        return self.both ^ prev_idx

    def prev_node(self, next_idx):
        return self.both ^ next_idx

class XORLinkedList(object):
    def __init__(self):
        self.memory = [XORLinkedListNode(None, -1, -1)]

    def head(self):
        return 0, -1, self.memory[0]  # head node index, prev node index, head node

    def add(self, val):
        current_node_index, previous_node_index, current_node = self.head()
        while True:  # walk down the list until we find the end
            next_node_index = current_node.next_node(previous_node_index)
            if next_node_index == -1:  # we reached the end on the list
                break
            previous_node_index, current_node_index = current_node_index, next_node_index
            current_node = self.memory[next_node_index]
        new_node_index = len(self.memory)  # "allocation"
        current_node.both = previous_node_index ^ new_node_index
        self.memory.append(XORLinkedListNode(val, current_node_index, -1))

    def get(self, index):
        current_index, previous_index, current_node = self.head()
        for cnt in range(index + 1):
            previous_index, current_index = current_index, current_node.next_node(previous_index)
            current_node = self.memory[current_index]
        return current_node.val