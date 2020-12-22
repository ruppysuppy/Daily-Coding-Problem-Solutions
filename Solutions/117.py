"""
Problem:

Given a binary tree, return the level of the tree with minimum sum.
"""

from sys import maxsize

from DataStructures.Queue import Queue
from DataStructures.Tree import BinaryTree, Node


def get_level_min_sum(tree: BinaryTree) -> int:
    if not tree.root:
        return 0
    # the levels are delimited in the queue by None
    queue = Queue()
    queue.enqueue(tree.root)
    queue.enqueue(None)

    min_level_sum = maxsize
    curr_level_sum = 0
    while not queue.is_empty():
        node = queue.dequeue()
        if node is not None:
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            curr_level_sum += node.val
        else:
            min_level_sum = min(curr_level_sum, min_level_sum)
            if len(queue) > 0:
                queue.enqueue(None)
                curr_level_sum = 0
    return min_level_sum


if __name__ == "__main__":
    a = Node(100)
    b = Node(200)
    c = Node(300)
    d = Node(400)
    e = Node(500)
    f = Node(600)
    g = Node(700)
    h = Node(800)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.left = f
    c.right = g

    d.right = h

    tree = BinaryTree()
    tree.root = a

    print(tree)
    print(get_level_min_sum(tree))
    a.val = 1000
    print(tree)
    print(get_level_min_sum(tree))
    b.val = 1500
    print(tree)
    print(get_level_min_sum(tree))
    h.val = 2000
    print(tree)
    print(get_level_min_sum(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
