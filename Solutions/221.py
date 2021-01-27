"""
Problem:

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of
unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create
an algorithm to find the nth sevenish number.
"""


def get_nth_sevenish_num(number: int) -> int:
    curr = 1
    curr_iteration = 1
    while curr < number:
        curr_iteration += 1
        curr += curr_iteration

    curr -= curr_iteration
    result = 7 ** (curr_iteration - 1)
    curr_to_add = 1

    for _ in range(number - curr - 1):
        result += curr_to_add
        curr_to_add *= 7
    return result


if __name__ == "__main__":
    print(get_nth_sevenish_num(1))  # 1 = 7 ^ 0
    print(get_nth_sevenish_num(2))  # 7 = 7 ^ 1
    print(get_nth_sevenish_num(3))  # 8 = 7 ^ 0 + 7 ^ 1
    print(get_nth_sevenish_num(4))  # 49 = 7 ^ 2
    print(get_nth_sevenish_num(5))  # 50 = 7 ^ 0 + 7 ^ 2
    print(get_nth_sevenish_num(6))  # 57 = 7 ^ 0 + 7 ^ 1 + 7 ^ 2


"""
SPECS:

TIME COMPLEXITY: O(log(n))
SPACE COMPLEXITY: O(1)
"""
