"""
Problem:

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between
the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""


HOUR_ANGLE = {
    1: (1 / 12) * 360,
    2: (2 / 12) * 360,
    3: (3 / 12) * 360,
    4: (4 / 12) * 360,
    5: (5 / 12) * 360,
    6: (6 / 12) * 360,
    7: (7 / 12) * 360,
    8: (8 / 12) * 360,
    9: (9 / 12) * 360,
    10: (10 / 12) * 360,
    11: (11 / 12) * 360,
    12: (12 / 12) * 360,
}


def get_displaced_hour_angle(mm: int) -> float:
    return (mm / 60) * (360 / 12)


def get_minutes_angle(mm: int) -> float:
    return (mm / 60) * 360


def get_angle_between_arms(time: str) -> int:
    hh, mm = [int(elem) for elem in time.split(":")]
    hour_angle = (HOUR_ANGLE[hh] + get_displaced_hour_angle(mm)) % 360
    minute_angle = get_minutes_angle(mm)
    return round(abs(hour_angle - minute_angle))


if __name__ == "__main__":
    print(get_angle_between_arms("12:20"))
    print(get_angle_between_arms("12:00"))
    print(get_angle_between_arms("6:30"))
    print(get_angle_between_arms("3:45"))


"""
SPECS:

TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
