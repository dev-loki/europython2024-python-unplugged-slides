from pathlib import Path
from collections.abc import Iterable
from itertools import batched, islice
from urllib import request
from typing import TypedDict
import json
from csv import DictWriter


LIB_URL = "http://localhost:1234/stream/json"
LIBRARY_DB = Path("library_raw.csv")


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
        yield json.loads(line)  # mypy might complain!


def work_on_the_library(*, max_entries: int = 100) -> None:
    """Force keyword argument with * as it is surprising behaviour"""
    library_generator = fetch_library()

    # We extract the available columns from the TypedDict
    column_names = Book.__annotations__.keys()

    with LIBRARY_DB.open("w") as file:
        # Initialize the object which helps us writing into CSV
        writer = DictWriter(file, fieldnames=column_names)

        # Write the columns in the first line
        writer.writeheader()

        # we can save our Generator in a file for later use
        # this is also easier to read if you create a pipeline of
        # data manipulation
        yield_10_items_at_a_time = batched(library_generator, 10)

        # Islice used to respect our boundary
        # Secret: The server would create entries forever ;)
        for batch in islice(yield_10_items_at_a_time, max_entries):
            # And write (up to) 10 items at a time into the csv
            writer.writerows(batch)


if __name__ == "__main__":
    work_on_the_library(max_entries=100)
