"""
Problem:

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

from typing import Optional

from DataStructures.LinkedList import Node, LinkedList


def sorted_merge(node: Node, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    if a is None:
        return b
    if b is None:
        return a

    result = None
    if a.val <= b.val:
        result = a
        result.next = sorted_merge(node, a.next, b)
    else:
        result = b
        result.next = sorted_merge(node, a, b.next)
    return result


def merge_sort(ll: LinkedList, h: Optional[Node]) -> Optional[Node]:
    if h is None or h.next is None:
        return h

    middle = get_middle(ll, h)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(ll, h)
    right = merge_sort(ll, next_to_middle)

    sortedlist = sorted_merge(ll, left, right)
    return sortedlist


def get_middle(ll: LinkedList, head: Optional[Node]) -> Optional[Node]:
    # searching for the middle of the linked list using fast pointer slow pointer
    if head == None:
        return head

    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def sort(ll: LinkedList) -> LinkedList:
    ll.head = merge_sort(ll, ll.head)
    # reseting rear
    curr = ll.head
    while curr.next:
        curr = curr.next
    ll.rear = curr
    return ll


if __name__ == "__main__":
    LL = LinkedList()

    for val in [6, 3, 7, 5, 30, 2, 50]:
        LL.add(val)

    print(LL)
    sort(LL)
    print(LL)
    print()

    LL = LinkedList()

    for val in [4, 1, -3, 99]:
        LL.add(val)

    print(LL)
    sort(LL)
    print(LL)


"""
SPECS:

TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(n)
"""
