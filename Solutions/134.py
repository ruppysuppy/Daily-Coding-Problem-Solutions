'''
Problem:

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:
* init(arr, size): initialize with the original large array and size.
* set(i, val): updates index at i with val.
* get(i): gets the value at index i.
'''

# the Sparse Array class
class SparseArray:
    # initialization function
    def __init__(self, arr, size):
        # using a dictionary to map the index to the value
        self.arr = {}
        # size stores the size of the array
        self.size = size

        # generating the array
        for index, val in enumerate(arr):
            # storing only the non-zero values
            if (val != 0):
                self.arr[index] = val
    
    # set function
    def set(self, pos, val):
        # if the index is out of range, IndexError is raised
        if (pos > self.size):
            raise IndexError

        # if the value is 0, its not set (if any value is present, its deleted)
        if (val == 0):
            if (pos in self.arr):
                del self.arr[pos]
        # the value is set if its non-zero
        else:
            self.arr[pos] = val
    
    # get function
    def get(self, pos):
        # if the position is in the array range
        if (pos < self.size):
            # if the value is non-zero, its extracted from the dictionary and returned
            if (pos in self.arr):
                return self.arr[pos]
            # else 0 is returned
            else:
                return 0
        # if the position is out of range, IndexError is raised
        else:
            raise IndexError
    
    # string function to display the array
    def __str__(self):
        string = ""

        for pos in range(self.size):
            if (pos in self.arr):
                string += f"{self.arr[pos]}, "
            else:
                string += "0, "

        return ("[" + string.rstrip(" ,") + "]")

# DRIVER CODE
arr = SparseArray([1, 0, 0, 0, 3, 0, 2, 0], 8)

print(arr)

arr.set(2, 4)
print(arr.get(2))
arr.set(4, 1)
print(arr.get(4))
arr.set(0, 0)
print(arr.get(0))

print(arr)