from collections.abc import Iterable
from itertools import batched
from urllib import request
from typing import TypedDict
import json


# This is from the generator.py code inside of /code
LIB_URL = "http://localhost:1234/stream/json"


class Book(TypedDict):
    """
    This is basically a dict with some types plunged onto it.
    - Tools like mypy, ruff, etc. can read this.
    - IDEs can read this and give you nice hints
    - Tools like pydantic can validate this :)
        https://docs.pydantic.dev/2.0/usage/types/dicts_mapping/#typeddict
    """

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
    """
    This fetches pure byte data from a server
    And then transforms it to json and yield lazily a book
    """
    response = request.urlopen(LIB_URL)
    for line in response:
        yield json.loads(line)  # mypy might complain!


def do_stuff_with_books(_books: tuple[Book, ...]) -> None:
    pass


def work_on_the_library() -> None:
    """
    We're now using the batched function
    """
    library_generator = fetch_library()

    for batch in batched(library_generator, 10):
        do_stuff_with_books(batch)
