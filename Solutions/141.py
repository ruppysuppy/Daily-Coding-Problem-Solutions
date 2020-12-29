"""
Problem:

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
"""


class Stack:
    def __init__(self) -> None:
        self.list = []
        self.stack1_last_index = 0
        self.stack2_last_index = 0
        self.stack3_last_index = 0

    def __repr__(self) -> str:
        return (
            f"Stack1: {self.list[:self.stack1_last_index]}"
            + f"\nStack2: {self.list[self.stack1_last_index:self.stack2_last_index]}"
            + f"\nStack3: {self.list[self.stack2_last_index:]}"
        )

    def pop(self, stack_number: int) -> int:
        if stack_number == 1:
            if len(self.list[: self.stack1_last_index]) == 0:
                raise ValueError("Stack Underflow")
            self.list.pop(self.stack1_last_index - 1)
            self.stack1_last_index -= 1
            self.stack2_last_index -= 1
            self.stack3_last_index -= 1
        elif stack_number == 2:
            if len(self.list[self.stack1_last_index : self.stack2_last_index]) == 0:
                raise ValueError("Stack Underflow")
            self.list.pop(self.stack2_last_index - 1)
            self.stack2_last_index -= 1
            self.stack3_last_index -= 1
        elif stack_number == 3:
            if len(self.list[self.stack2_last_index :]) == 0:
                raise ValueError("Stack Underflow")
            self.list.pop()
            self.stack3_last_index -= 1

    def push(self, item: int, stack_number: int) -> None:
        if stack_number == 1:
            self.list.insert(self.stack1_last_index, item)
            self.stack1_last_index += 1
            self.stack2_last_index += 1
            self.stack3_last_index += 1
        elif stack_number == 2:
            self.list.insert(self.stack2_last_index, item)
            self.stack2_last_index += 1
            self.stack3_last_index += 1
        elif stack_number == 3:
            self.list.insert(self.stack3_last_index, item)
            self.stack3_last_index += 1


if __name__ == "__main__":
    stack = Stack()
    stack.push(5, 3)
    stack.push(10, 2)
    stack.push(1, 1)

    print(stack)
    print()

    stack.push(3, 3)
    stack.push(1, 2)
    stack.push(0, 2)

    print(stack)
    print()

    stack.pop(2)
    stack.pop(1)
    stack.pop(3)

    print(stack)
