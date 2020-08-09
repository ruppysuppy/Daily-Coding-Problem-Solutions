"""
Problem:

You are given the head to a singly linked list, where each node also has a 'random' pointer that points to anywhere in the linked list. 
Deep clone the list.
"""

# local import from the Datastructure module
from DataStructures.LinkedList import Linked_list, Node

# function to join the random pointers of element at pos1 to the element at pos2
def rand_join(self, pos1, pos2):
    # pos_source points to the node whose random pointer is being set
    pos_source = self.head
    # pos_dest points to the node where the random pointer points to
    pos_dest = self.head

    try:
        # moving the pointers to the required positions
        for _ in range(pos1):
            pos_source = pos_source.next

        for _ in range(pos2):
            pos_dest = pos_dest.next

        # setting the random pointer
        pos_source.random_ptr = pos_dest

    except:
        # raising Index Error if the poition is out of range
        raise IndexError("Given position is out of the Linked List")


# FUNCTION TO PERFORM THE OPERATION
def clone(self):
    # clone head tracks the head of the cloned list
    clone_head = self.head
    # pos1 stores the current position
    pos1 = self.head
    # pos2 stores the position of the next element (needed as the linked list is repeatedly broken and reacttached)
    pos2 = self.head.next

    # duplicating all elements (by value in the linked list) [a->b->c becomes a->a->b->b->c->c]
    for _ in range(self.length):
        pos1.next = Node(pos1.val)
        pos1 = pos1.next
        pos1.next = pos2
        pos1 = pos1.next
        if pos2 != None:
            pos2 = pos2.next
        else:
            break

    # setting the clone head to the proper position
    clone_head = clone_head.next
    # pos1 stores the current element of the linked list
    pos1 = self.head

    # setting the random pointer of the cloned linked list (every 2nd element in the new linked list: a->[a]->b->[b]->c->[c])
    for _ in range(self.length - 1):
        pos1.next.random_ptr = pos1.random_ptr
        pos1 = pos1.next.next

    # pos1 stores the current position (original linked list)
    pos1 = self.head
    # pos2 stores the current position (cloned linked list)
    pos2 = self.head.next

    # reverting the linked list to its original form
    for _ in range(self.length - 1):
        pos1.next = pos2.next
        pos2.next = pos2.next.next
        pos1 = pos1.next
        if pos2.next == None:
            break
        else:
            pos2 = pos2.next

    # creating the cloned linked list from the cloned head, pos2 (points to the rear) and length of original linked list
    cloned_LL = Linked_list()
    cloned_LL.head = clone_head
    cloned_LL.length = self.length
    cloned_LL.rear = pos2

    return cloned_LL


# adding the necessary functions and variables to the classes
setattr(Node, "random_ptr", None)
setattr(Linked_list, "rand_join", rand_join)
setattr(Linked_list, "clone", clone)

# DRIVER CODE
LL = Linked_list()

LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)

LL.rand_join(0, 2)
LL.rand_join(2, 0)
LL.rand_join(1, 3)

print("Original List:", LL)

LL_clone = LL.clone()

print("Cloned List:", LL_clone)

# adding different elements to show that the clone is a deep copy
LL.add(100)
LL_clone.add(5)

print("\nOriginal List:", LL)

print("Cloned List:", LL_clone)
