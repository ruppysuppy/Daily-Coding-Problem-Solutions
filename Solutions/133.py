"""
Problem:

Given a node in a binary tree, return the next bigger element, also known as the
inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""

from typing import Optional

from DataStructures.Tree import Node, BinarySearchTree


def inorder_successor_helper(node: Node) -> Optional[int]:
    # using bst property to find the inorder successor
    if node.right:
        pos = node.right
        while pos.left:
            pos = pos.left
        return pos.val
    if node.parent:
        return node.parent.val
    return None


def inorder_successor(node: Node) -> Optional[int]:
    if not node:
        return
    return inorder_successor_helper(node)


# adding the parent pointer to Node class
setattr(Node, "parent", None)

if __name__ == "__main__":
    a = Node(10)
    b = Node(5)
    c = Node(30)
    d = Node(22)
    e = Node(35)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    b.parent = a
    c.parent = a
    d.parent = c
    e.parent = c

    tree = BinarySearchTree()
    tree.root = a

    print(tree)
    print(inorder_successor(d))
    print(inorder_successor(a))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
