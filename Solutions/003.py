"""
Problem:

Write a program to serialize a tree into a string and deserialize a string into a tree.
"""

from typing import List

from DataStructures.Tree import Node, BinaryTree


def serialize_helper(node: Node) -> str:
    # helper function to serialize a binary tree (uses prefix traversal)
    # data is padded with single quotes (') and comma (,) is used as a delimiter
    if node.right is None and node.left is None:
        return f"'{node.val}','None','None'"
    elif node.left is not None and node.right is None:
        return f"'{node.val}',{serialize_helper(node.left)},'None'"
    elif node.left is None and node.right is not None:
        return f"'{node.val}','None',{serialize_helper(node.right)}"
    elif node.left is not None and node.right is not None:
        return (
            f"'{node.val}',"
            + f"{serialize_helper(node.left)},"
            + f"{serialize_helper(node.right)}"
        )


def serialize(tree: BinaryTree) -> str:
    # function to serialize a binary tree
    return serialize_helper(tree.root)


def deserialize_helper(node: Node, data: List[str]) -> Node:
    # function to deserialize the string
    # data is a queue containing the data as a prefix notation can be easily decoded
    # using a queue
    left = data.pop(0).strip("'")
    if left != "None":
        # if the left child exists, its added to the tree
        node.left = Node(left)
        node.left = deserialize_helper(node.left, data)

    right = data.pop(0).strip("'")
    if right != "None":
        # if the right child exists, its added to the tree
        node.right = Node(right)
        node.right = deserialize_helper(node.right, data)
    return node


def deserialize(string: str) -> BinaryTree:
    # function to deserialize a string into a binary tree
    # the string is considered to have the same format as the binary tree serialization
    # eg: data is padded with single quotes (') and comma (,) is used as a delimiter
    data = string.split(",")
    tree = BinaryTree()
    tree.root = Node(data.pop(0).strip("'"))
    deserialize_helper(tree.root, data)
    return tree


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node("root")

    tree.root.left = Node("left")
    tree.root.right = Node("right")

    tree.root.left.left = Node("left.left")

    print(serialize(tree))

    generated_tree = deserialize(
        "'root','left','left.left','None','None','None','right','None','None'"
    )

    print(serialize(generated_tree))


"""
SPECS:

SERIALIZE: (n = Number of Nodes)
TIME COMPLEXITY: O(n) 
SPACE COMPLEXITY: O(n)

DESERIALIZE: (n = Number of Characters in the String)
TIME COMPLEXITY: O(n) 
SPACE COMPLEXITY: O(n)
"""
