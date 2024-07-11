from pathlib import Path
from collections.abc import Iterable
from itertools import chain, pairwise
from urllib import request
from typing import TypedDict
import json
from csv import DictWriter


LIB_URL = "http://localhost:1234/stream/json"
LIBRARY_DB = Path("library_clean.csv")


class Book(TypedDict):
    title: str
    author: str
    lent_by: str | None
    lent_since: str | None
    lent_times: int
    year: str
    catalogued: str
    location: str
    excerpt: str


def fetch_library() -> Iterable[Book]:
    response = request.urlopen(LIB_URL)

    for line in response:
        yield json.loads(line)


def generate_non_duplicates(books: Iterable[Book]) -> Iterable[Book]:
    """
    This takes an iterable for books
    and yields in the same format, but excluding duplicates

    pairwise:
        We use pairwise to get all subsequent pairs of books.

    chain:
        We use chain to lazily take care of the the edge case,
        that we'd have to yield either the first or last book
        additionally
    """
    for book, book2 in pairwise(chain((None,), books)):
        assert book2 is not None  # just for mypy
        if book == book2:
            print("Duplicate found!")
            continue

        yield book2


def _alt_generate_non_duplicates(books: Iterable[Book]) -> Iterable[Book]:
    """
    We don't have to use pairwise/chain but I prefer
    the first solution as this "feels" larger
    """
    iterator = iter(books)

    left = next(iterator)
    yield left

    for right in iterator:
        if left != right:
            yield right
            left = right


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    columns = Book.__annotations__.keys()
    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=columns)
        writer.writeheader()

        # We could now use batch again :)
        for book in generate_non_duplicates(book_gen):
            writer.writerow(book)


if __name__ == "__main__":
    only_save_non_duplicates()
