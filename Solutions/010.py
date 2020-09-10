"""
Problem:

Implement a job scheduler which takes in a function f and an integer n, and calls f
after n milliseconds.
"""

from time import sleep
from typing import Callable


def get_seconds_from_milliseconds(time_mil: int) -> float:
    return time_mil / 1000


def job_scheduler(function: Callable, delay: int) -> None:
    sleep(get_seconds_from_milliseconds(delay))
    function()


# function to test the job scheduler
def print_hello() -> None:
    print("Hello!")


if __name__ == "__main__":
    job_scheduler(print_hello, 1)
    job_scheduler(print_hello, 500)
    job_scheduler(print_hello, 1000)
