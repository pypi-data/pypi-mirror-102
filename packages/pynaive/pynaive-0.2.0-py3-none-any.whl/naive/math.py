"""A module with a simple function."""


from typing import Sequence


class EmptyListError(Exception):
    """Thrown in the `average` function when an empty iterable is detected."""


def average(numbers: Sequence[float]) -> float:
    """Computes average value of a list of numbers.

    Args:
        numbers: a list of numbers

    Returns:
        average value of the specified list of numbers

    Raises:
        EmptyListError if the list is empty
    """
    total = 0.0
    count = 0
    for n in numbers:
        count += 1
        total += n
    if count == 0:
        raise EmptyListError
    return total / count
