"""
Problem:

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the
constraint that the key in the left child must be less than or equal to the root and
the key in the right child must be greater than or equal to the root.
"""

from DataStructures.Tree import BinaryTree, BinarySearchTree, Node


def is_binary_search_tree_helper(node: Node) -> bool:
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    elif (node.left and node.left.val > node.val) or (
        node.right and node.right.val < node.val
    ):
        return False
    return is_binary_search_tree_helper(node.left) and is_binary_search_tree_helper(
        node.right
    )


def is_binary_search_tree(tree: BinaryTree) -> bool:
    return is_binary_search_tree_helper(tree.root)


if __name__ == "__main__":
    tree1 = BinarySearchTree()

    tree1.add(5)
    tree1.add(9)
    tree1.add(1)
    tree1.add(4)
    tree1.add(10)
    tree1.add(3)
    tree1.add(2)
    tree1.add(10)
    tree1.add(7)

    print(is_binary_search_tree(tree1))

    tree2 = BinaryTree()
    tree2.root = Node(5)

    tree2.root.left = Node(4)
    tree2.root.right = Node(6)

    print(is_binary_search_tree(tree2))

    tree3 = BinaryTree()
    tree3.root = Node(5)

    tree3.root.left = Node(6)
    tree3.root.right = Node(4)

    print(is_binary_search_tree(tree3))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n)) [recursion depth]
"""
