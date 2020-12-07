"""
Problem:

Using a read7() method that returns 7 characters from a file, implement readN(n) which
reads n characters.

For example, given a file with the content "Hello world", three read7() returns
"Hello w", "orld" and then "".
"""

# COUNT_7 stores the number of characters already read from the file
# STASHED_TEXT stores the unreturned data (used in readN)
COUNT_7 = 0
STASHED_TEXT = ""


def read7(filename: str = "data_082.txt") -> str:
    global COUNT_7
    with open(filename, "r") as f:
        f.seek(COUNT_7, 0)
        data = f.read(7)
    COUNT_7 += 7
    return data


def readN(n: int, filename: str = "data_082.txt") -> str:
    global STASHED_TEXT
    for _ in range((n // 7) + 1):
        STASHED_TEXT += read7(filename)
    text = STASHED_TEXT[:n]
    STASHED_TEXT = STASHED_TEXT[n:]
    return text


if __name__ == "__main__":
    print(readN(3))
    print(readN(10))
    print(readN(15))
    print(readN(25))
    print(readN(1000))
    print(readN(1000))
