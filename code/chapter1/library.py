import json
from urllib import request
from typing import TypedDict

URL_BOOK = "http://localhost:8123/book"


class BookResponse(TypedDict):
    title: str
    author: str
    lent_by: str | None
    lent_since: str | None
    lent_times: int
    year: str
    catalogued: str
    location: str
    excerpt: str


def fetch_book() -> BookResponse:
    response = request.urlopen(URL_BOOK).read()
    return json.loads(response)


def main() -> None:
    book = fetch_book()
    print(book)

    # Define result as TypedDict

    # Fetch books as batched
    # save locally in sqlite
    ...


if __name__ == "__main__":
    main()
