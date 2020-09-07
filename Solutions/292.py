"""
Problem:

A teacher must divide a class of students into two teams to play dodgeball.
Unfortunately, not all the kids get along, and several refuse to be put on the same
team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a
satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5}
and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
On the other hand, given the input below, you should return False.

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
"""

from typing import Dict, List, Set, Tuple, Union


def divide_into_groups(
    students: Dict[int, List[int]]
) -> Union[bool, Tuple[Set[int], Set[int]]]:
    set1 = set()
    set2 = set()
    nemesis1 = set()
    nemesis2 = set()

    for student in students:
        if student in nemesis1 and student in nemesis2:
            # satisfactory pair of teams doesn't exist
            return False
        # creating the necessary reference
        if student in nemesis1:
            set_curr = set2
            nemesis_curr = nemesis2
        else:
            set_curr = set1
            nemesis_curr = nemesis1
        set_curr.add(student)
        for nemesis in students[student]:
            nemesis_curr.add(nemesis)
    return set1, set2


if __name__ == "__main__":
    students = {0: [3], 1: [2], 2: [1, 4], 3: [0, 4, 5], 4: [2, 3], 5: [3]}
    print(divide_into_groups(students))

    students = {0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4, 5], 4: [2, 3], 5: [3]}
    print(divide_into_groups(students))


"""
SPECS:

TIME COMPLEXITY: O(n)
[O(n) by amortized analysis, as the in the worst case (everyone wants to be alone),
the nested loop runs 2 times and breaks out as the nemesis contains all students]
SPACE COMPLEXITY: O(n)
"""
