---
layout: image
image: images/fetching-data.png
---

# Chapter 1: Fetching data

<style>
h1 {
    margin-top: 50% !important;
    font-weight: bolder;
    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
}
</style>

---

## Fetching data

<br> <hr> <br>

````md magic-move
```python
"""
Typical fetching with the popular requests library
"""
import requests


def fetch_book() -> dict:
    return requests.get(URL_BOOK).json()
```

```python {1-3,5-6|1,2,4,5,10}
"""
Replace
- import with urllib Typical fetching with popular requests library.
- requests.get with urllib.urlopen.
"""
from urllib import request


def fetch_book() -> dict:
    response = request.urlopen(URL_BOOK).read()
```

```python {1-3,5,8,10}
"""
We now have to take care of json ourselves
"""
from urllib import request
import json


def fetch_book() -> dict:
    response = request.urlopen(URL_BOOK).read()
    return json.loads(response)
```

```python
"""
An example response for our project
"""
def fetch_book() -> dict: ...

fetch_book() == dict(
  title="Remarkable Saga of the Clacks",
  author="Alexandra Scott",
  lent_by=null,
  lent_since=null,
  lent_times=8,
  year="The 7th year after Turtle Moves",
  catalogued="year -395 in the 2nd month",
  location="Great Hall: bottom shelve. 5m from the end",
  excerpt=(
      "Near the bubbling cauldron had never seen such a" 
      " sight: some dwarf miner raised the dead. The "
      "annual magical cooking competition begins."
  ),
)
```
````

<!--
- Most of us should already know requests or similar libraries (httpx?)
- replacing by urllib.request + json
- And this is what our server will return -> one example of a book
-->

---

## Working with data

<hr><br>

````md magic-move
```python
def fetch_book() -> dict:
    response = request.urlopen(URL_BOOK).read()
    return json.loads(response)


# This is what our data looks like
fetch_book() == dict(
  title="Remarkable Saga of the Clacks",
  author="Alexandra Scott",
  lent_by=null,
  lent_since=null,
  lent_times=8,
  year="The 7th year after Turtle Moves",
  catalogued="year -395 in the 2nd month",
  location="Great Hall: bottom shelve...",
  excerpt="Near the bubbling cauldron...",
)
```

```python
"""We can and should make our lives easier!"""
book_format = dict(
  title="Remarkable Saga of the Clacks",
  author="Alexandra Scott",
  lent_by=null,
  lent_since=null,
  lent_times=8,
  year="The 7th year after Turtle Moves",
  catalogued="year -395 in the 2nd month",
  location="Great Hall: bottom shelve...",
  excerpt="Near the bubbling cauldron...",
)


def fetch_book() -> dict: ...
```

```python
"""We can and should make our lives easier!"""
from typing import TypedDict


book_format = dict(
  title="Remarkable Saga of the Clacks",
  author="Alexandra Scott",
  lent_by=null,
  lent_since=null,
  lent_times=8,
  year="The 7th year after Turtle Moves",
  catalogued="year -395 in the 2nd month",
  location="Great Hall: bottom shelve...",
  excerpt="Near the bubbling cauldron...",
)


def fetch_book() -> dict: ...
```

```python
"""
With TypedDict from typing module we help the IDE
to give us proper type hints!
Positive Sideffect: This helps static code checkers help us
-> e.g. ruff,mypy,pyright,pyre,...
"""
from typing import TypedDict


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


def fetch_book() -> BookResponse: ...
```
````

<!--
Let's move the data on top, as we wanna work with it
TypedDict has numerous advantages over dict 

- typechecks (free automated tests) and better code completion by IDEs 
- this won't be a talk about typing python (ref to typing talk here!)
-->

---
layout: center
---

## This is what it looks like

<hr>

![](images/01_editor_helpers.png)

<!--
This is an example from VIM, but works with all modern IDEs
-->

---
layout: image-left
image: images/orang-utan-library.png
---

## Let's continue

<br>

<hr> 

<br>

<v-clicks>

- There are a LOT of books. And we only have limited ressources
- This means that we need to work on the books in batches
- Plenty of solutions!
- Let's first look on how we might have done it before python3.12
- And then how python3.12 makes our life easier :)

