'''
Problem:

Write a program that checks whether an integer is a palindrome. Do not convert the integer into a string.

Example:

Input = 121
Output = True

Input = 888
Output = True

Input = 678
Output = False
'''

# FUNCTION TO PERFORM THE OPERATION
def pal_check(num):
    # dec_places stores the number of decimal places in the number
    dec_place = 0
    
    # getting the number of decimal places
    temp = num

    while (temp >= 10):
        dec_place += 1
        temp = temp // 10

    # if the number of digits is odd, the middle number is excluded from comparison
    if (dec_place % 2 == 0):
        # checking if the number is a palindrome
        for i in range((dec_place)//2):
            digit1 = (num // (10 ** i)) % (10 ** (i + 1))
            digit2 = (num % (10 ** (dec_place - i + 1))) // (10 ** (dec_place - i))
            
            if (digit1 != digit2):
                return False
    # if the number of digits is even, the middle number is included in comparison
    else:
        # checking if the number is a palindrome
        for i in range((dec_place)//2 + 1):
            digit1 = (num // (10 ** i)) % 10
            digit2 = (num % (10 ** (dec_place - i + 1))) // (10 ** (dec_place - i))
            
            if (digit1 != digit2):
                return False
    
    # returning True if all the checks for palindrome passes
    return True

# DRIVER CODE
print(pal_check(235))
print(pal_check(121))
print(pal_check(888))
print(pal_check(1661))
print(pal_check(678))