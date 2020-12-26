"""
Problem:

Given the root of a binary search tree, and a target K, return two nodes in the tree
whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""

from typing import Generator, Optional, Tuple

from DataStructures.Tree import BinaryTree, Node


def inorder_traverse_generator(node: Node) -> Generator[int, None, None]:
    if node.left:
        for val in inorder_traverse_generator(node.left):
            yield val
    yield node.val
    if node.right:
        for val in inorder_traverse_generator(node.right):
            yield val


def get_inorder_traverse_generator(
    tree: BinaryTree,
) -> Optional[Generator[int, None, None]]:
    if tree.root:
        return inorder_traverse_generator(tree.root)
    return None


def get_target_sum(tree: BinaryTree, k: int) -> Tuple[Optional[int], Optional[int]]:
    generator = get_inorder_traverse_generator(tree)
    if not generator:
        return None, None
    # checking for the target sum
    previous = set()
    for val in generator:
        if (k - val) in previous:
            return (k - val), val
        previous.add(val)
    return None, None


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(10)

    tree.root.left = Node(5)
    tree.root.right = Node(15)

    tree.root.right.left = Node(11)
    tree.root.right.right = Node(15)

    print(get_target_sum(tree, 15))
    print(get_target_sum(tree, 20))
    print(get_target_sum(tree, 21))
    print(get_target_sum(tree, 25))
    print(get_target_sum(tree, 30))
    print(get_target_sum(tree, 35))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
