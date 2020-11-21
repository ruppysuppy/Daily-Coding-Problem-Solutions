from typing import Union


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

    def __delitem__(self, position: int) -> None:
        del self.queue[position]
        self.elements -= 1

    def __getitem__(self, position: int) -> Union[int, str]:
        return self.queue[position]

    def __setitem__(self, position: int, value: Union[int, str]) -> None:
        self.queue[position] = value

    def dequeue(self) -> Union[int, str]:
        # Remove and return the object at the head of the queue
        # Raises error if the queue is empty
        if self.elements == 0:
            raise Exception("Queue Underflow. Cannot de-queue from an empty queue")
        self.elements -= 1
        return self.queue.pop(0)

    def enqueue(self, val: Union[int, str]) -> None:
        # Add an object to the end of the queue
        self.elements += 1
        self.queue.append(val)

    def is_empty(self) -> bool:
        # Check if the queue is empty
        return not bool(self.queue)

    def peek(self) -> Union[int, str]:
        # Get the value at the queue head without removing it
        if self.is_empty():
            raise Exception("Queue Underflow. Cannot peek at an empty queue")
        return self.queue[0]
