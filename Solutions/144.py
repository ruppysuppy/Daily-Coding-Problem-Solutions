'''
Problem:

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.
If two distances to larger numbers are equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.
Follow-up: If you can preprocess the array, can you do this in constant time?

Example: 

Input = [4, 1, 3, 5, 6], 0
Output = 3
'''

# helper function to preprocess the data
def preprocess(arr):
    # dictionary for storing the preprocessed results
    preprocessed_indices = {}
    # getting the length of the array
    length = len(arr)

    # sorting the index value tuple by value
    sorted_tuples = [(value, index) for index, value in enumerate(arr)]
    sorted_tuples.sort(key=lambda tup: tup[0])
    
    # iterating through the sorted tuple
    for k, (_, i) in enumerate(sorted_tuples[:-1]):
        # min_dist stores the minimum distance from the 
        min_dist = length

        # iterating through the right side of the element (as the elements to the right are larger in a sorted array)
        for m in range(k + 1, length):
            # getting the absolute distance
            dist_temp = abs(i - sorted_tuples[m][1])
            # updating the distance as per requirement
            if (dist_temp < min_dist):
                min_dist = dist_temp
                preprocessed_indices[i] = sorted_tuples[m][1]

    # returning the preprocessed indices dictionary
    return preprocessed_indices

# FUNCTION TO PERFORM THE OPERATION
def nearest_larger(arr, index):
    # preprocessing the data
    preprocessed_indices = preprocess(arr)

    # checking if the index is in the preprocessed_indices
    if (index not in preprocessed_indices):
        return None

    # returning the proper index value
    return preprocessed_indices[index]

# DRIVER CODE
print(nearest_larger([4, 1, 3, 5, 6], 0))
print(nearest_larger([4, 1, 3, 5, 6], 1))
print(nearest_larger([4, 1, 3, 5, 6], 4))
print(nearest_larger([4, 1, 3, 5, 6], 3))