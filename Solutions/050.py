"""
Problem:

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and
each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

from __future__ import annotations
from typing import Callable, Optional, Union

from DataStructures.Tree import BinaryTree, Node


# symbol to function map
OPERATIONS_DICT = {
    "+": lambda num1, num2: num1 + num2,
    "-": lambda num1, num2: num1 - num2,
    "*": lambda num1, num2: num1 * num2,
    "/": lambda num1, num2: num1 / num2,
}


class ExpressionTreeNode(Node):
    def __init__(
        self,
        val: Union[int, float, str, Callable],
        left: Optional[ExpressionTreeNode] = None,
        right: Optional[ExpressionTreeNode] = None,
    ) -> None:
        Node.__init__(self, val, left, right)

    def transform_helper(self) -> None:
        if self.val in OPERATIONS_DICT:
            self.val = OPERATIONS_DICT[self.val]
            self.left.transform_helper()
            self.right.transform_helper()

    def calculate_helper(self) -> Union[int, float]:
        if callable(self.val):
            return self.val(self.left.calculate_helper(), self.right.calculate_helper())
        return self.val


def calculate_expression_tree(tree: BinaryTree) -> Union[int, float]:
    root = tree.root
    if root:
        root.transform_helper()
        return root.calculate_helper()
    return None


if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = ExpressionTreeNode("*")
    tree.root.left = ExpressionTreeNode("+")
    tree.root.right = ExpressionTreeNode("+")

    tree.root.left.left = ExpressionTreeNode(3)
    tree.root.left.right = ExpressionTreeNode(2)

    tree.root.right.left = ExpressionTreeNode(4)
    tree.root.right.right = ExpressionTreeNode(5)

    print(calculate_expression_tree(tree))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(log(n))
"""
