"""
Some new stuff here (especially for beginners):
1. def batched[T]: what the T is that?
    - T is an arbitrary thing.
    - It means that we take a collection of "Something"
    - ... and return a nested collection
2. Iterable vs Iterator
    - iter(Iterable) gives us an Iterator
    - Iterable (contains __iter__ method)
    - Iterator (has __iter__ and __next__)
"""

from collections.abc import Iterable, Iterator
from itertools import islice


def batched[T](
    some_iterable: Iterable[T],
    size: int = 2,
) -> Iterator[tuple[T, ...]]:
    iterator = iter(some_iterable)

    while batch := tuple(islice(iterator, size)):
        yield batch
