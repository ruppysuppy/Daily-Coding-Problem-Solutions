"""
Problem:

The United States uses the imperial system of weights and measures, which means that
there are many different, seemingly arbitrary units to measure distance. There are 12
inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity of one unit to
the correct amount of any other unit. You should also allow for additional units to be
added to the system.
"""

from typing import Union


class UnitConverter:
    def __init__(self) -> None:
        # default available metrics
        self.metrics = {
            "inch": 1,
            "foot": 1 * 12,
            "yard": 3 * 1 * 12,
            "chain": 22 * 3 * 1 * 12,
        }

    def add_unit(
        self, new_unit: str, available_unit: str, value: Union[int, float]
    ) -> None:
        # add a new unit with respect to an unit already present
        if available_unit not in self.metrics:
            raise ValueError(f"Unit not found: {available_unit}")
        self.metrics[new_unit] = self.metrics[available_unit] * value

    def convert(
        self,
        source_unit: str,
        result_unit: str,
        value: Union[int, float],
        precision: int = 4,
    ) -> float:
        # convert one metric to another, rounds off the result to required decimal
        # places
        if source_unit not in self.metrics:
            raise ValueError(f"Unit not found: {source_unit}")
        if result_unit not in self.metrics:
            raise ValueError(f"Unit not found: {result_unit}")
        return round(
            value * self.metrics[source_unit] / self.metrics[result_unit], precision
        )


if __name__ == "__main__":
    uc = UnitConverter()
    print(uc.convert("inch", "foot", 24))
    print(uc.convert("inch", "yard", 36))

    uc.add_unit("furlong", "chain", 10)

    print(uc.convert("inch", "furlong", 4 * 36 * 22 * 10))
    print(uc.convert("foot", "yard", 4))
    print(uc.convert("chain", "inch", 2))
    print(uc.convert("chain", "foot", 3))

    # NOTE: "centimeter" is not a part of imperial system, its used to show that
    # smaller units works too
    uc.add_unit("centimeter", "inch", 0.394)
    print(uc.convert("centimeter", "foot", 1))
