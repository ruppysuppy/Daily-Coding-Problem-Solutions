'''
Problem:

Given a list of integers, return the largest product that can be made by multiplying any three integers.
You can assume the list has at least three integers.

Example:

Input = [-10, -10, 5, 2]
Output = 500 (-10 * -10 * 5)
'''

# FUNCTION TO PERFORM THE OPERATION
def largest_prod_3(Arr, length):
    # neg1 & neg2 stores the smallest & second smallest negative numbers
    neg1 = 0
    neg2 = 0
    # pos1, pos2 & pos3 stores the 3 largest positive numbers
    pos1 = 0
    pos2 = 0
    pos3 = 0

    # looping over the array
    for i in range(length):
        # if the current element is smaller than neg1, neg1 & neg2 are updated
        if (Arr[i] < neg1):
            neg2 = neg1
            neg1 = Arr[i]
        
        # if the current element is smaller than neg2 and larger than neg1, neg2 are updated
        elif (Arr[i] < neg2):
            neg2 = Arr[i]
        
        # if the current element is larger than pos1, pos1, pos2 & pos3 are updated
        elif (Arr[i] > pos1):
            pos3 = pos2
            pos2 = pos1
            pos1 = Arr[i]
        
        # if the current element is larger than pos2 and smaller than pos1, pos2 & pos3 are updated
        elif (Arr[i] > pos2):
            pos3 = pos2
            pos2 = Arr[i]
        
        # if the current element is larger than pos3 and smaller than pos2, pos3 is updated
        elif (Arr[i] > pos2):
            pos3 = Arr[i]
    
    # the product of neg1 & neg2 is larger than that of pos2 & pos3, then they are multiplied in the final product
    # else pos2 & pos3 are multiplied in the final product
    if ((neg1 * neg2) > (pos2 * pos3)):
        return (neg2 * neg1 * pos1)
    else:
        return (pos1 * pos2 * pos3)

# DRIVER CODE
inp = [-10, -10, 5, 2]
print(largest_prod_3(inp, len(inp)))