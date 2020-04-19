'''
Problem:

Given a list of elements, find the majority element, which appears more than half the times (> floor(len(lst) / 2.0)).
You can assume that such an element exists.

Example:

Input = [1, 2, 1, 1, 3, 4, 0]
Output = 1
'''

# FUNCTION TO PERFORM THE OPERATION
def majority_element(arr):
    # getting the length
    length = len(arr)
    
    # returning the values based on length
    if (not length):
        return
    elif (length < 3):
        return arr[0]
    
    # freq hash map to store the frequency of each element
    freq = {}

    # iterating through the array and generating freq
    for elem in arr:
        if (elem in freq):
            freq[elem] += 1
        else:
            freq[elem] = 1
    
    # iterating through freq and finding the majority element
    for elem in freq:
        if (freq[elem] > (length // 2)):
            return elem

# DRIVER CODE
print(majority_element([1, 2, 1, 1, 1, 4, 0]))
print(majority_element([1, 1, 1, 3, 3, 3, 4, 1, 1]))