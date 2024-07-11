from typing import Iterable, TypedDict
from collections import defaultdict


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


def most_common_words_in_title(books: Iterable[Book]) -> dict[str, int]:
    """
    Much more concise :)
    """
    word_counter = defaultdict(int)

    for book in books:
        for word in book["title"].split():
            word_counter[word] += 1

    return word_counter
