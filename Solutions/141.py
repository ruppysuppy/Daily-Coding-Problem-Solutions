'''
Problem:

Implement 3 stacks using a single list:
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
'''

# stack class
class Stack:
    # initialization
    def __init__(self):
        self.list = []
        # pos1 stores the starting index of stack 1
        # pos2 stores the starting index of stack 2
        # pos3 stores the starting index of stack 3
        self.pos1 = 0
        self.pos2 = 0
        self.pos3 = 0

    # pop function
    def pop(self, stack_number):
        if (stack_number == 1):
            # calculating the length and checking for underflow
            if (len(self.list[:self.pos1]) == 0):
                raise ValueError("Stack Underflow")
            # getting the necessary value
            self.list.pop(self.pos1-1)
            # updating the position markers
            self.pos1 -= 1
            self.pos2 -= 1
            self.pos3 -= 1
        elif (stack_number == 2):
            # calculating the length and checking for underflow
            if (len(self.list[self.pos1:self.pos2]) == 0):
                raise ValueError("Stack Underflow")
            # getting the necessary value
            self.list.pop(self.pos2-1)
            # updating the position markers
            self.pos2 -= 1
            self.pos3 -= 1
        else:
            # calculating the length and checking for underflow
            if (len(self.list[self.pos2:]) == 0):
                raise ValueError("Stack Underflow")
            # getting the necessary value
            self.list.pop()
            # updating the position markers
            self.pos3 -= 1

    # push function
    def push(self, item, stack_number):
        if (stack_number == 1):
            # adding the value to the list
            self.list.insert(self.pos1, item)
            # updating the position markers
            self.pos1 += 1
            self.pos2 += 1
            self.pos3 += 1
        elif (stack_number == 2):
            # adding the value to the list
            self.list.insert(self.pos2, item)
            # updating the position markers
            self.pos2 += 1
            self.pos3 += 1
        else:
            # adding the value to the list
            self.list.insert(self.pos3, item)
            # updating the position markers
            self.pos3 += 1
    
    # string function
    def __str__(self):
        return f"Stack1: {self.list[:self.pos1]}\nStack2: {self.list[self.pos1:self.pos2]}\nStack3: {self.list[self.pos2:]}"

# DRIVER CODE
stack = Stack()
stack.push(5, 3)
stack.push(10, 2)
stack.push(1, 1)

print(stack, "\n")

stack.push(3, 3)
stack.push(1, 2)
stack.push(0, 2)

print(stack, "\n")

stack.pop(2)
stack.pop(1)
stack.pop(3)

print(stack, "\n")