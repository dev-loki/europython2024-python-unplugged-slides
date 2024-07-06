#!/usr/bin/python

from contextlib import suppress
import random
import csv
from pathlib import Path
from typing import Any, NamedTuple, Self
from functools import partialmethod
import http.server
import json
import socketserver
import sys
from datetime import datetime


## Base data for generating text
ADJECTIVES = Path("data/adjectives.txt").read_text().strip().splitlines()
AUTHOR_TITLES = (
    Path("data/author_titles.txt").read_text().strip().splitlines() + [""] * 5
)
EXCERPT_ACTION = Path("data/excerpt_actions.txt").read_text().strip().splitlines()
EXCERPT_ADJECTIVE = Path("data/excerpt_adjectives.txt").read_text().strip().splitlines()
EXCERPT_CHAR = Path("data/excerpt_chars.txt").read_text().strip().splitlines()
EXCERPT_LOCATION = Path("data/excerpt_locations.txt").read_text().strip().splitlines()
EXCERPT_PLOT_ELEMENT = (
    Path("data/excerpt_plot_elements.txt").read_text().strip().splitlines()
)
GENRES = Path("data/genres.txt").read_text().strip().splitlines()
LOCATIONS = Path("data/locations.txt").read_text().strip().splitlines()
NAMES_FIRST = Path("data/names_first.txt").read_text().strip().splitlines()
NAMES_SECOND = Path("data/names_second.txt").read_text().strip().splitlines()
NOUNS = Path("data/nouns.txt").read_text().strip().splitlines()
SUFFIXES = Path("data/suffixes.txt").read_text().strip().splitlines()
YEAR_EVENTS = Path("data/events.txt").read_text().strip().splitlines()

MIN_DATE = -500
MAX_DATE = 1000
PORT = 8123
CSV_FILE = "library.csv"


#####################################
## Generator objects and functions ##
#####################################


class AnkhDate(NamedTuple):
    year: int | None = None
    month: int | None = None

    def __str__(self) -> str:
        if not self.year:
            return "unknown"

        if self.month == 1:
            return f"year {self.year:04d} in the {self.month}st month"
        if self.month == 2:
            return f"year {self.year:04d} in the {self.month}nd month"
        if self.month == 3:
            return f"year {self.year:04d} in the {self.month}rd month"
        return f"year {self.year:04d} in the {self.month}th month"

    @classmethod
    def random(cls, max_date: int = MAX_DATE) -> Self:
        if random.randint(1, 100) < 5:
            return cls()

        try:
            year = random.randint(MIN_DATE, max_date - 1)
        except Exception:
            year = 42
        month = random.choice(list(range(1, 13)) + [7, 7, 7, 7])

        return cls(year, month)


def title_generator() -> str:
    return (
        f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} {random.choice(SUFFIXES)}"
    )


def ankh_morpok_year() -> str:
    match random.randint(0, 14):
        case 0:
            return f"The year of {random.choice(YEAR_EVENTS)}"
        case 1:
            return f"The 1st year after {random.choice(YEAR_EVENTS)}"
        case 2:
            return f"The 2nd year after {random.choice(YEAR_EVENTS)}"
        case 3:
            return f"The 3rd year after {random.choice(YEAR_EVENTS)}"
        case yearno:
            return f"The {yearno}th year after {random.choice(YEAR_EVENTS)}"


def book_location() -> str:
    vertical = random.choice(("top", "middle", "bottom"))
    horizontal_m = random.randint(1, 15)
    directions = random.choice(("start", "end"))

    return (
        f"{random.choice(LOCATIONS)}: {vertical} shelve. "
        f"{horizontal_m}m from the {directions}"
    )


def excerpt() -> str:
    action = random.choice(EXCERPT_ACTION)
    adjective = random.choice(EXCERPT_ADJECTIVE)
    subject = random.choice(EXCERPT_CHAR)
    location = random.choice(EXCERPT_LOCATION)
    plot_element = random.choice(EXCERPT_PLOT_ELEMENT)

    structures = [
        lambda: f"{subject.capitalize()} {action} {location}.",
        lambda: f"{location.capitalize()}, {subject} {action}.",
        lambda: f"With {adjective} intent, {subject} {action} {location}.",
        lambda: f"{action.capitalize()}, {subject} did, {location}.",
        lambda: f"A {adjective} scene unfolded as {subject} {action} {location}.",
        lambda: f"{location.capitalize()} bore witness as {subject} {action}.",
        lambda: f"In a {adjective} turn of events, {subject} {action} {location}.",
        lambda: f"Amidst {adjective} surroundings, {subject} {action} {location}.",
        lambda: f"Without hesitation, {subject} {action} {location}.",
        lambda: f"{location.capitalize()} trembled as {subject} {action}.",
        lambda: f"Legends speak of how {subject} {action} {location}.",
        lambda: f"In a display of {adjective} prowess, {subject} {action} {location}.",
        lambda: f"Whispers spread of {subject} who {action} {location}.",
        lambda: f"{subject.capitalize()} stood {adjective}, poised to {action} {location}.",
        lambda: f"Time seemed to slow as {subject} {action} {location}.",
        lambda: f"Against all odds, {subject} {action} {location}.",
        lambda: f"{location.capitalize()} had never seen such a sight: {subject} {action}.",
    ]

    return random.choice(structures)() + " " + plot_element


def catalogued_date() -> AnkhDate:
    return AnkhDate.random()


def person() -> str:
    first_name = random.choice(NAMES_FIRST)
    second_name = random.choice(NAMES_SECOND)
    return f"{first_name} {second_name}"


def author() -> str:
    if title := random.choice(AUTHOR_TITLES):
        return f"{title} {person()}"

    return person()


