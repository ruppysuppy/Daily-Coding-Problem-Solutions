"""
Problem:

Given a string consisting of parentheses, single digits, and positive and negative
signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
"""


def evaluate(expression: str) -> int:
    result = 0
    add = True
    sub_eval_string = ""
    number_of_parentheses = 0
    for char in expression:
        if number_of_parentheses > 0:
            # inside a set of parentheses
            if char == "(":
                number_of_parentheses += 1
            elif char == ")":
                number_of_parentheses -= 1
            if number_of_parentheses == 0:
                # evaluating part within parentheses recursively
                if add:
                    result += evaluate(sub_eval_string)
                else:
                    result -= evaluate(sub_eval_string)
                sub_eval_string = ""
            else:
                sub_eval_string += char
        else:
            if char == "-":
                add = False
            elif char == "+":
                add = True
            elif char == "(":
                number_of_parentheses = 1
            elif char.isdigit():
                if add:
                    result += int(char)
                else:
                    result -= int(char)
    return result


if __name__ == "__main__":
    print(evaluate("-1 + (2 + 3)"))
    print(evaluate("-1 + (2 + 3) + (2 - 3)"))
    print(evaluate("-1 + (2 + 3) + ((2 - 3) + 1)"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
