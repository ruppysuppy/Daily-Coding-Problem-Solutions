'''
Problem:

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
Do this in O(N) time and O(1) space.

Example:
[6, 1, 3, 3, 3, 6, 6] => 1
'''

# We can sum the bits in same positions for all the numbers and take modulo with 3. 
# The bits for which sum is not multiple of 3, are the bits of number with single occurrence.
# Let us consider the example array {9, 8, 9, 9}. The 1001, 1000, 1001, 1001
# Sum of first bits (2 ^ 0) % 3 = (1 + 1 + 1 + 0) % 3 = 0
# Sum of second bits (2 ^ 1) % 3 = (0 + 0 + 0 + 0) % 3 = 0
# Sum of third bits (2 ^ 2) % 3 = (0 + 0 + 0 + 0) % 3 = 0
# Sum of fourth bits (2 ^ 3) % 3 = (1 + 1 + 1 + 1) % 3 = 1
# Hence number which appears once is 1000

# FUNCTION TO PERFORM THE OPERATION
def get_unique(arr):
    # Variable to store the element which occours once
    unique_elem = 0
      
    # Iterate through all the bits (considering a 64 bit machine)
    for i in range(64):
        # sum_i_pos_bits stores the sum of the masked position bits of all elements in the array
        # mask stores the current mask (example of a 4 bit mask for 2nd pos: 0100 and for 1st pos: 0010)
        sum_i_pos_bits = 0
        mask = (1 << i) 

        # Calculating the sum_i_pos_bits for the current mask
        for elem in arr: 
            if (elem & mask): 
                sum_i_pos_bits = sum_i_pos_bits + 1
                  
        # If the sum_i_pos_bits is 1 (implies the unique element contains 1 in that position), adding it to the unique_elem
        if (sum_i_pos_bits % 3) : 
            unique_elem = unique_elem | mask 
      
    return unique_elem 

# DRIVER CODE
arr = [3, 3, 2, 3] 
print(get_unique(arr))

arr = [13, 19, 13, 13]
print(get_unique(arr))

arr = [6, 1, 3, 3, 3, 6, 6]
print(get_unique(arr))

arr = [12, 1, 3, 1, 1, 2, 3, 2, 2, 3] 
print(get_unique(arr))