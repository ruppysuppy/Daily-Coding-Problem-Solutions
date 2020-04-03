'''
Problem:

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). 
peek shows the next element that would be returned on next().
Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
'''

# PeekableInterface
class PeekableInterface(object):
    def __init__(self, iterator):
        # setting the iterator
        self.iterator = iterator
        # setting next_value and has_next as per data
        try:
            self.next_val = next(self.iterator)
            self.has_next = True
        except StopIteration:
            self.next_val = None
            self.has_next = False

    def peek(self):
        # returning the next value upon peeking
        return self.next_val

    def next(self):
        # checking if the iterator has values
        if (self.has_next):
            # storing the next value in a temporary variable
            temp = self.next_val
            try:
                # getting the next value
                self.next_val = next(self.iterator)
            except StopIteration:
                # if StopIteration error occours, the iterator has been exhausted
                # next_value and has_next are updated
                self.next_val = None
                self.has_next = False
            # returning temp
            return temp
        # returning None if the iterator has been exhausted
        else:
            return None

    def hasNext(self):
        # returning has_next
        return self.has_next

# DRIVER CODE
sample_list = [1, 2, 3, 4, 5]
iterator = iter(sample_list)
peekable = PeekableInterface(iterator)

print(peekable.peek())
print(peekable.hasNext())

print(peekable.next())
print(peekable.next())
print(peekable.next())

print(peekable.peek())
print(peekable.hasNext())

print(peekable.next())
print(peekable.hasNext())
print(peekable.peek())
print(peekable.next())

print(peekable.hasNext())
print(peekable.peek())

print()

sample_list = []
iterator = iter(sample_list)
peekable = PeekableInterface(iterator)

print(peekable.peek())
print(peekable.hasNext())