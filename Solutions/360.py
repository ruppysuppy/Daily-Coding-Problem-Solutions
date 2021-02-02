"""
Problem:

You have access to ranked lists of songs for various users. Each song is represented as
an integer, and more preferred songs appear earlier in each list. For example, the list
[4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.

Given a set of these ranked lists, interleave them to create a playlist that satisfies
everyone's priorities.

For example, suppose your input is {[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}. In this
case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].
"""

from typing import List

from DataStructures.PriorityQueue import MinPriorityQueue


def interleave_playlist(playlists: List[List[int]]) -> List[int]:
    queue = MinPriorityQueue()
    result = []
    # priority queue generation
    # offset used to ensure that in case a song occours 2nd time (in different
    # playlists), the priorities for all the songs in the 2nd playlist gets offset
    for playlist in playlists:
        offset = 0
        for priority, song in enumerate(playlist):
            if song not in queue:
                queue.push(song, offset + priority)
            else:
                old_priority = queue.get_priority(song)
                offset += max(priority, old_priority)
                queue.update_key(song, offset + priority)
    # priority queue updation
    # updating the queue is necessary to ensure if a song (occuring 2nd time in a
    # different playlists) gets push down the queue, all the songs in the playlist
    # (where the song appeared 1st) also get pushed down
    for playlist in playlists:
        offset = 0
        for priority, song in enumerate(playlist):
            old_priority = queue.get_priority(song)
            if old_priority > priority:
                offset = max(offset, old_priority - priority)
            queue.update_key(song, priority + offset)

    while not queue.is_empty():
        result.append(queue.extract_min())
    return result


if __name__ == "__main__":
    print(interleave_playlist([[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]))


"""
SPECS:

TIME COMPLEXITY: O(n x log(n))
SPACE COMPLEXITY: O(n)
[n = number of elements in the matrix]
"""
