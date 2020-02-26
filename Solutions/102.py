'''
Problem:

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

Example:

Input = [1, 2, 3, 4, 5], 9
Output = [2, 3, 4]
'''

# FUNCTION TO PERFORM THE OPERATION
def get_part(arr, k):
    # total_sum stores the sum till the current iteration
    total_sum = 0
    # getting the length of the list
    length = len(arr)

    # setting up necessary variables
    start, end = 0, 0
    iteration = 0

    # using a moving window to converge to the final answer
    while (iteration < length):
        # if the window has been found, we return the part of the list
        if (total_sum == k):
            return arr[start : end]

        # if the total_sum exceeds the target sum, we remove the starting element from the window
        elif (total_sum > k):
            total_sum -= arr[start]
            start += 1
        
        # if the total_sum is smaller than the target sum, we add the next element to the window
        else:
            total_sum += arr[iteration]
            end = iteration + 1
            iteration += 1
    
    # returning None if the target sum cannot be achieved
    return None

# DRIVER CODE
print(get_part([1, 2, 3, 4, 5], 0))
print(get_part([1, 2, 3, 4, 5], 1))
print(get_part([1, 2, 3, 4, 5], 5))
print(get_part([5, 4, 3, 4, 5], 12))
print(get_part([5, 4, 3, 4, 5], 11))
print(get_part([1, 2, 3, 4, 5], 9))
print(get_part([1, 2, 3, 4, 5], 3))
print(get_part([1, 2, 3, 4, 5], 300))