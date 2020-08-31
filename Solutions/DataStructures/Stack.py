class Stack:
    """
    Stack Class for LIFO Structure

    Functions:
    is_empty: Check if the stack is empty
    peek: Get the value at the stack top without removing it
    pop: Pop the object at the top of the stack
         Raises erorr if the stack is empty
    push: Push an object to the top of the stack
    """

    def __init__(self) -> None:
        self.stack = []
        self.rear = -1
        self.top = -1

    def __repr__(self) -> str:
        return str(self.stack)

    def __len__(self) -> int:
        return len(self.stack)

    def peek(self) -> int:
        # Get the value at the stack top without removing it
        if self.is_empty():
            raise Exception("Stack Underflow. Cannot peek at an empty stack")
        return self.stack[-1]

    def pop(self) -> int:
        # Pop the value at the stack top
        if self.rear == -1:
            raise Exception("Stack Underflow. Cannot pop from an empty stack")
        elif self.top == 0:
            self.rear = -1
            self.top = -1
        else:
            self.top -= 1
        return self.stack.pop()

    def push(self, val: int) -> None:
        # Push a new value to the stack top
        if self.rear == -1:
            self.stack.append(val)
            self.rear = 0
            self.top = 0
        else:
            self.stack.append(val)
            self.top += 1

    def is_empty(self) -> bool:
        # Check if the stack is empty
        return not bool(self.stack)
