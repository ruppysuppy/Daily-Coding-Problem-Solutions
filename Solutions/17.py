"""
Problem:

Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
"""

# Function to count the number of tabs
def count_tabs(string):
    return string.count("\t")


# FUNCTION TO PERFORM THE OPERATION
def longest_dir(string):
    # Getting the required data from the given string
    dir_list = string.split("\n")
    length = len(dir_list)
    longest_directory_length = 0
    longest_directory = ""

    # looping over the list of paths
    for i in range(length - 1, -1, -1):
        # counting the number of tabs to check the location (0 tabs=parent, 1=sub-directory, 2=sub-sub-directory, ...)
        temp = dir_list[i]
        count = count_tabs(temp)
        temp_dir = temp.lstrip("\t")

        # moving back through the list to recreate the entire directory (if it is a file: files have '.')
        if temp_dir.find(".") != -1:
            for j in range(i, -1, -1):
                if count_tabs(dir_list[j]) < count:
                    temp_dir = dir_list[j].lstrip("\t") + "/" + temp_dir
                    temp = dir_list[j]
                    count = count_tabs(temp)

        # if the length of the generated is larger than the previously available longest_directory, details are overwritten
        if longest_directory_length < len(temp_dir):
            longest_directory_length = len(temp_dir)
            longest_directory = temp_dir

    return longest_directory_length


# DRIVER CODE
print(longest_dir("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(
    longest_dir(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    )
)
