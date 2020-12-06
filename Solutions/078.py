"""
Problem:

Given k sorted singly linked lists, write a function to merge all the lists into one
sorted singly linked list.
"""

from sys import maxsize
from typing import List

from DataStructures.LinkedList import LinkedList, Node


def merge_sorted_linked_list(list_of_LL: List[LinkedList]) -> LinkedList:
    k = len(list_of_LL)
    position_arr = [LL.head for LL in list_of_LL]
    sorted_ll = LinkedList()
    while any(position_arr):
        # finding the node with minimum value
        minimum = maxsize
        for i in range(k):
            if position_arr[i] is not None:
                if position_arr[i].val < minimum:
                    minimum = position_arr[i].val
                    position = i
        # generating new node
        if sorted_ll.head is None:
            sorted_ll.add(position_arr[position].val)
            curr_position = sorted_ll.head
        else:
            curr_position.next = Node(position_arr[position].val)
            curr_position = curr_position.next
        sorted_ll.length += 1
        position_arr[position] = position_arr[position].next
    # resetting rear
    sorted_ll.rear = curr_position
    return sorted_ll


if __name__ == "__main__":
    LL1 = LinkedList()
    LL1.add(2)
    LL1.add(25)
    LL1.add(70)

    LL2 = LinkedList()
    LL2.add(5)
    LL2.add(8)
    LL2.add(14)
    LL2.add(15)
    LL2.add(21)
    LL2.add(48)

    LL3 = LinkedList()
    LL3.add(0)
    LL3.add(90)

    print(LL1)
    print(LL2)
    print(LL3)

    List = [LL1, LL2, LL3]
    print(merge_sorted_linked_list(List))


"""
SPECS:

TIME COMPLEXITY: O(n + k)
SPACE COMPLEXITY: O(n + k)
[n = total number of nodes]
"""
