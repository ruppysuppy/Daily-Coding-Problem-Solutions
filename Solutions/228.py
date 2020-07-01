'''
Problem:

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 

Example:

Input = [10, 7, 76, 415]
Output = 77641510
'''


class ModifiedInt:
    # helper class for the sort operation (requires __lt__ dunder method)

    def __init__(self, val):
        if type(val) != int: raise TypeError
        self.val = str(val)

    def __lt__(self, other):
        # returns the number with shorter length or has a smaller more significant digit
        if (type(other) == ModifiedInt):
            if (self.val == other.val): return False

            for c1, c2 in zip(self.val, other.val):
                if (c1 > c2): return False
                elif (c1 < c2): return True

            if (len(self.val) > len(other.val)): return True
        return False


def get_largest(arr):
    arr = list(map(ModifiedInt, arr))
    arr.sort(reverse=True)
    return int("".join(map(lambda x: x.val, arr)))


# DRIVER CODE
print(get_largest([10, 7, 76, 415]))