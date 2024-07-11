from typing import Iterable, TypedDict, Counter
from itertools import chain


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


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    # This will generate a looong stream of words in all the
    # books and the specified columns
    book_word_generator = chain.from_iterable(
        chain(
            book["title"].split(),
            book["author"].split(),
            book["excerpt"].split(),
        )
        for book in books
    )

    return Counter(book_word_generator)
