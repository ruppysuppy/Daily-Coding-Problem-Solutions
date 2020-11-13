"""
Problem:

Run-length encoding is a fast and simple method of encoding strings. The basic idea is
to represent repeated successive characters as a single count and character. For
example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded
have no digits and consists solely of alphabetic characters. You can assume the string
to be decoded is valid.
"""


def encode_run_length_encoding(string: str) -> str:
    # Time Complexity: O(n), Space Complexity: O(1)
    if not string:
        return ""
    encoded_string = ""
    prev_char = string[0]
    count = 0
    # generating the encoded string
    for char in string:
        if char != prev_char:
            encoded_string += str(count) + prev_char
            prev_char = char
            count = 1
        else:
            count += 1
    encoded_string += str(count) + prev_char
    return encoded_string


def decode_run_length_encoding(string: str) -> str:
    # Time Complexity: O(n), Space Complexity: O(1)
    decoded_string = ""
    char_frequency = 0
    # generating the decoded string
    for char in string:
        if char.isdigit():
            char_frequency = char_frequency * 10 + int(char)
        else:
            decoded_string += char * char_frequency
            char_frequency = 0
    return decoded_string


if __name__ == "__main__":
    print(encode_run_length_encoding("AAAABBBCCDAA"))
    print(decode_run_length_encoding("4A3B2C1D2A"))
