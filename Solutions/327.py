"""
Problem:

Write a program to merge two binary trees. Each node in the new tree should hold a
value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the
new tree should match that input node.
"""

from DataStructures.Tree import BinaryTree, Node


def merge_trees_helper(node: Node, node1: Node, node2: Node) -> None:
    n1_l_val, n1_r_val = 0, 0
    n2_l_val, n2_r_val = 0, 0
    n1_l, n1_r = None, None
    n2_l, n2_r = None, None
    # tree1 node related data generation
    if node1:
        if node1.left:
            n1_l_val = node1.left.val
            n1_l = node1.left
        if node1.right:
            n1_r_val = node1.right.val
            n1_r = node1.right
    # tree2 node related data generation
    if node2:
        if node2.left:
            n2_l_val = node2.left.val
            n2_l = node2.left
        if node2.right:
            n2_r_val = node2.right.val
            n2_r = node2.right
    # left node generation
    if n1_l is not None or n2_l is not None:
        node.left = Node(n1_l_val + n2_l_val)
        merge_trees_helper(node.left, n1_l, n2_l)
    # right node generation
    if n1_r is not None or n2_r is not None:
        node.right = Node(n1_r_val + n2_r_val)
        merge_trees_helper(node.right, n1_r, n2_r)


def merge_trees(tree1: BinaryTree, tree2: BinaryTree) -> BinaryTree:
    tree = BinaryTree()
    if not tree1.root and not tree2.root:
        return tree
    # root generation
    r1, r2 = 0, 0
    if tree1.root:
        r1 = tree1.root.val
    if tree2.root:
        r2 = tree2.root.val
    tree.root = Node(r1 + r2)
    # generating rest of the tree
    merge_trees_helper(tree.root, tree1.root, tree2.root)
    return tree


if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.right = Node(4)
    print(tree1)

    tree2 = BinaryTree()
    tree2.root = Node(2)
    tree2.root.right = Node(-3)
    tree2.root.right.right = Node(10)
    print(tree2)

    print(merge_trees(tree1, tree2))


"""
SPECS:

TIME COMPLEXITY: O(nodes_tree1 + nodes_tree2)
SPACE COMPLEXITY: O(height_tree1 + height_tree2)
"""
