"""
Problem:

You are given an array of length 24, where each element represents the number of new
subscribers during the corresponding hour. Implement a data structure that efficiently
supports the following:

- update(hour: int, value: int): Increment the element at index hour by value.
- query(start: int, end: int): Retrieve the number of subscribers that have signed up
  between start and end (inclusive).

You can assume that all values get cleared at the end of the day, and that you will not
be asked for start and end values that wrap around midnight.
"""


class Hourly_Subscribers:
    def __init__(self) -> None:
        self.sub_count = [0 for _ in range(24)]

    def update(self, hour: int, value: int) -> None:
        self.sub_count[hour - 1] += value

    def query(self, start: int, end: int) -> int:
        return sum(self.sub_count[start : end + 1])


if __name__ == "__main__":
    hs = Hourly_Subscribers()

    hs.update(2, 50)
    hs.update(5, 100)

    print(hs.query(1, 7))

    hs.update(2, 10)

    print(hs.query(1, 7))