def lent_by() -> str | None:
    if random.choice((True, False)):
        return person()

    return None


def lent_since(max_date: AnkhDate) -> AnkhDate:
    if not max_date.year:
        return AnkhDate.random()

    return AnkhDate.random(max_date.year)


def lent_times() -> int:
    return random.choice(list(range(10)) + [42])


def generate_book() -> dict[str, Any]:
    catalogued = catalogued_date()
    lent_name = lent_by()

    return dict(
        title=title_generator(),
        author=author(),
        lent_by=lent_name,
        lent_since=str(lent_since(catalogued)) if lent_name else None,
        lent_times=lent_times(),
        year=str(ankh_morpok_year()),
        catalogued=str(catalogued),
        location=book_location(),
        excerpt=excerpt(),
    )


######################
## Server functions ##
######################


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    HTTP_OK = 200
    HTTP_NOT_FOUND = 404

    def _set_meta(self, code: int, content_type: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    # not really necessary, but just to show off partialmethod
    ok = partialmethod(_set_meta, HTTP_OK)
    ok_json = partialmethod(_set_meta, HTTP_OK, "application/json")
    ok_csv = partialmethod(_set_meta, HTTP_OK, "text/csv")

    @staticmethod
    def csv_gen():
        with open(CSV_FILE, "rb") as file:
            yield from file.readlines()

    def do_GET(self) -> None:
        match self.path:
            case "/book":
                self.ok_json()

                book = generate_book()

                self.wfile.write(json.dumps(book).encode())

            case "/columns":
                self.ok_csv()

                columns = next(self.csv_gen()).strip()

                self.wfile.write(columns)

            case "/library":
                self.ok_csv()

                library = [generate_book() for _ in range(100)]

                self.wfile.write(json.dumps(library).encode())

            case "/stream":
                self._set_meta(self.HTTP_OK, "text/csv")

                with suppress(BrokenPipeError, ConnectionResetError):
                    for line in self.csv_gen():
                        self.wfile.write(line)
                        sleep(0.1)

            case path:
                self._set_meta(self.HTTP_NOT_FOUND, "text/plain")

                self.wfile.write(f"path '{path}' does not exist".encode())

    def log_message(self, format, *args):
        print(
            f"[{datetime.now().strftime("%H:%M:%S.%f")}] - "
            f"{self.client_address[0]} - {format % args}",
            flush=True,
        )


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """ThreadingMixin allows to handle multiple concurrent requests"""

    pass


def serve(port: int = PORT) -> None:
    with ThreadingHTTPServer(("", port), RequestHandler) as httpd:
        print(f"Starting on: http://localhost:{port}")
        print(f" - GET http://localhost:{port}/columns")
        print(f" - GET http://localhost:{port}/stream", flush=True)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down...")
            sys.exit(1)


##############################
## Additional CLI functions ##
##############################


def save_csv(filename: str, num: int):
    if not filename.endswith(".csv"):
        filename += ".csv"

    cols = generate_book().keys()
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()

        for _ in range(num):
            book = generate_book()
            writer.writerow(book)
            if random.randint(1, 42) == 13:
                # Random duplicates
                writer.writerow(book)


def save_json(filename: str, num: int, jsonl: bool) -> None:
    if jsonl and not filename.startswith(".jsonl"):
        filename += ".jsonl"
    elif not jsonl and not filename.startswith(".json"):
        filename += ".json"

    books = []
    for _ in range(num):
        book = generate_book()
        books.append(book)
        if random.randint(1, 42) == 13:
            # Random duplicates
            books.append(book)

    if jsonl:
        if not filename.endswith(".jsonl"):
            filename += ".jsonl"

        with open(filename, "w") as f:
            f.writelines([json.dumps(book) + "\n" for book in books])
    else:
        if not filename.endswith(".json"):
            filename += ".json"
        with open(filename, "w") as f:
            f.write(json.dumps(books))


def print_book(counter: int) -> None:
    for _ in range(counter):
        book = generate_book()
        print(book["title"], book["author"])
        for key, value in book.items():
            if key not in ("title", "author"):
                print(f"  {key}:\t{value}")
        print(flush=True)


def cli() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Create CSV/JSON or serve")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Print book
    parser_book = subparsers.add_parser("book")
    parser_book.add_argument("num", type=int, nargs="?", default=1, help="Print books")

    # Serve part
    parser_serve = subparsers.add_parser("serve")
    parser_serve.add_argument(
        "port", type=int, nargs="?", default=8123, help="Port number to serve"
    )

    # Save part
    parser_csv = subparsers.add_parser("csv")
    parser_csv.add_argument(
        "num",
        type=int,
        nargs="?",
        default=1000,
        help="Number of records to save to CSV",
    )
    parser_csv.add_argument(
        "filename",
        type=str,
        nargs="?",
        default="output.csv",
        help="Filename to save CSV records",
    )

    parser_json = subparsers.add_parser("json")
    parser_json.add_argument(
        "num",
        type=int,
        nargs="?",
        default=1000,
        help="Number of records to save to JSON",
    )
    parser_json.add_argument(
        "filename",
        type=str,
        nargs="?",
        default="output",
        help="Filename to save JSON records",
    )
    parser_json.add_argument(
        "--jsonl", action="store_true", help="Save records to JSONL format"
    )

    args = parser.parse_args()
    if args.command == "serve":
        serve(args.port)
    elif args.command == "csv":
        save_csv(args.filename, args.num)
    elif args.command == "json":
        save_json(args.filename, args.num, bool(args.jsonl))
    elif args.command == "book":
        print_book(args.num)


if __name__ == "__main__":
    cli()
