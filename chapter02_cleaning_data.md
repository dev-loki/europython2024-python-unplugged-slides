---
layout: image-left
image: public/data-cleaning.png
---

<br>
<br>
<br>
<br>
<br>

# Chapter 2: Cleaning data

<hr> 

<v-click>

_(wrong meme universe again - I know)_

</v-click>

---
layout: image-right
image: public/magic-cooking-book-duplicate.png
---

## Duplicate books

<hr> 

<v-clicks depth="2">

- We want to fetch data from the library...
- But: Magical library. Means: the books will duplicate!
- The orang utan librarian of the Unseen University wants the list of 
  unique books as CSV (obviously!)
- This is **NOT** a leetcode talk ;) 
    - no fancy but obvious solution if P in NP
    - also: no super clever text similarity or duplication algorithms

</v-clicks>

<!--
No leetcode -> solutions might not be perfect
- The goal are the tools and not having O(1) algorithms ;)
-->

---

````md magic-move
```python
"""This is our current version"""
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        for batch in batched(lib, 10):
            writer.writerows(batch)
```
```python {16-18}
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_du..plicates() -> None:
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        for batch in batched(book_gen, 10):
            """Filter out the duplicates:"""
            for book in filter_double_books(batch):
                writer.writerows(batch)
```
```python {10-11|12,20-24}
from csv import DictWriter


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    """
    As we watch our code run, we recognize, that
    Books always duplicate in pairs!
    Naive approach incoming
    """
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        last_book = None
        for book in bookgen:
            if book != last_book:
                writer.writerow(book_gen)
            last_book = book
```
```python {2,10,11,12}
from csv import DictWriter
from itertools import pairwise


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    """
    But: We can use pairwise for that!
    """
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        last_book = None
        for book in bookgen:
            if book != last_book:
                writer.writerow(book_gen)
            last_book = book
```
```python {2,16-18}
from csv import DictWriter
from itertools import pairwise


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        for book, book2 in pairwise(book_gen):
            if book != book2:
                writer.writerow(book_gen)
```
```python {10,11,12|10-22|19,24-26}
from csv import DictWriter
from itertools import pairwise


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    """
    Problem: We don't get the last book!
    """
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
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
```python {9-12,19}
from csv import DictWriter


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    """
    We can also use destructuring, but this would 
    defy the purpose of a generator
    """
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        for book, book2 in pairwise([None, *lib]):
            if book != book2:
                writer.writerow(book2)
```
```python {2,11,12|20}
from csv import DictWriter
from itertools import chain, pairwise


LIBRARY_DB = Path("library_raw.csv")
COLUMNS = Book.__annotations.__.keys()


