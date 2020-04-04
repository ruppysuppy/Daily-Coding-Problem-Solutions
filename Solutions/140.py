'''
Problem:

You are given an array of integers in which two elements appear exactly once and all other elements appear exactly twice. 
Find the two elements that appear only once.
Follow-up: Can you do this in linear time and constant space?

Example:

Input = [2, 4, 6, 8, 10, 2, 6, 10]
Output = 4, 8 (The order does not matter)
'''

# FUNCTION TO PERFORM THE OPERATION
def get_uniques(arr):
    # checking if the array has at least 2 elements
    if (len(arr) >= 2):
        # getting the xor of all the values
        xor_res = 0

        for val in arr:
            xor_res = xor_res ^ val
        
        # getting the rightmost rest bit (as at least 1 bit needs to differ for 2 numbers to be different)
        rightmost_set_bit = xor_res & ~(xor_res - 1)
        num1 = 0
        num2 = 0

        # using the rightmost set bit as mask to segregate the array of numbers into 2 sets 
        # performing xor for num1 and num2 based on the set to which they belong to
        # the 2 sets are based on whether a number has rightmost_set_bit 1 or 0
        for val in arr:
            if (val & rightmost_set_bit):
                num1 = num1 ^ val
            else:
                num2 = num2 ^ val
        
        return num1, num2
    
    # if the array is empty or contains 1 element, 2 'None's are returned
    else:
        return None, None

# DRIVER CODE
print(get_uniques([2, 4, 6, 8, 10, 2, 6, 10]))
print(get_uniques([2, 4, 8, 8, 10, 2, 6, 10]))