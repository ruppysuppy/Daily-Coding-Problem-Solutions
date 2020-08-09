class Queue:
    """
    Queue Class for FIFO Structure

    Functions:
    dequeue: Remove and return the object at the start of the queue
             Raises error if the queue is empty
    enqueue: Add an object to the end of the queue
    isEmpty: check if the queue is empty
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
        # Remove and return the object at the start of the queue
        # Raises error if the queue is empty
        if self.elements == 0:
            raise Exception("Queue Underflow. Cannot de-queue from an empty queue")
        self.elements -= 1
        return self.queue.pop(0)

    def isEmpty(self) -> bool:
        # Check if the queue is empty
        return bool(self.queue)
