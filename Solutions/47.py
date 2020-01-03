'''
Problem:

You are given a array of numbers representing the stock prices of a company in chronological order. 
Write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

Example:

[9, 11, 8, 5, 7, 10] => 5 (since you could buy the stock at 5 dollars and sell it at 10 dollars)
'''

# FUNCTION TO PERFORM THE OPERATION
def max_diff(Arr):
    # length: stores the length of the arr
    length = len(Arr)

    # If there are less than 2 elements, buying and selling is not possible
    if (length < 2):
        return None

    # min_element: stores the minimum element till the current position (initialized with Arr[0])
    # diff: stores the maximum profit (initialized with (Arr[1] - Arr[0]))
    min_element = Arr[0]
    diff = Arr[1] - Arr[0]

    # Iterating over the array
    for i in range(1, length):
        # If the current element is smaller than the min_element, its updated
        if (min_element > Arr[i]):
            min_element = Arr[i]
        # If the difference is larger than the current difference, its updated
        elif (diff < (Arr[i] - min_element)):
            diff = (Arr[i] - min_element)
    
    # Incase there is negative difference, 0 is returned, else the max difference is returned
    return max(0, diff)

# DRIVER CODE
print(max_diff([9, 11, 8, 5, 7, 10]))
print(max_diff([1, 2, 3, 4, 5]))
print(max_diff([5, 4, 3, 2, 1]))
print(max_diff([1000]))