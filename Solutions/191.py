'''
Problem:

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.
The intervals are not necessarily sorted in any order.

Example:

Input = (7, 9), (2, 4), (5, 8)
Output = 1 (as the last interval can be removed and the first two won't overlap)
'''

# FUNCTION TO PERFORM THE OPERATION
def num_overlap(arr):
    # cache to store whether a time frame falls in the input time interval
    cache = [0 for _ in range(max(max(arr))+1)]
    # variable to store the overlap count
    overlap_count = 0

    # iterating through the intervals
    for interval in arr:
        # breaking the interval into start and end
        start, end = interval
        # flag checks for overlap
        flag = True

        # iterating through the interval range 
        # (to end-1 as 2 intervals may have the same end and start time without overlaping)
        for i in range(start, end):
            # checking if the value in the cache is 0 (no overlap)
            if (cache[i] == 0):
                cache[i] = 1
            else:
                # if an overlap occurs, overlap count is incremented
                # flag is unset so that the overlap is counted once
                if (flag):
                    overlap_count += 1
                    flag = False
    
    # returning overlap count
    return overlap_count

# DRIVER CODE
print(num_overlap([[0, 1], [1, 2]]))
print(num_overlap([(7, 9), (2, 4), (5, 8)]))
print(num_overlap([(7, 9), (2, 4), (5, 8), (1, 3)]))