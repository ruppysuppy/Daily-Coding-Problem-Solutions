'''
Problem:

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

Example:

Linked List = 5 -> 1 -> 8 -> 0 -> 3
k = 3
Output = 1 -> 0 -> 5 -> 8 -> 3
'''

# local import from the Datastructre module
from DataStructures.LinkedList import Node, Linked_list

# FUNCTION TO PERFORM THE OPERATION
def pivot(self, k):
    # declaring the 2 pointers
    ptr1 = self.head
    ptr2 = self.head

    # using the 2 pointers to swap the values
    for _ in range(self.length):
        if (ptr2.val < k):
            ptr1.val, ptr2.val = ptr2.val, ptr1.val
            ptr1 = ptr1.next
        # iterating through the linked list
        ptr2 = ptr2.next

# adding the pivot function to the Linked List class
setattr(Linked_list, 'pivot', pivot)

# DRIVER CODE
LL = Linked_list()
LL.add(5)
LL.add(1)
LL.add(8)
LL.add(0)
LL.add(3)

print(LL)

LL.pivot(3)

print(LL)