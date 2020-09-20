"""
Problem:

Given a linked list, remove all consecutive nodes that sum to zero. Print out the
remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this
case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""

from DataStructures.LinkedList import Node, LinkedList


def delete_zero_sum(linked_list: LinkedList) -> LinkedList:
    cumulative = 0
    cumulative_sum_map = {}
    dummy_head = Node(0)
    dummy_head.next = linked_list.head
    linked_list.head = dummy_head
    # removing 0 sum nodes using the property:
    # x -> y -> x [values (x and y) are cumulative sums] implies the linked list
    # contains x -> (y - x) -> -(y - x) and hence the nodes at the end can be removed
    # [this property can also be used to detect multiple nodes summing up to 0]
    node = linked_list.head
    while node:
        cumulative += node.val
        if cumulative in cumulative_sum_map:
            cumulative_sum_map[cumulative].next = node.next
        cumulative_sum_map[cumulative] = node
        node = node.next
    # resetting the linked list (removing dummy head and setting rear)
    linked_list.head = linked_list.head.next
    node = linked_list.head
    while node:
        linked_list.rear = node
        node = node.next
    return linked_list


if __name__ == "__main__":
    linked_list = LinkedList()
    for elem in [3, 4, -7, 5, -6, 6]:
        linked_list.add(elem)
    print(delete_zero_sum(linked_list))

    linked_list = LinkedList()
    for elem in [7, 4, -4, -7, 5, -6, 6]:
        linked_list.add(elem)
    print(delete_zero_sum(linked_list))

    linked_list = LinkedList()
    for elem in [7, 4, -4, -7, 5, -6, 6, 10]:
        linked_list.add(elem)
    print(delete_zero_sum(linked_list))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
