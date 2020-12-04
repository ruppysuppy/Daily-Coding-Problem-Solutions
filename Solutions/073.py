"""
Problem:

Given the head of a singly linked list, reverse it in-place.
"""

from DataStructures.LinkedList import LinkedList


def reverse_inplace(ll: LinkedList) -> None:
    ll.rear = ll.head
    ptr_prev, ptr_curr, ptr_next = None, ll.head, ll.head.next
    # reversing the flow
    while ptr_curr is not None:
        ptr_curr.next = ptr_prev
        ptr_prev, ptr_curr = ptr_curr, ptr_next
        if ptr_next is None:
            break
        ptr_next = ptr_next.next
    ll.head = ptr_prev


if __name__ == "__main__":
    ll = LinkedList()
    for num in range(1, 6):
        ll.add(num)
    print(ll)
    reverse_inplace(ll)
    print(ll)

    ll = LinkedList()
    for num in range(1, 3):
        ll.add(num)
    print(ll)
    reverse_inplace(ll)
    print(ll)

    ll = LinkedList()
    for num in range(1, 2):
        ll.add(num)
    print(ll)
    reverse_inplace(ll)
    print(ll)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
