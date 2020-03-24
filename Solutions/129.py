'''
Problem:

Given a real number n, find the square root of n. 

Example:

Input = 9
Output = 3
'''

# global value for tolerence
TOLERENCE = 10 ** (-6)

# helper function to check whether 2 numbers are almost equal (within the tolerence limit)
def almost_equal(num1, num2):
    return (num1 + TOLERENCE > num2 and num1 - TOLERENCE < num2)

# FUNCTION TO PERFORM THE OPERATION
def get_sqrt(num):
    # using binary search to get the squary root in O(log(n))
    # high stores the upper-bound
    # low stores the lower-bound
    high = num
    low = 0

    # finding the square root (mid)
    while True:
        # getting the current mid
        mid = (high + low) / 2
        # temp stores the square of mid
        temp = mid * mid

        # if temp is equal to the passed number, mid is the square root 
        # its rounded to 6 decimal places and returned
        if (almost_equal(temp, num)):
            return round(mid, 6)
        
        # depending upon the value of temp, the next search domain is restricted (check binary search for details)
        elif (temp < num):
            low = mid + 1
        
        else:
            high = mid - 1

# DRIVER CODE
print(get_sqrt(100))
print(get_sqrt(9))
print(get_sqrt(3))
print(get_sqrt(2))