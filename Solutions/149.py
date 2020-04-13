'''
Problem:

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).
You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.


EXAMPLE:

Input = [1, 2, 3, 4, 5], 1, 3 
Output = 5 (sum([2, 3]))
'''

# class to optimize the array and perform the sum over range
class SubarraySumOptimizer:
    # default initialization function
    def __init__(self, arr):
        # creating a preprocessed array
        self.preprocessed_arr = [0 for _ in range(len(arr)+1)]
        # sum current stores the sum till the current element
        sum_curr = 0

        # preprocessing the array
        for i in range(len(arr)):
            sum_curr += arr[i]
            self.preprocessed_arr[i+1] = sum_curr

    # FUNCTION TO PERFORM THE OPERATION
    def sum(self, start, end):
        # checking if the query is valid, returns 0 for invalid query
        if ((start < 0) or (end > len(self.preprocessed_arr)-1) or (start > end)):
            return 0
        
        # returning the difference (as the array has been preprocessed)
        return (self.preprocessed_arr[end] - self.preprocessed_arr[start])

# DRIVER CODE
sso = SubarraySumOptimizer([1, 2, 3, 4, 5])

print(sso.sum(1, 3))
print(sso.sum(0, 5))
print(sso.sum(0, 4))
print(sso.sum(3, 4))
print(sso.sum(3, 3))