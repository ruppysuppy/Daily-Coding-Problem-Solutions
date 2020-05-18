'''
Problem:

Given n numbers, find the greatest common denominator between them.

Example:

Input = [42, 56, 14]
Output = 14
'''

# importingg gcd function from math module
from math import gcd as gcd_of_2

# FUNCTION TO PERFORM THE OPERATION
def gcd(nums):
    # if the array is empty, None is returned
    if (not nums):
        return None
    
    # initializing the result
    result = nums[0]

    # finding the gcd of all the numbers
    for num in nums[1:]:
        result = gcd_of_2(result, num)
    
    # returning the result
    return result

# DRIVER CODE
print(gcd([42, 56, 14]))
print(gcd([3, 5]))
print(gcd([9, 15]))