import re
from typing import Iterable, Generator, TypedDict
from pathlib import Path
from urllib import request
import json


LIB_URL = "http://localhost:1234/stream/json"
LIBRARY_DB = Path("library_clean.csv")
LOST_THRESHOLD = -300


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


def extract_year(morpokh_year: str) -> int:
    if match := re.search(r"(?P<year>-?\d+)", morpokh_year):
        return int(match.group("year"))

    raise ValueError("Cannot extract year")


def hide_lost_books(iterable: Iterable[Book]) -> Generator[Book, None, list[Book]]:
    """
    Generator Explanation:
        - Book: is what we yield one by one
        - None: is the kind of message we expact from outside
        - list[Book]: is what we get after the full run
    """
    lost_books = []

    for book in iterable:
        if (
            # Not lent right now
            book["lent_since"] is None
            # or it's not lent sooo long ago
            or extract_year(book["lent_since"]) >= LOST_THRESHOLD
        ):
            yield book

        else:
            lost_books.append(book)

    return lost_books
