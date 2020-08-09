"""
Problem:

Given a linked list and a positive integer k, rotate the list to the right by k places.

Example:

Linked list = 7 -> 7 -> 3 -> 5
k = 2
Output = 3 -> 5 -> 7 -> 7

Linked list = 1 -> 2 -> 3 -> 4 -> 5
k = 3
Output = 3 -> 4 -> 5 -> 1 -> 2
"""

# importing the necessary classes
from DataStructures.LinkedList import Linked_list, Node

# FUNCTION TO PERFORM THE OPERATION
def rot_right(self, k=0):
    # getting the number of rotations to be performed
    k = k % self.length

    # shifting the element from head to the rear of the linked list
    for _ in range(k):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.rear.next = temp
        self.rear = self.rear.next


# binding the function to the linked list class
setattr(Linked_list, "rot_right", rot_right)

# DRIVER CODE
LL = Linked_list()
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)

print(LL)

LL.rot_right(3)

print(LL)
