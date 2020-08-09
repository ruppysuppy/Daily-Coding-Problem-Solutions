"""
Problem:

You run an e-commerce website and want to record the last N order ids in a log. 

Implement a data structure to accomplish this, with the following API: 
* record(order_id): adds the order_id to the log 
* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space
"""

# Object to store the necessary details
class Order_Log:
    # Initialization
    def __init__(self, length):
        # Circular buffer to hold the order ids
        self.log_circular_buffer = [None for _ in range(length)]
        self.length = length
        self.pos = 0

    # FUNCTION TO PERFORM THE OPERATION (record)
    def record(self, order_id):
        # Storing the order id and moving to the next index
        self.log_circular_buffer[self.pos] = order_id
        self.pos += 1

        # Returning to the start in case all logs are filled
        if self.pos == self.length:
            self.pos = 0

    # FUNCTION TO PERFORM THE OPERATION (get_last)
    def get_last(self, i):
        # Getting the position of the desired order id
        # Negative numbers won't be a problem as python supports negative indexing (in other languages, use i += length (if i < 0))
        i = self.pos - i

        return self.log_circular_buffer[i]


# DRIVER CODE
log = Order_Log(10)

for id in range(20):
    log.record(id)

print(log.get_last(1))

print(log.get_last(5))

log.record(20)
log.record(21)

print(log.get_last(1))
print(log.get_last(3))
