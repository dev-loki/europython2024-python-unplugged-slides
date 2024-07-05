from itertools import batched
from typing import Iterable, TypeVar


T = TypeVar("T")


def overlapping_batched(iterable: Iterable[T], n: int) -> Iterable[tuple[T, ...]]:
    """
    Like itertools.batched but includes the last element from previous batch
    as first item.

    >>> list(overlapping_batched([1,2,3,4], 2))
    [(1, 2), (2, 3, 4)]

    >>> list(overlapping_batched([1,2,3], 1))
    [(1,), (1, 2), (2, 3)]
    """
    iterator = iter(iterable)
    last_element = None

    for batch in batched(iterator, n):
        if last_element is not None:
            yield tuple([last_element, *batch])
        else:
            yield tuple(batch)

        last_element = batch[-1]
