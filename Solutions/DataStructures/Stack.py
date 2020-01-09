class Stack():
    '''
    Stack Class for the implementation of a stack
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self):
        self.stack = []
        self.head = -1
        self.rear = -1
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        temp = ""

        for i in self.stack:
            temp += f"{i} "
        
        if (temp == ""):
            temp = "*EMPTY*"
        
        return f"Stack: {temp}\nHead: {self.head}\t\tRear = {self.rear}"
    
    def push(self, val):
        # Pushes a new value to the stack rear
        if (self.head == -1):
            self.stack.append(val)
            self.head = 0
            self.rear = 0
        
        else:
            self.stack.append(val)
            self.rear += 1
    
    def pop(self):
        # Pops the value at the stack rear (returns None if empty)
        if (self.head == -1):
            return None

        elif (self.rear == 0):
            self.head = -1
            self.rear = -1
        
        else:
            self.rear -= 1   
        
        return self.stack.pop()