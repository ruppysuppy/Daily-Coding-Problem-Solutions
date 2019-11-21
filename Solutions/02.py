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

# FUNCTION TO PERFORM THE OPERATION (WITHOUT DIVISION)
def prod_no_div(Arr, length):
    output = [None] * length # Create an empty output list
    product = 1 # Set initial product run forward
    
    # Calculating the cumulative product (before the i'th element)
    for i in range(length):
        output[i] = product
        product = product * Arr[i]

    product = 1
    
    # Calculating the cumulative product (after the i'th element)
    for i in range(length-1, -1, -1):
        output[i] *= product
        product *= Arr[i]
        
    return output 

# DRIVER CODE
Arr = [int(i) for i in input("Enter the array elements separated by a space: ").split()]
length = len(Arr)

ans1 = prod(Arr, length)
ans2 = prod_no_div(Arr, length)

print(("The resultant elements are (Using Division): " + "{} " * length).format(*ans1))
print(("The resultant elements are (Without Division): " + "{} " * length).format(*ans2))

'''
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n) in this solution, if overwriting the original array is allowed, it becomes O(1)

NOTE:
If division is not allowed, it becomes a bit complex and using O(n) Space becomes mandatory

OR

You could make your own simple division function using the code below :)

# WORKS ONLY FOR PERFECTLY DIVISIBLE NUMBERS
def div(num, divisor):
    quotient = 0

    while (num > 0):
        num -= divisor
        quotient += 1
    
    return quotient
'''