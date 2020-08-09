class Stack:
    """
    Stack Class for the implementation of a stack

    Functions:
    isEmpty: Check if the stack is empty
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

    def isEmpty(self) -> bool:
        # Check if the stack is empty
        return bool(self.stack)
