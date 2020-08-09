"""
Problem:

Given a number in Roman numeral format, convert it to decimal.
The values of Roman numerals are as follows:
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

Example:

Input = XIV
Output = 14
"""

# global map for the Roman numbers
VALUE_MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

# FUNCTION TO PERFORM THE OPERATION
def convert_roman_to_decimal(num_str: str) -> int:
    # declaring the map
    global VALUE_MAP

    length = len(num_str)
    num = 0

    # iterating through the Roman number
    for i in range(length - 1):
        # checking whether the value has to be added or subtracted and performing the operation
        if VALUE_MAP[num_str[i]] < VALUE_MAP[num_str[i + 1]]:
            num -= VALUE_MAP[num_str[i]]
        else:
            num += VALUE_MAP[num_str[i]]

    # since the loop goes till length-1, adding the last value
    num += VALUE_MAP[num_str[length - 1]]

    return num


# DRIVER CODE
print(convert_roman_to_decimal("I"))
print(convert_roman_to_decimal("IV"))
print(convert_roman_to_decimal("XIV"))
print(convert_roman_to_decimal("XL"))
