"""
Problem:

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2
containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n
\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a
file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a
second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file
within our file system. For example, in the second example above, the longest absolute
path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the
double quotes).

Given a string representing the file system in the above format, return the length of
the longest absolute path to a file in the abstracted file system. If there is no file
in the system, return 0.
"""


def count_tabs(string: str) -> int:
    return string.count("\t")


def longest_dir(string: str) -> int:
    dir_list = string.split("\n")
    length = len(dir_list)
    longest_directory_length = 0
    # calculating the length of the longest absolute path
    for i in range(length - 1, -1, -1):
        temp = dir_list[i]
        temp_dir = temp.lstrip("\t")
        # skipping calculation if it is not a file
        if temp_dir.find(".") == -1:
            continue
        # counting the number of tabs to check the location
        # (0 tabs = root, 1 tab = sub-directory, 2 tabs = sub-sub-directory, ...)
        count = count_tabs(temp)
        # moving back through the list to recreate the entire directory
        for j in range(i, -1, -1):
            if count_tabs(dir_list[j]) < count:
                temp_dir = dir_list[j].lstrip("\t") + "/" + temp_dir
                temp = dir_list[j]
                count = count_tabs(temp)
        # storing the longest directory path length
        longest_directory_length = max(longest_directory_length, len(temp_dir))
    return longest_directory_length


if __name__ == "__main__":
    print(longest_dir("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
    print(
        longest_dir(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2"
            + "\n\t\t\tfile2.ext"
        )
    )


"""
SPECS:

TIME COMPLEXITY: O(n ^ 2)
SPACE COMPLEXITY: O(n)
"""
