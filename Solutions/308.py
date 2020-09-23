"""
Problem:
You are presented with an array representing a Boolean expression. The elements are of
two kinds:

T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements using parentheses so that the
entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are
two acceptable groupings: (F | T) & T and F | (T & T).
"""

from typing import List


def evaluator(arr: List[str]) -> List[bool]:
    expr = "".join(arr)
    if len(arr) == 1 or len(arr) == 3:
        return [eval(expr)]

    groupings = []
    # checking all possible arrangements
    for i in range(len(arr) // 2):
        pivot = i * 2 + 1
        left = arr[:pivot]
        right = arr[pivot + 1 :]
        for fe in evaluator(left):
            for se in evaluator(right):
                new_exp = str(fe) + arr[pivot] + str(se)
                # adding the expression only if evaluates to True
                if eval(new_exp):
                    groupings.append(True)
    return groupings


def get_groupings(arr: List[str]) -> int:
    # replacing the 'T's and 'F's
    for ind in range(len(arr)):
        if arr[ind] == "F":
            arr[ind] = "False"
        elif arr[ind] == "T":
            arr[ind] = "True"
    return len(evaluator(arr))


if __name__ == "__main__":
    print(get_groupings(["F", "|", "T", "&", "T"]))
    print(get_groupings(["F", "|", "T", "&", "T", "^", "F"]))
    print(get_groupings(["F", "|", "T", "&", "F", "^", "F"]))
    print(get_groupings(["F", "|", "T", "|", "F", "^", "F"]))
    print(get_groupings(["T", "^", "T", "&", "F"]))


"""
SPECS:

TIME COMPLEXITY: O(n ^ 3)
SPACE COMPLEXITY: O(n ^ 2)
"""
