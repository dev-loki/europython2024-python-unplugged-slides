---
layout: image-left
image: images/data-cleaning.png
---

# Chapter 2: Cleaning data

<v-click>

_(wrong universe again - I know)_

</v-click>

---
layout: image-right
image: images/magic-cooking-book-duplicate.png
---

## Duplicate books

<v-clicks depth="2">

- We want to fetch data from the library...
- But as it is a magical library from Ankh Morpork, 
  the books will duplicate!
- The orang utan librarian of the Unseen University wants the list of 
  unique books as CSV (obviously!)
- This is **NOT** a leetcode talk ;)

</v-clicks>

---

````md magic-move
```python
"""This is our current version"""
from csv import DictWriter
from itertools import batched


LIBRARY_DB = "library_raw.csv"
COLUMNS = BookResponse.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with Path(LIBRARY_DB).open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        for batch in batched(book_gen, 10):
            for book in filter_double_books(batch):
                writer.writerows(batch)
```

```python
from csv import DictWriter


LIBRARY_DB = "library_raw.csv"
COLUMNS = BookResponse.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with Path(LIBRARY_DB).open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        last_book = None
        for book in bookgen:
            if book != last_book:
                writer.writerow(book_gen)
            last_book = book
```

```python
from csv import DictWriter
from itertools import pairwise


LIBRARY_DB = "library_raw.csv"
COLUMNS = BookResponse.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with Path(LIBRARY_DB).open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        for book, book2 in pairwise(book_gen):
            if book != book2:
                writer.writerow(book_gen)
```

```python
from csv import DictWriter
from itertools import pairwise


LIBRARY_DB = "library_raw.csv"
COLUMNS = BookResponse.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with Path(LIBRARY_DB).open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        book = book2 = None
        for book, book2 in pairwise(lib):
            if book != book2:
                writer.writerow(book)

        # NOT a fan:
        if book2 and book != book2:
            writer.writerow(book2)
```
```python
from csv import DictWriter
from itertools import chain, pairwise


LIBRARY_DB = "library_raw.csv"
COLUMNS = BookResponse.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with Path(LIBRARY_DB).open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        for book, book2 in pairwise(chain([None], lib):
            if book != book2:
                writer.writerow(book2)
```
````

---
layout: center
---

### What new modules did we learn about?

---
layout: center
---

#### pairwise


TODO: Finish

---
layout: center
---

#### chain

TODO: Finish

---
layout: center
---

## Saving the deduplicated data

Basically just an excuse to show grouping of contextmanagers

```python
OUTPUT_FILE = 'library_clean.csv'

def remove_duplicates(iterable: Iterable) -> Iterator: ...


def clean_data(input_csv_file: str) -> str:
    out_name = input_csv_file.replace(".csv", "-clean.csv")

    with (
        Path(input_csv_file).open("r") as read_file,
        Path(out_name).open("w") as write_file,
    ):
        reader = csv.DictReader(read_file)
        writer = csv.DictWriter(write_file)

        for row in remove_duplicates(reader):
            writer.writerow(row)
```

---
layout: center
---

### Remove the books we cannot get back

---

````md magic-move
```python
"""
We start by creating a new function,
and iterating through the books...
"""
def hide_lost_books(iterable: Iterable) -> Iterator:
    for book in iterable:
        if book[?]
```

```python
"""
and iterating through the books...
... until we find...
"""
def hide_lost_books(iterable: Iterable) -> Iterator:
    for book in iterable:
        if book[?]  # <--- wait a minute
```

```python
"""
... until we find...
Let's make our live easier again
"""
def hide_lost_books(
    iterable: Iterable[BookResponse]
) -> Iterator[BookResponse]:
    for book in iterable:
        if book["lent_since"] < "???"  # <--- wait a minute²
```

```python
"""
Let's make our live easier again
- we won't go too much into detail 
- there are specialized typing talks :)
"""
def hide_lost_books(
    iterable: Iterable[BookResponse]
) -> Iterator[BookResponse]:
    example_year = "year 450 in the 3rd month"
    for book in iterable:
        # How do we get the year?
        if book["lent_since"] < "???"  
```

