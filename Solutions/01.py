'''
Problem:

Given an array of n integers and a target number, find whether the array contains 2 numbers which sum up to the target number.
'''

# FUNCTION TO CHECK WHETHER THE TARGET SUM CAN BE REACHED
def target_sum(arr, len_arr, target):
    cache = {} # Initialized a cache to store the location and the element (for memorization)
    # NOTE: It is not mandatory to use a dictionary, a set(hash list) can also be used if the aim is just to check if the target sum can be reached, without specifying the position of the elements to add

    for i in range(len_arr): # a loop to go over each element in the array
        if ((target - arr[i]) in cache): # if an element which upon adding to the current element gives the target element is found, the answer is returned
            return [True, i, cache[target - arr[i]]]
        else: # else we add the element (as the key) and the position to the dictionary (if a set is used, storing the position would be much more difficult)
            cache[arr[i]] = i

    # If no element sums up to the target element, False is returned
    return [False]

# DRIVER CODE
Arr = [int(i) for i in input("Enter the array elements (separated by a space): ").split()]
target = int(input("Enter the target sum: "))

ans = target_sum(Arr, len(Arr), target)

if (ans[0]):
    print("The Target sum can be achieved by adding elements {} (pos: {}) and {} (pos: {})".format(Arr[ans[2]], ans[2], Arr[ans[1]], ans[1]))
else:
    print("The Target sum cannot be achieved")