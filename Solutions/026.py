"""
Problem:

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

from DataStructures.LinkedList import Node, LinkedList


def delete_kth_last_node(ll: LinkedList, k: int) -> None:
    # case for head node removal
    if k == len(ll):
        temp = ll.head
        if len(ll) == 1:
            ll.head = None
            ll.rear = None
        else:
            ll.head = temp.next
            temp.next = None
        ll.length -= 1
        del temp
        return
    # generic node removal
    ptr_end = ll.head
    ptr_k = ll.head
    # moving the ptr_end up by k nodes
    for _ in range(k + 1):
        if ptr_end is None:
            raise ValueError(f"Linked list contains less than {k} nodes")
        ptr_end = ptr_end.next
    # searching for the end of the linked list
    # ptr_k is trailing the ptr_end up by k nodes, when end pointer reaches the end,
    # ptr_k is k nodes away from the end
    while ptr_end is not None:
        ptr_end = ptr_end.next
        ptr_k = ptr_k.next
    # removing the required element
    temp = ptr_k.next
    ptr_k.next = temp.next
    temp.next = None
    ll.length -= 1
    del temp


if __name__ == "__main__":
    ll1 = LinkedList()
    for i in range(1, 10):
        ll1.add(i)
    print(ll1)
    delete_kth_last_node(ll1, 5)
    print(ll1)

    ll2 = LinkedList()
    for i in range(1, 4):
        ll2.add(i)
    print(ll2)
    delete_kth_last_node(ll2, 3)
    print(ll2)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
