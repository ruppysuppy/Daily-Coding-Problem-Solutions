"""
Problem:

Write a function, throw_dice(N, faces, total), that determines how many ways it is
possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""


def throw_dice(N: int, faces: int, total: int, accumulator: int = 0) -> int:
    if N == 0 and total == 0:
        return accumulator + 1
    elif total < 0:
        return accumulator
    # dfs to calculate the answer
    for i in range(1, faces + 1):
        accumulator = throw_dice(N - 1, faces, total - i, accumulator)
    return accumulator


if __name__ == "__main__":
    print(throw_dice(3, 6, 7))


"""
SPECS:

TIME COMPLEXITY: O(faces ^ log(total))
SPACE COMPLEXITY: O(total) [call stack included]
"""
