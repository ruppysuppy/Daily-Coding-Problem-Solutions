'''
Problem:

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
'''

# importing LinkedList from the DataStructures
from DataStructures.LinkedList import Linked_list

# FUNCTION TO PERFORM THE OPERATION
def merge_sorted_linked_list(list_of_LL, k):
    # pos list to store the current location on each of the linked list
    # sorted_list stores the final sorted linked list
    pos = [LL.head for LL in list_of_LL]
    sorted_list = Linked_list()

    # lopping over the pos list till all the position pointers reach the end (None) of the Linked List
    while any(pos):
        # initializing a random large minimum value (pererably use sys.INT_MAX)
        minimum = 9999

        # looping over the position pointers
        for i in range(k):
            # if the pointer is not None and the value is less than the minimum, position & minimum is updated
            if (pos[i] != None):
                if (pos[i].val < minimum):
                    minimum = pos[i].val
                    position = i

        # the value is added to the sorted Linked List
        sorted_list.add(pos[position].val)
        # the position pointer is moved to the next value
        pos[position] = pos[position].next
    
    return sorted_list

# DRIVER CODE
LL1 = Linked_list()
LL1.add(2)
LL1.add(25)
LL1.add(70)

LL2 = Linked_list()
LL2.add(5)
LL2.add(8)
LL2.add(14)
LL2.add(15)
LL2.add(21)
LL2.add(48)

LL3 = Linked_list()
LL3.add(0)
LL3.add(90)

print(LL1)
print(LL2)
print(LL3)

List = [LL1, LL2, LL3]
print(merge_sorted_linked_list(List, len(List)))