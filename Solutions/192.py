"""
Problem:

You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array and are trying to advance to the end. 
You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

Example:

Input = [1, 3, 1, 2, 0, 1]
Output = True (we can go from indices 0 -> 1 -> 3 -> 5)

Input = [1, 2, 1, 0, 0]
Output = False (we can't reach the end)
"""

# FUNCTION TO PERFORM THE OPERATION
def can_reach_end(arr):
    # getting the length of the array
    length = len(arr)

    # creating a array to use dynamic programming
    dp = [False for _ in range(length)]
    # base case (the end is reached)
    dp[length - 1] = True

    # iterating through the elements from the end
    for i in range(length - 2, -1, -1):
        # checking for an element in the reach of current position, from which the end can be reached
        for j in range(i + 1, min(length, i + arr[i] + 1)):
            # if such an element is found, the array is updated and the control breaks out of the loop
            if dp[j]:
                dp[i] = True
                break

    return dp[0]


# DRIVER CODE
print(can_reach_end([1, 3, 1, 2, 0, 1]))
print(can_reach_end([1, 2, 1, 0, 0]))
