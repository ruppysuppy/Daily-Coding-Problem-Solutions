"""
Problem:

Implement locking in a binary tree. A binary tree node can be locked or unlocked only
if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked. lock, which attempts to lock the
node. If it cannot be locked, then it should return false. Otherwise, it should lock it
and return true. unlock, which unlocks the node. If it cannot be unlocked, then it
should return false. Otherwise, it should unlock it and return true. You may augment
the node to add parent pointers or any other property you would like. You may assume
the class is used in a single-threaded program, so there is no need for actual locks or
mutexes. Each method should run in O(h), where h is the height of the tree.
"""

from DataStructures.Tree import Node, BinaryTree


class NodeWithLock(Node):
    """
    Binary Tree Node with locking mechanism

    Functions:
    is_locked: check if the current node is locked
    lock: locks the current node
    unlock: unlocks the current node
    _is_any_parent_unlocked: helper function to check if any parent is unlocked
    _is_any_descendant_unlocked: helper function to check if any of the descendant is
            unlocked
    """

    def __init__(self, val: int) -> None:
        Node.__init__(self, val)
        self.locked = False
        self.parent = None

    def __str__(self) -> str:
        curr_node = f"{self.val}, {'locked' if self.locked else 'unlocked'}"
        left, right = "", ""
        if self.left:
            left = f"{self.left} "
        if self.right:
            right = f" {self.right}"
        return f"({left} {curr_node} {right})"

    def is_locked(self) -> bool:
        return self.locked

    def lock(self) -> bool:
        is_any_parent_unlocked = self._is_any_parent_unlocked()
        is_any_descendant_unlocked = self._is_any_descendant_unlocked()
        if is_any_parent_unlocked or is_any_descendant_unlocked:
            self.locked = True
            return True
        return False

    def unlock(self) -> bool:
        is_any_parent_unlocked = self._is_any_parent_unlocked()
        is_any_descendant_unlocked = self._is_any_descendant_unlocked()
        if is_any_parent_unlocked or is_any_descendant_unlocked:
            self.locked = False
            return True
        return False

    def _is_any_parent_unlocked(self) -> bool:
        # time complexity: O(log(n))
        node = self
        while node.parent:
            if not node.is_locked():
                return True
            node = node.parent
        return False

    def _is_any_descendant_unlocked(self) -> bool:
        # time complexity: O(log(n))
        if not self.is_locked():
            return True

        if self.left:
            left = self.left._is_any_descendant_unlocked()
        else:
            left = False
        if self.right:
            right = self.right._is_any_descendant_unlocked()
        else:
            right = False
        return left or right


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = NodeWithLock(5)

    tree.root.left = NodeWithLock(3)
    tree.root.left.parent = tree.root
    tree.root.right = NodeWithLock(18)
    tree.root.right.parent = tree.root

    tree.root.left.left = NodeWithLock(0)
    tree.root.left.left.parent = tree.root.left

    print(tree)

    print()
    print(tree.root.left.left.lock())
    print(tree.root.left.lock())
    print(tree.root.lock())
    print()

    print(tree)

    print()
    print(tree.root.left.unlock())
    print()

    print(tree)

    print()
    print(tree.root.unlock())
    print()

    print(tree)
