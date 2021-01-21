"""
Problem:

Given a linked list of numbers and a pivot k, partition the linked list so that all
nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could
be 1 -> 0 -> 5 -> 8 -> 3.
"""

from DataStructures.LinkedList import Node, LinkedList


def pivot_linked_list(ll: LinkedList, k: int) -> None:
    ptr1, ptr2 = ll.head, ll.head
    length = len(ll)
    k = k % length
    for _ in range(length):
        if ptr2.val < k:
            ptr1.val, ptr2.val = ptr2.val, ptr1.val
            ptr1 = ptr1.next
        ptr2 = ptr2.next


if __name__ == "__main__":
    LL = LinkedList()
    LL.add(5)
    LL.add(1)
    LL.add(8)
    LL.add(0)
    LL.add(3)

    print(LL)

    pivot_linked_list(LL, 3)

    print(LL)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
