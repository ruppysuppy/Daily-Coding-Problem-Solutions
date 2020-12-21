"""
Problem:

Given two non-empty binary trees s and t, check whether tree t has exactly the same
structure and node values with a subtree of s. A subtree of s is a tree consists of a
node in s and all of this node's descendants. The tree s could also be considered as a
subtree of itself.
"""

from DataStructures.Tree import BinaryTree, Node


def is_equal(node1: Node, node2: Node) -> bool:
    if (not node1) and (not node2):
        return True
    if (not node1) or (not node2):
        return False
    if node1.val != node2.val:
        return False
    return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)


def find_helper(sub_tree1: Node, sub_tree2: Node) -> bool:
    if is_equal(sub_tree1, sub_tree2):
        return True
    # if the subtree is not same, the children are checked
    if sub_tree1.left and find_helper(sub_tree1.left, sub_tree2):
        return True
    if sub_tree1.right and find_helper(sub_tree1.right, sub_tree2):
        return True
    return False


def get_match(s: BinaryTree, t: BinaryTree) -> bool:
    if s.root and t.root:
        return find_helper(s.root, t.root)
    return False


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(0)
    tree1.root.left = Node(1)
    tree1.root.right = Node(2)
    tree1.root.right.left = Node(3)
    tree1.root.right.right = Node(4)

    tree2 = BinaryTree()
    tree2.root = Node(2)
    tree2.root.left = Node(3)
    tree2.root.right = Node(4)

    tree3 = BinaryTree()
    tree3.root = Node(2)
    tree3.root.left = Node(3)
    tree3.root.right = Node(5)

    print(get_match(tree1, tree2))
    print(get_match(tree1, tree3))


"""
SPECS:

TIME COMPLEXITY: O(2 ^ n)
SPACE COMPLEXITY: O(log(n))
"""
