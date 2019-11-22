'''
Problem:

Given n integers and a target number, find whether 2 of the given numbers sum up to the target number.
'''

# FUNCTION TO PERFORM THE OPERATION
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

# FUNCTION TO PERFORM THE OPERATION (NO ADDITIONAL SPACE)
def target_sum_2ptr(arr, len_arr, target):
    arr.sort() # Sorting the list

    # Setting default values
    ptr1 = 0
    ptr2 = len_arr - 1

    # Main loop iterating and checking if the target sum is achieved
    while (ptr1 < ptr2):
        # If the target is achieved, True is returned
        if (arr[ptr1] + arr[ptr2] == target):
            return True
        
        # If the sum of the elements is less than the target, the pointer starting from the begining is incremented.
        # This is because the array is sorted and so arr[i] <= arr[i + 1]
        elif (arr[ptr1] + arr[ptr2] < target):
            ptr1 += 1

        # If the sum of the elements is greater than the target, the pointer starting from the end is decremented.
        # This is because the array is sorted and so arr[i] >= arr[i - 1]
        else:
            ptr2 -= 1
    
    # If the pointers meet, then there are no elements which add up to the target, so False is returned
    return False

# DRIVER CODE
Arr = [int(i) for i in input("Enter the array elements (separated by a space): ").split()]
target = int(input("Enter the target sum: "))

ans = target_sum(Arr, len(Arr), target)

if (ans[0]):
    print("The Target sum can be achieved by adding elements {} (pos: {}) and {} (pos: {})".format(Arr[ans[2]], ans[2], Arr[ans[1]], ans[1]))
else:
    print("The Target sum cannot be achieved by adding the given elements")

'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)

NOTE: If additional space is not allowed to be used, then the list can be sorted and 2 pointer method applied.
As a result, time complexity becomes O(nlog(n)) and space complexity becomes O(1)
'''