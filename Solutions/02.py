'''
Problem:

Given n integers, find the product of the numbers except the number at i'th position
Eg: [1, 2, 3, 4] => [24, 12, 8, 6]
Explaination: At pos 0, result = 2x3x4; at pos 1 result = 1x3x4; at pos 2 result = 1x2x4; at pos 3 result = 1x2x3 [USING 0 BASED INDEX]
'''

# FUNCTION TO PERFORM THE OPERATION
def prod(Arr, length):
    prod_target = 1 # Variable storing the product of all the elements
    prod_Arr = [0] * length # New List to store the results

    # Calculating the product of all elements
    for i in Arr:
        prod_target = prod_target * i
    
    # Calculating the result at pos i (product of all elements / element at pos i)
    for i in range(length):
        prod_Arr[i] = prod_target // Arr[i]
    
    return prod_Arr

# DRIVER CODE
Arr = [int(i) for i in input("Enter the array elements separated by a space: ").split()]
length = len(Arr)
ans = prod(Arr, length)

print(("The resultant elements are: " + "{} " * length).format(*ans))

'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n) IN THIS SOLUTION, IF OVERWRITING THE ORIGINAL ARRAY IS ALLOWED, IT BECOMES O(1)
'''