'''
Problem:

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?

Example:

Input = [2, 4, 6, 2, 5]
Output = 13
'''

# FUNCTION TO PERFORM THE OPERATION
def max_nonadjacent_sum(arr):
    # Declaring variables
    inc = 0 # Holds the maximum value (INCLUDING the i'th element of the array)
    exc = 0 # Holds the maximum value (EXCLUDING the i'th element of the array)

    # iterating over the array
    for i in arr:
        # Storing the value of inc in temp
        temp = inc

        # Finding the max INCLUDING the i'th value
        inc = max(exc+i, i)

        # Finding the max EXCLUDING the i'th value
        exc = max(temp, inc-i)
        
    return max(inc, exc)

# DRIVER CODE
print(max_nonadjacent_sum([2, 4, -6, 2, 5]))
print(max_nonadjacent_sum([-5, 1, 1, -5]))
print(max_nonadjacent_sum([5, 5, 10, 100, 10, 5]))