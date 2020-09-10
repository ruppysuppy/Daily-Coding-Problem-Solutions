"""
Problem:

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""

# Importing from the local module
from DataStructures.LinkedList import Node, Linked_list

# FUNCTION TO PERFORM THE OPERATION
def del_LL_k(LL, k):
    # Creating necessary vaibales
    # ptr1 -> finds the end, ptr2 -> finds the k'th last element, iterations -> tracks the number of iterations
    ptr1 = LL.head
    ptr2 = LL.head
    iterations = 0

    # Looping over till the end of the linked list
    while ptr1.next:
        ptr1 = ptr1.next
        iterations += 1

        # If at least k iterations has been made, ptr2 is moved to the next node in each iteration
        # So ptr2 trails ptr1 by k nodes
        if iterations >= k:
            ptr2 = ptr2.next

    # Storing the reference (as it needs to be deleted after the reference is removed)
    temp = ptr2.next

    # Updating the values
    ptr2.val = ptr2.next.val
    ptr2.next = ptr2.next.next

    # Deleting using the stored refernce
    del temp


# DRIVER CODE
LL = Linked_list()
LL.add(5)
LL.add(6)
LL.add(7)
LL.add(8)
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)

print(LL)

del_LL_k(LL, 5)

print(LL)
