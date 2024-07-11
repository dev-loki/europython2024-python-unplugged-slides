---
layout: image
image: fetching-data.jpg
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


def fetch_book(url):
    return requests.get(url).json()


URL_BOOK = "http://localhost:1234/book"
print(fetch_book(URL_BOOK))
```
```python {1-3,5-6|1,2,4,5,10}
"""
Replace
- import with urllib Typical fetching with popular requests library.
- requests.get with urllib.urlopen.
"""
from urllib import request


def fetch_book(url):
    response = request.urlopen(url).read()


URL_BOOK = "http://localhost:1234/book"
print(fetch_book(URL_BOOK))
```

```python {1-3,5,8,10}
"""
But we now have to take care of json ourselves
"""
from urllib import request
import json


def fetch_book(url):
    response = request.urlopen(url).read()
    return json.loads(response)


URL_BOOK = "http://localhost:1234/book"
print(fetch_book(url))
```
```python
"""
An example response for our project
"""
def fetch_book(url): ...

fetch_book(URL_BOOK) == dict(
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
```python {2,3,7|4,5,7|10-19|22}
"""
With TypedDict from typing module we help the IDE
to give us proper type hints!
Positive Sideffect: This helps static code checkers help us
-> e.g. ruff,mypy,pyright,pyre,...
"""
from typing import TypedDict


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


def fetch_book() -> Book: ...
```
```python
"""
You can specify keys which might not be given
"""
from typing import TypedDict, NotRequired


class Book(TypedDict):
    title: str
    author: str
    lent_by: NotRequired[str]
    lent_since: NotRequired[str]
    lent_times: int
    year: str
    catalogued: str
    location: str
    excerpt: str
```
```python
"""
Or it might be useful to have it this way (not here though ;) )
"""
from typing import TypedDict, Required


class Book(TypedDict, total=False):
    title: Required[str] 
    author: Required[str]
    lent_by: str
    lent_since: str
    lent_times: Required[int]
    year: Required[str]
    catalogued: Required[str]
    location: Required[str]
    excerpt: Required[str]
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

## This is what it might like (Autocompletion <3)

<hr>

![](/01_editor_helpers.jpg)

<!--
This is an example from VIM, but works with all modern IDEs
-->

---
layout: image-left
image: orang-utan-library.jpg
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

</v-clicks>

<!--
THAT is the librarian of the Unseen University. He's nameless (if he had a name, he would be able to turn back human)
-->

---

## Batching

<hr> <br>

````md magic-move
```python {1-4|6-8|9-10|11-13|7,12,14}
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
```python {1-3,11|5-6,11|8,9,14|8,9,15-18}
"""
With islice this already gets better ...
... as we can even consume generators :)

Better as we now can even use generators with unknown size!
It is lazy as well and doesn't create huge list of tuples!

Iterable: Something with __next__ (no for x in collection)
Iterator: Something with __next__ and __iter__ (for x in collection)
"""
from itertools import islice


def batched(some_iterable: Iterable, size: int = 2) -> Iterator[tuple]:
    iterator = iter(some_iterable)
    
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
"""
Let's start using batched
- Imagine we enhanced our fetch_library 
  to actually stream the books from library
"""
def fetch_library() -> Iterable[Book]: ...

def work_on_the_library() -> None:
    lib = fetch_library()
```
```python
"""
Using the batched function:
- iterate through the library
- and let us work on 10 books at a time
"""
from itertools import batched


def fetch_library() -> Iterable[Book]: ...


def work_on_the_library() -> None:
    lib = fetch_library()

    for batch in batched(lib, 10):
        do_stuff_with_books(batch)
```
```python {1-4,9}
"""
We want to save the library so way have 
local data to work on!
"""
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")


def work_on_the_library() -> None:
    lib = fetch_library()

    for batch in batched(lib, 10):
        do_stuff_with_books(batch)
```
```python {5,14,15|7,8,14,15|15,16|17-18}
from csv import DictWriter
from itertools import batched


LIBRARY_DB = Path("library_raw.csv")

# fetches the keys form our TypedDict :)
BOOK_COLS = Book.__annotations.__.keys()


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
layout: center
---

## Summary

<br> <hr> <br> 

#### We started very small, but we might have learned something new

---
layout: center
---

### Trivial

<br> <hr> <br> 

Let's start with the stuff you likely already knew...

<v-clicks>

- csv (_"duh!"_)
- json (_"Yeah I knew that!"_)
- TypedDict with (Not)Required keys (Maybe new for a few?)
- All of those are in more detail in the /code folder inside the repository

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
- definetely worth a try, if you only have very few non-async requests

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
