"""
Problem:

Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

Example:

Input = "/usr/bin/../bin/./scripts/../"
Output = "/usr/bin/"
"""


def get_shortest_standardized_path(path):
    path_list = path.split("/")
    stack = []

    for curr in path_list:
        if curr == "..":
            stack.pop()
        elif curr == ".":
            continue
        else:
            stack.append(curr)

    return "/".join(stack)


if __name__ == "__main__":
    print(get_shortest_standardized_path("/usr/bin/../bin/./scripts/../"))
