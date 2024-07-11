import re
from typing import Iterable, NamedTuple, TypedDict, Iterator
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


class BookMeta(NamedTuple):
    current: Book
    lost: list[Book]


def hide_lost_books(iterable: Iterable[Book]) -> Iterator[BookMeta]:
    lost_books = []

    for book in iterable:
        if book["lent_since"] is None:
            yield BookMeta(book, lost_books)
        elif extract_year(book["lent_since"]) >= -300:
            yield BookMeta(book, lost_books)
        else:
            lost_books.append(book)