def only_save_non_duplicates() -> None:
    """
    chain to the rescue!
    It lazily chains multiple iterators without effort
    """
    book_gen = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()

        for book, book2 in pairwise(chain([None], lib):
            if book != book2:
                writer.writerow(book2)
```
````

<!--
"Remember this" 

We have written this basic code to just save the data from "magic funnel" to CSV
-->

---
layout: center
hideInToc: true
---

## What new modules did we learn about?

---
layout: center
---

### pairwise

<br><hr><br>

<v-clicks>

- Signature: `def pairwise(iterable: Iterable[T]) -> Iterable[tuple[T, T]]`
- Uses an iterator like `range(10)`...
- ... and creates a new iterator like `((0,1), (1,2), (2,3), ..., (8, 9))`
- other example: `list(pairwise("Hello")) == [("H","e"), ("e","l"), ("l","l"), ("l","o")]` 
- is lazy -> Without `list(...)` or other ways of consuming pairwise does (almost) nothing

</v-clicks>

---
layout: center
---

## chain

<br><hr><br>

<v-clicks depth="2">

- Chains together multiple iterables 
- From this `list(chain('Hello', 'World'))` ...
    - We get this `['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']`
- Advantage: it's lazy and doesn't create a large¹ object, like:
    - `combined_list = [*my_list, *my_other_list]`
    - ¹(not large means: it only holds references)
- It can flatten lists with a classmethod: `chain.from_iterable(...)`

</v-clicks>


---
layout: center
---

## It can flatten lists

_(also a common thing people do themselves)_

<br><hr><br>

```python {1|2|4}
my_list = [[1,2,3], [3,4,5]]
flattened = chain.from_iterable(my_list)

assert list(flattened) == [1,2,3,3,4,5]
```

---
layout: center
---

### ChainMap

<br><hr><br>

_For the brevity of completeness..._

<v-clicks>

- There is also `itertools.ChainMap`
- Works similar to `chain`:
- `cm = ChainMap({"a": 1}, {"b": 2}, {"a": 3})` gives us:
    - `cm["a"] == 1` (Not `3`!)
    - `cm["b"] == 2`
    - `cm["c"] --> KeyError`
- Attention: Different behaviour than `**dict`
    - `{**adict, **bdict} => dict(ChainMap(bdict, adict))`

</v-clicks>

---
layout: center
---

## Saving the deduplicated data

<hr> 

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

<hr> 

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
"""
def hide_lost_books(iterable: Iterable) -> Iterator:
    for book in iterable:
        if book[?]  # <--- wait a minute
```

```python
"""
Let's make our live easier again
"""
def hide_lost_books(
    iterable: Iterable[Book]
) -> Iterator[Book]:
    for book in iterable:
        if book["lent_since"] < "???"
```

```python
"""
We want to extract the year
"""
def hide_lost_books(
    iterable: Iterable[Book]
) -> Iterator[Book]:
    example_year = "year 450 in the 3rd month"
    for book in iterable:
        # How do we get the year?
        if book["lent_since"] < "???"  
```

```python
import re


def extract_year(morporkyear: str) -> int:
    """Search for first number in year string. Easy. Right?"""
    return int(re.search(r"(\d)", morporkyear).group(0))


def hide_lost_books(iterable: Iterable[Book]) -> Iterator[Book]:
    ...
```

```python
import re


def extract_year(morporkyear: str) -> int:
    """
    But how do we know this really does what we want?
    We could try it, but this is boring and doesn't scale!
    """
    return int(re.search(r"(\d)", morporkyear).group(0))


def hide_lost_books(iterable: Iterable[Book]) -> Iterator[Book]:
    ...
```
````

---
layout: image-right
image: public/orang-utan-doctor.png
---

## Doctest - to the rescue

<hr> 

```python
"""Lets start with the same function, but add some
minimal documentation"""
import re


def extract_year(morporkyear: str) -> int:
    """
    This extracts the year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450
    """
    return int(
        re.search(r"(\d)", morporkyear).group(0)
    )
```

---
layout: image-right
image: public/orang-utan-doctor.png
---

```sh {1|3-10|10-13}
python -m doctest code/chapter2/doctest_example.py

**************************************************
File ".../code/chapter2/doctest_example.py", 
    line 8,in doctest_example.extract_year
Failed example: extract_year("year 450 in the 3rd 
    month")
Expected: 450
Got: 4
**************************************************
1 items had failures:
   1 of 1 in doctest_example.extract_year
***Test Failed*** 1 failures.
```

---
layout: image-right
image: public/orang-utan-doctor.png
---

Long story short: lets fix it!

<hr> 

````md magic-move
```python
"""
Basically just saying that we expect at least one 
but arbitrary many numbers
"""
import re


def extract_year(morporkyear: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450
    """
    return int(
        re.search(r"(\d+)", morporkyear).group(0)
    )
```

```python
"""
Adding a few more "tests" & fixing the issues
"""
import re


def extract_year(morporkyear: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450

    >>> extract_year("year -450 in the 3rd month")
    -450

    >>> extract_year("year 0 in the 3rd month")
    0
    """
    return int(
        re.search(r"(-?\d+)", morporkyear).group(0)
    )
```
````

---

### 🕵️ Let's continue hiding the lost books

<hr> 

````md magic-move
```python
# ⬇️  Confident enough, that this works now
def extract_year(morpork_year: str) -> int: ...


def hide_lost_books(iterable: Iterable[Book]) -> Iterator[Book]:
    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
```

```python
"""
Use `yield from` to directly generate from this and unindent the code
Why?
-> Because it's lazy and bidirectional
-> Means: forwards "send" values correctly
-> Does not work in async code :(
"""
def extract_year(morporkyear: str) -> int: ...

def hide_lost_books(iterable: Iterable[Book]) -> Iterator[Book]:
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
-> Bad because global state can mess with us
"""
def extract_year(morporkyear: str) -> int: ...

lost_books = []

def hide_lost_books(
    iterable: Iterable[Book]
) -> Iterator[Book]:
    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)
```

```python
"""
Yield the lost books last?
-> ugly with return type
"""
def extract_year(morporkyear: str) -> int: ...


def hide_lost_books(
    iterable: Iterable[Book]
) -> Iterator[Book | None]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    yield None  # as a separator

    # The lost books
    yield from lost_books
```

```python
"""
Let's adapt our return type.

Instead of an singular Value Iterator we will return
a Generator
"""
def hide_lost_books(
    iterable: Iterable[Book]
) -> Generator[Book, None, list[Book]]:
    #     yield --^      | send ^ |   ^---- return type
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield book
        else:
            lost_books.append(book)

    yield None  # as a separator

    # The lost books
    yield from lost_books
```

```python
def hide_lost_books(
    iterable: Iterable[Book]
) -> Generator[Book, None, list[Book]]:
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
Usage
"""
def hide_lost_books(iterable: Iterable[Book]) -> \
    Generator[Book, None, list[Book]]: ...

def get_return_value() -> tuple[list[Book], list[Book]]:
    non_hidden_generator = hide_lost_books(mylibrary)

    # consume the whole generator (just as example)
    non_lost_books = list(non_hidden_generator)

    dropped_books = []
    try:
        next(non_hidden_generator)
    except StopIteration as e:
        dropped_books = e.value

    return non_lost_books, dropped_books
```
````

---
layout: center
---

### Summary

<hr> 

<v-clicks depth="2">

- Generators `yield` values
- Generators always also return a value inside `StopIteration` (default `None`)
- Is it a good idea?
    - No. Most likely not, as it is kind of suprising behaviour
- But why did we just see it?
    - Because sometimes in one-off scripts this is faster and easier than
      a sophisticated object containing the data solution
- What about the middle argument in `Generation[A, B, C]`?
    - Out of scope, but basically we can SEND stuff to generators after their creation
    - `gen = create_generator(); gen.send(123)`
    - Fetch with `received = yield anothervalue; received == 123`

</v-clicks>

--- 
layout: two-cols
---

### 🤓 But how would I do it?

<hr>

<v-clicks>

- We use an object to track the data.
    - `NamedTuple` to avoid ugly `result[0]` and `result[1]`
    - Better: `result.lost` and `result.current`
- relatively cheap: We only transport references
- just yield this container instead of complex surprising methods

</v-clicks>

::right::

```python {all|1-4|5-6|16|all}{at:1}
from typing import NamedTuple


class BookMeta(NamedTuple):
    current: Book
    lost: list[Book]


def hide_lost_books(
    iterable: Iterable[Book]
) -> Iterator[BookMeta]:
    lost_books = []

    for book in iterable:
        if extract_year(book["lent_since"]) >= -300:
            yield BookMeta(book, lost_books)
        else:
            lost_books.append(book)
```
