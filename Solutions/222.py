"""
Problem:

Given an absolute pathname that may have . or .. as part of it, return the shortest
standardized path.

For example, given /usr/bin/../bin/./scripts/../, return /usr/bin/.
"""

from DataStructures.Stack import Stack


def get_shortest_standardized_path(path: str) -> str:
    path_list = path.split("/")
    stack = Stack()

    for curr_directory in path_list:
        if curr_directory == ".":
            continue
        elif curr_directory == "..":
            stack.pop()
        else:
            stack.push(curr_directory)
    return "/".join(stack)


if __name__ == "__main__":
    print(get_shortest_standardized_path("/usr/bin/../bin/./scripts/../"))


"""
SPECS:

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
"""
