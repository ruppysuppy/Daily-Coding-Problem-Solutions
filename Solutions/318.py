"""
Problem:

You are going on a road trip, and would like to create a suitable music playlist. The
trip will require N songs, though you only have M songs downloaded, where M < N. A
valid playlist should select each song at least once, and guarantee a buffer of B songs
between repeats.

Given N, M, and B, determine the number of valid playlists.
"""


def get_num_of_valid_playlist(N: int, M: int, B: int) -> int:
    # possible ways of selecting each song = [
    #   (N), (N - 1), (N - 2) ... (N - B), (N - B), (N - B), ... till M songs
    # ]
    if B >= N:
        return 0
    result = 1
    curr = N
    for i in range(M):
        result = result * curr
        # after B songs, 1 new song will be available and 1 will be off limits, so the
        # number of available songs will be locked at (N - B)
        if i < B:
            curr -= 1
    return result


if __name__ == "__main__":
    # (1, 2, 1), (2, 1, 2)
    print(get_num_of_valid_playlist(2, 3, 1))

    # (1, 2, 3, 1), (1, 3, 2, 1),
    # (2, 1, 3, 2), (2, 3, 1, 2),
    # (3, 1, 2, 3), (3, 2, 1, 3)
    print(get_num_of_valid_playlist(3, 4, 2))


"""
SPECS:

TIME COMPLEXITY: O(m)
SPACE COMPLEXITY: O(1)
"""
