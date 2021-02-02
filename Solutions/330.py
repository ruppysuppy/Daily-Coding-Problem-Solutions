"""
Problem:

A Boolean formula can be said to be satisfiable if there is a way to assign truth
values to each variable such that the entire formula evaluates to true.

For example, suppose we have the following formula, where the symbol ¬ is used to
denote negation:

(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)
One way to satisfy this formula would be to let a = False, b = True, and c = True.

This type of formula, with AND statements joining tuples containing exactly one OR, is
known as 2-CNF.

Given a 2-CNF formula, find a way to assign truth values to satisfy it, or return False
if this is impossible.
"""

from typing import Dict, List, Union


def generate_combinations(num: int) -> List[List[bool]]:
    # generate all boolean combinations for the given number of variables
    numbers = [num for num in range(pow(2, num))]
    combinations = []
    for number in numbers:
        bin_number = bin(number)[2:].zfill(num)
        combinations.append(list(bool(int(i)) for i in bin_number))
    return combinations


def validation_problem(expression: str) -> Union[Dict[str, bool], bool]:
    # getting the variables
    formatted_expression = ""
    variables = {}
    for index, char in enumerate(expression):
        formatted_expression += char.lower()
        if char.isalpha() and char not in "OR AND":
            if char not in variables:
                variables[char] = set()
            variables[char].add(index)
    # generating all combinations for the given variables
    variables_set = set(variables.keys())
    variables_list = list(variables_set)
    variables_count = len(variables_list)
    combinations = generate_combinations(variables_count)
    # checking expression satisfiablity using all combinations
    for combination in combinations:
        calulation_expression = ""
        for index, char in enumerate(formatted_expression):
            if char == "¬":
                calulation_expression += "not "
            elif char in variables_set and index in variables[char]:
                position = variables_list.index(char)
                calulation_expression += str(combination[position])
            else:
                calulation_expression += char
        if eval(calulation_expression):
            return {key: value for key, value in zip(variables_list, combination)}
    # returning False if the expression cannot be satisfied
    return False


if __name__ == "__main__":
    print(validation_problem("(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)"))
    print(validation_problem("a AND a"))
    print(validation_problem("a AND ¬a"))


"""
SPECS:

TIME COMPLEXITY: O(length x (2 ^ variables))
SPACE COMPLEXITY: O(2 ^ variables)
"""
