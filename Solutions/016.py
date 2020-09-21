"""
Problem:

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log get_last(i): gets the ith last element
from the log. i is guaranteed to be smaller than or equal to N. You should be as
efficient with time and space as possible.
"""


class Order_Log:
    def __init__(self, N: int) -> None:
        self.circular_buffer = [None for _ in range(N)]
        self.N = N
        self.pos = 0

    def record(self, order_id: int) -> None:
        # adding the order_id to the log
        self.circular_buffer[self.pos] = order_id
        self.pos += 1
        if self.pos == self.N:
            self.pos = 0

    def get_last(self, i: int) -> int:
        # getting the ith last element from the log
        position = self.pos - i
        return self.circular_buffer[position]


if __name__ == "__main__":
    log = Order_Log(10)

    for id in range(20):
        log.record(id)

    print(log.get_last(1))
    print(log.get_last(5))

    log.record(20)
    log.record(21)

    print(log.get_last(1))
    print(log.get_last(3))
