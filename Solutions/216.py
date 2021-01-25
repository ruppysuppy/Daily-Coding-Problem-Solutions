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
In addition, note that the Roman numeral system uses subtractive notation for numbers
such as IV and XL.

For the input XIV, for instance, you should return 14.
"""

VALUE_MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def convert_roman_to_decimal(num_str: str) -> int:
    length = len(num_str)
    num = 0

    for i in range(length - 1):
        # check if the value has to be added or subtracted
        if VALUE_MAP[num_str[i]] < VALUE_MAP[num_str[i + 1]]:
            num -= VALUE_MAP[num_str[i]]
        else:
            num += VALUE_MAP[num_str[i]]
    num += VALUE_MAP[num_str[length - 1]]
    return num


if __name__ == "__main__":
    print(convert_roman_to_decimal("I"))
    print(convert_roman_to_decimal("IV"))
    print(convert_roman_to_decimal("XIV"))
    print(convert_roman_to_decimal("XL"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
