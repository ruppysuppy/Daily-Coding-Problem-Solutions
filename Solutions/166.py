"""
Problem:

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
* next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
* has_next(): returns whether or not the iterator still has elements left.
Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

Example:

Input = [[1, 2], [3], [], [4, 5, 6]]
Output = 1, 2, 3, 4, 5, 6 (calling next() repeatedly should output this sequence)
"""

# iterator class
class iterator:
    # initialization function
    def __init__(self, mat):
        # storing the matrix and the generator
        self.mat = mat
        self.generator = self.generator_func(mat)
        self.next_value = next(self.generator)

    # generator function to generate the values from the matrix
    def generator_func(self, matrix):
        for array in matrix:
            for element in array:
                yield element

    # string function to display the matrix
    def __str__(self):
        return str(self.mat)

    # has next function implementation
    def has_next(self):
        # checking if the elements are left in the iterator
        return self.next_value != None

    # next function implementation
    def next(self):
        # storing the next value for returning
        temp = self.next_value

        # updating the next value
        try:
            self.next_value = next(self.generator)
        except StopIteration:
            self.next_value = None

        # returning the stored value
        return temp


# DRIVER CODE
iter_obj = iterator([[1, 2], [3], [], [4, 5, 6]])
print(iter_obj)

print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
print(iter_obj.has_next())
print(iter_obj.next())
