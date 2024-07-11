from typing import TypedDict, NamedTuple, Iterable
from itertools import groupby


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


def family_name(book: Book) -> str:
    if book["lent_by"]:
        return book["lent_by"].split()[1]
    return ""


class BiggestLender(NamedTuple):
    family: str
    lent_books: int


def family_lent_the_most(books: Iterable[Book]) -> BiggestLender:
    # Filter books that have been lent out
    # We need it to be sorted by the key to be grouped!
    only_lent_books = sorted((b for b in books if b["lent_by"]), key=family_name)

    # This groups an iterable by a specific key
    books_by_family_name = groupby(only_lent_books, key=family_name)

    # Find the family with the most lent books
    family, lent_books = max(
        ((family, list(group)) for family, group in books_by_family_name),
        key=lambda item: len(item[1]),
    )

    return BiggestLender(family, len(lent_books))
