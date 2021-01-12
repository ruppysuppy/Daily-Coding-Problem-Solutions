"""
Problem:

Given a stack of N elements, interleave the first half of the stack with the second
half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the
stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""

from DataStructures.Stack import Stack
from DataStructures.Queue import Queue


def interleave(stack: Stack) -> Stack:
    queue = Queue()
    # interleaving the elements
    for i in range(1, len(stack)):
        for _ in range(i, len(stack)):
            queue.enqueue(stack.pop())
        for _ in range(len(queue)):
            stack.push(queue.dequeue())
    return stack


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)
    print(interleave(stack))
    print()

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack)
    print(interleave(stack))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
