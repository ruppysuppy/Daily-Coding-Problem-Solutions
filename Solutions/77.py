'''
Problem:

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.

Example:

Input = [(1, 3), (5, 8), (4, 10), (20, 25)]
Output = [(1, 3), (4, 10), (20, 25)]
'''

# FUNCTION TO PERFORM THE OPERATION
def merge(intervals):
    # sorting the values by the start time
    intervals.sort(key=lambda x: x[0])
    # res stores the final result
    # start stores the current start time
    # end stores the current end time
    res = []
    start = intervals[0][0]
    end = intervals[0][1]

    # looping over the intervals from the 2nd one (as the 1st is used to set start and end)
    for interval in intervals[1:]:
        # if the current end time is less than the next start time (no overlap)
        # the start (current) and end is added to the result and start/end reset
        if (end < interval[0]):
            res.append((start, end))
            start = interval[0]
            end = interval[1]
        # if the end lies between the next start and end, end is updated to next end
        elif (end < interval[1] and end > interval[0]):
            end = interval[1]
    
    # adding the last start and end pair
    res.append((start, end))

    return res

# DRIVER CODE
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
print(merge([(1, 3), (5, 10), (4, 8), (20, 25)]))