</v-clicks>

<!--
THAT is the librarian of the Unseen University. He's nameless (if he had a name, he would be able to turn back human)
-->

---

## Batching

<hr> <br>

````md magic-move
```python {1-4|6-8|9-10|11-13|8,15}
"""
Sometimes search engines bring one to this or similar
stackoverflow solutions¹
"""

def batched(some_list: list, size: int = 2) -> list[tuple]:
    batches = []

    for i in range(0, len(some_list), size):
        batch = some_list[i : i+size]
        if batch:
            batches.append(batch)

    return batches
```
```python {1-5|8|8-12|13|15-16|all}
"""
With islice this already gets better ...
... as we can even consume generators :)
"""
from itertools import islice


def batched(some_iterable: Iterable, size: int = 2) -> Iterator[tuple]:
    """
    Better as we now can even use generators with unknown size!
    It is lazy as well and doesn't create huge list of tuples!
    """
    iterator = iter(iterable)
    
    while batch := tuple(islice(iterator, size)):
        yield batch
```
```python
"""
But why reinvent the wheel? (In py3.12!)
"""
from itertools import batched
```
```python
def work_on_the_library() -> None:
    """
    Let's start using batched
    - Imagine we enhanced our fetch_library 
      to actually stream the books from library
    """
    lib = fetch_library()  # this is a generator of books!
```
```python {4-9|1|12,13}
from itertools import batched


def work_on_the_library() -> None:
    """
    Using the batched function:
     - iterate through the library
     - and let us work on 10 books at a time!
    """
    lib = fetch_library()

    for batch in batched(lib, 10):
        do_stuff_with_books(batch)
```
```python {5,9-12}
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")


def work_on_the_library() -> None:
    """
    We want to save the library so way have 
    local data to work on!
    """
    lib = fetch_library()

    for batch in batched(lib, 10):
        do_stuff_with_books(batch)
```
```python {5,14,15|7,8,14,15|15,16|17-18}
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")

# fetches the keys form our TypedDict :)
BOOK_COLS = BookResponse.__annotations.__.keys()


def work_on_the_library() -> None:
    lib = fetch_library()

    with LIBRARY_DB.open("w") as file:
        writer = DictWriter(file, fieldnames=BOOK_COLS)
        writer.writeheader()
        for batch in batched(lib, 10):
            writer.writerows(batch)
```
````

<small v-click.hide="5">

_one of many examples: [stackoverflow/312443](https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks)_

</small>

<!--
- typical batch function - seen it numerous times

- We now want to process duplicates
 
- only yield unique books

- as similar books are in similar parts of the library we can search in batches
-->

---
layout: two-cols
---

<br> <br> <br> <br> <br> <br> 

## Summary

<br> <br> 

### We started very small, but which modules did we learn about?

::right::

<br> <br> <br> <br> <br> <br> 

### Trivial

<br> <hr> <br> 

<v-clicks>

- csv (_"duh!"_)
- json (_"Yeah I knew that"_)
- TypedDict (Maybe new)

</v-clicks>

<!--
Let's be honest: These are the trivial modules you very likely already 
know
-->

---
layout: center
---

## urllib.requests

<br><hr><br>

<v-clicks>

- fetch and send data via HTTP(S)
- restricted to `GET`/`POST` (POST by setting the `data` parameter)
- not as bad to use as one might think,
  considering the vast amount of modules to replace it

</v-clicks>

<!--
as one might think due to all the alternatives

POST via setting data -> done
Query params via URL ;)
-->

---
layout: center
---

## itertools.islice

<br><hr><br>

<v-clicks depth="2">

- basically works like `mylist[from:to:steps]`
- but also works on Generators with unknown size :)
- cannot go backwards or use negative indizes:
    - works: `mylist[::-1]` (reversing a list)
    - doesn't work: `islice(mygenerator, start=-9, step=-3)`

</v-clicks>

---
layout: center
---

## itertools.batched

<br> <hr> <br>

<v-clicks>

- Finally arrived in `python3.12`
- Works on all kind of iterable stuff
- delivers `tuple[T]` of size `n`
- `list(batched(range(5), 3)) == [(0, 1, 2), (3, 4)]`

</v-clicks>
