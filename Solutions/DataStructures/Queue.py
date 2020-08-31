class Queue:
    """
    Queue Class for FIFO Structure

    Functions:
    dequeue: Remove and return the object at the head of the queue
             Raises error if the queue is empty
    enqueue: Add an object to the end of the queue
    is_empty: Check if the queue is empty
    peek: Get the value at the queue head without removing it
    """

    def __init__(self) -> None:
        self.queue = []
        self.elements = 0

    def __repr__(self) -> str:
        return str(self.queue)

    def __len__(self) -> int:
        return self.elements

    def enqueue(self, val: int) -> None:
        # Add an object to the end of the queue
        self.elements += 1
        self.queue.append(val)

    def dequeue(self) -> int:
        # Remove and return the object at the head of the queue
        # Raises error if the queue is empty
        if self.elements == 0:
            raise Exception("Queue Underflow. Cannot de-queue from an empty queue")
        self.elements -= 1
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        # Check if the queue is empty
        return not bool(self.queue)

    def peek(self) -> int:
        # Get the value at the queue head without removing it
        if self.is_empty():
            raise Exception("Queue Underflow. Cannot peek at an empty queue")
        return self.queue[0]
