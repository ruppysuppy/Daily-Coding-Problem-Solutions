'''
Problem:

Implement a bit array.
A bit array is a space efficient array that holds a value of 1 or 0 at each index.
* init(size): initialize the array with size
* set(i, val): updates index at i with val where val is either 1 or 0.
* get(i): gets the value at index i.
'''

# Bit Array class
class Bit_Array():
    # initialize function
    def __init__(self, length):
        # storing the length of the array and the indices where the element is 1
        self.length = length
        self.indices = set()
    
    # function to set the value of i'th position of the bit array
    def set(self, pos, val):
        # if the given position is out of the array, IndexError is raised
        if (pos >= self.length):
            raise IndexError("Index is out of range")

        # if the value is 1, its added to the index set 
        # (as duplicates are not allowed in hash list, even if the value is present, there is no problem)
        if (val):
            self.indices.add(pos)
        # if the value is 0, if the element at the position was 1, the position removed from the index set
        else:
            if (pos in self.indices):
                self.indices.remove(pos)
    
    def get(self, pos):
        # if the given position is out of the array, IndexError is raised
        if (pos >= self.length):
            raise IndexError("Index is out of range")

        # returning the value based on whether the position is present in the index list
        if (pos in self.indices):
            return 1
        else:
            return 0
    
    # function to display the array
    def __str__(self):
        res = []

        for pos in range(self.length):
            if (pos in self.indices):
                res.append(1)
            else:
                res.append(0)
        
        return str(res)

# DRIVER CODE
arr = Bit_Array(8)

print(arr)

arr.set(5, 1)
arr.set(1, 1)

print(arr)

print(arr.get(1))
print(arr.get(4))