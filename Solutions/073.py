"""
Problem:

Given the head of a singly linked list, reverse it in-place.
"""

# importing the linked list
from DataStructures.LinkedList import Linked_list

# FUNCTION TO PERFORM THE OPERATION
def reverse_inplace(LL):
    # setting the rear pointer
    LL.rear = LL.head

    # using 3 pointers (ptr1 points the previous node, ptr2 the current node and ptr3 the next node)
    ptr1 = None
    ptr2 = LL.head
    ptr3 = LL.head.next

    # looping over till we reach the end of the linked list
    while ptr2 != None:
        # reversing the flow (ptr2 -> ptr1)
        ptr2.next = ptr1

        # updating the pointers to their next locations
        ptr1 = ptr2
        ptr2 = ptr3
        if ptr3 == None:
            break
        ptr3 = ptr3.next

    # setting the head of the linked list
    LL.head = ptr1


# DRIVER CODE
LL = Linked_list()

LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)
LL.add(6)
LL.add(7)
LL.add(8)

print(LL)

reverse_inplace(LL)

print(LL)
