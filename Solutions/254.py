"""
Probelm:

Recall that a full binary tree is one in which each node is either a leaf node, or has
two children. Given a binary tree, convert it to a full one by removing nodes with only
one child.

For example, given the following tree:

         a
      /     \
    b         c
  /            \
d                 e
  \             /   \
    f          g     h
You should convert it to:

     a
  /     \
f         e
        /   \
       g     h
"""

from DataStructures.Tree import Node, BinaryTree


def create_full_bin_tree_helper(node: Node) -> None:
    # if a node with one missing child is encountered, the value is replaced by its
    # child and the children of the current node overwritten with the child's children
    if node.right is None and node.left is None:
        return
    elif node.left is not None and node.right is None:
        node.val = node.left.val
        node.right = node.left.right
        node.left = node.left.left
        create_full_bin_tree_helper(node)
    elif node.left is None and node.right is not None:
        node.val = node.right.val
        node.left = node.right.left
        node.right = node.right.right
        create_full_bin_tree_helper(node)
    elif node.left is not None and node.right is not None:
        create_full_bin_tree_helper(node.left)
        create_full_bin_tree_helper(node.right)


def create_full_bin_tree(tree: BinaryTree) -> None:
    if tree.root:
        create_full_bin_tree_helper(tree.root)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node("a")

    tree.root.left = Node("b")
    tree.root.right = Node("c")

    tree.root.left.left = Node("d")
    tree.root.left.left.right = Node("f")

    tree.root.right.right = Node("e")

    tree.root.right.right.left = Node("g")
    tree.root.right.right.right = Node("h")

    print(tree)

    create_full_bin_tree(tree)

    print(tree)


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
