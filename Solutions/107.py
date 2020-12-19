"""
Problem:

Print the nodes in a binary tree level-wise. For example, the following should print
1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

from typing import List

from DataStructures.Queue import Queue
from DataStructures.Tree import BinaryTree, Node


def get_lvl_wise_nodes(tree: BinaryTree) -> List[Node]:
    # using bfs to generate the list of nodes by level
    if not tree.root:
        return []

    queue = Queue()
    queue.enqueue(tree.root)
    ans = []
    while not queue.is_empty():
        node = queue.dequeue()
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)
        ans.append(node.val)
    return ans


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)

    print(f"Tree: {tree}")
    print(f"Level wise result: {get_lvl_wise_nodes(tree)}")


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
