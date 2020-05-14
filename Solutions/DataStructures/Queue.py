class Queue(super):
    '''
    Queue Class for FIFO Structure

    Functions:
    enqueue: function to add an object to the end of the queue
    denqueue: function to remove and return the object at the start of the queue (raises error if the queue is empty)
    isEmpty: function to check if the queue is empty
    '''

    # Initialize function (Automatically called upon creating an object instance)
    def __init__(self):
        self.queue = []
        self.elements = 0
    
    # String function (Automatically called upon converting to string, generally used when printing)
    def __str__(self):
        return str(self.queue)
    
    # Length function (Automatically called upon calling len())
    def __len__(self):
        return self.elements
    
    def enqueue(self, val):
        # function to add an object to the end of the queue
        self.elements += 1
        self.queue.append(val)
    
    def dequeue(self):
        # function to remove and return the object at the start of the queue (raises error if the queue is empty)
        if (self.elements == 0):
            raise Exception("Queue Underflow. Cannot Dequeue from an empty queue")
        
        self.elements -= 1
        return self.queue.pop(0)

    def isEmpty(self):
        # function to check if the queue is empty
        if (self.queue == []):
            return True
        else:
            return False