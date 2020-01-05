'''
Problem:

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
Do this in O(N) time.

Example:
[34, -50, 42, 14, -5, 86] => 137
[-5, -1, -8, -9] => 0
'''

# FUNCTION TO PERFORM THE OPERATION
def max_cont_sum(Arr):
    # length: stores the length of the provided list
    # max_loc: stores the position of the max value in the modified list
    # min_loc: stores the position of the min value in the modified list
    length = len(Arr)
    max_loc = 0
    min_loc = 0

    # looping over and modifying the list (Arr[i] is the sum of all the elements till i. Eg: [1, 2, 3] => [1, 3, 6])
    for i in range(1, length):
        Arr[i] = Arr[i] + Arr[i-1]
    
    # looping over the list and updating min_loc and max_loc
    for i in range(length):
        # min_loc updation
        if (Arr[min_loc] > Arr[i]):
            min_loc = i
        
        # min_loc updation
        elif (Arr[max_loc] < Arr[i]):
            max_loc = i
    
    # if the value if at max_loc is negative, all the elements are negative, 0 is returned
    if (Arr[max_loc] > 0):
        # if min_loc is 0 and the element is positive, all the elements till max_loc is is the max sub arr, so Arr[max_loc] is returned
        if ((min_loc == 0) and (Arr[0] > 0)):
            return Arr[max_loc]
        # else Arr[max_loc] - Arr[min_loc] is returned
        return (Arr[max_loc] - Arr[min_loc])
    else:
        return 0

# DRIVER CODE
print(max_cont_sum([34, -50, 42, 14, -5, 86]))
print(max_cont_sum([-5, -1, -8, -9]))
print(max_cont_sum([5, 1, 8, 9]))