```python {1-4,8-9}
"""
Nothing too complicated...
"""
import re


def extract_year(morpokh_year: str) -> int:
    """Search for first number in year string. Right?"""
    return int(re.search(r"(\d)", morpokh_year).group(0))


def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    ...
```

```python {1-4,8-9}
"""
But how do we know this really does what we want?
We could try it, but this is boring and doesn't scale!
"""
import re


def extract_year(morpokh_year: str) -> int:
    return int(re.search(r"(\d)", morpokh_year).group(0))


def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    ...
```
````

---
layout: image-right
image: images/orang-utan-doctor.png
---

## Doctest - to the rescue

```python
import re


def extract_year(morpokh_year: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450
    """
    return int(re.search(r"(\d)", morpokh_year).group(0))
```

<v-click>

```sh {1|3-8|8-11}
python -m doctest code/chapter2/doctest_example.py

**********************************************************************
File ".../code/chapter2/doctest_example.py", line 8, in doctest_example.extract_year
Failed example: extract_year("year 450 in the 3rd month")
Expected: 450
Got: 4
**********************************************************************
1 items had failures:
   1 of 1 in doctest_example.extract_year
***Test Failed*** 1 failures.
```

</v-click>

---

Long story short: lets fix it!

````md magic-move
```python
import re


def extract_year(morpokh_year: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450

    >>> extract_year("year 0 in the 3rd month")
    0
    """
    return int(re.search(r"(\d+)", morpokh_year).group(0))
```

```python
import re


def extract_year(morpokh_year: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450

    >>> extract_year("year -450 in the 3rd month")
    -450

    >>> extract_year("year 0 in the 3rd month")
    0
    """
    return int(re.search(r"(-?\d+)", morpokh_year).group(0))
```
````

---


````md magic-move

```python {2,6-9}
"""
Let's continue with hiding the lost books from our catalogue
"""
def extract_year(morpokh_year: str) -> int: ...

def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
```

```python
"""
Use `yield from` to directly generate from this and unindent the code
-> Lazy :)
-> Does not work in async code :(
"""
def extract_year(morpokh_year: str) -> int: ...

def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    yield from (
        book 
        for book in iterable
        if extract_year(book["lent_since"]) >= -300
    )
```

```python
"""
But now we want to keep track of the lost books.
Using a global variable :/ ?
"""
def extract_year(morpokh_year: str) -> int: ...

lost_books = []

def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)
```

```python
"""
Using a global variable :/ ?
Yield the lost books last? -> ugly with return type
"""
def extract_year(morpokh_year: str) -> int: ...


def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    yield lost_books
```

```python
"""
Yield the lost books last? -> ugly with return type

"""
def extract_year(morpokh_year: str) -> int: ...


def hide_lost_books(iterable: Iterable[BookResponse]) -> Iterator[BookResponse]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    return lost_books
```

```python
"""
Let's adapt our return type.
Generator[yield type, send type, return type]
"""
def hide_lost_books(iterable: Iterable[BookResponse]) -> Generator[BookResponse, None, list[BookResponse]]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    return lost_books
```

```python
"""
Generator[yield type, send type, return type]
                      ^^^^----[ lets not go into this ;) ]
"""
def hide_lost_books(
    iterable: Iterable[BookResponse]
) -> Generator[BookResponse, None, list[BookResponse]]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    return lost_books
```


```python {2,7-19}
"""
And this is how we use it :)
"""
def hide_lost_books(iterable: Iterable[BookResponse]) -> \
    Generator[BookResponse, None, list[BookResponse]]: ...

def get_return_value():
    non_hidden_generator = hide_lost_books(mylibrary)

    # consume the iterator (just as example)
    non_lost_books = list(non_hidden_generator)

    dropped_books = []
    try:
        next(non_hidden_generator)
    except StopIteration as e:
        # tbh: I wished there was a better way
        dropped_books = e.value

    return non_lost_books, dropped_books
```
````
