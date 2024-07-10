import json
from typing import TypedDict
from urllib import request


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


def fetch_book(url) -> Book:
    response = request.urlopen(url).read()
    return json.loads(response)
