---
layout: center
---

# Miscellaneous

<br> <hr> <br>

_(We might not get to this, due to time restrictions)_

---

## Mixin for ordering objects

<br> <hr> <br>

<v-clicks>

- Imagine we have our own object containing data we need
- It should be sortable (e.g. the books by year!)
- But taking care of all the magic dunder methods is annoying:<br>
  `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`

</v-clicks>

---

## Order objects

<br><hr><br>

````md magic-move
```python
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year
```
```python
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __lt__(self, other: 'Book') -> bool:
        # Can also be __le__
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year < other_year
```
```python
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __lt__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year < other_year

    def __eq__(self, other: 'Book') -> bool:
        # Good to have, but not necessary
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year == other_year

```
```python
from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __lt__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year < other_year

    def __eq__(self, other: 'Book') -> bool:
        # Good to have, but not necessary
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year == other_year
```
````

---

# with suppress

<br> <hr> <br>

````md magic-move
```python
def ignore_failing_call():
    try:
        might_fail_but_I_dont_care()
    except RuntimeError as err:
        """We don't care about failing"""
        pass
```
```python
import contextlib


def ignore_failing_call():
    try:
        might_fail_but_I_dont_care()
    except RuntimeError as err:
        """We don't care about failing"""
        pass
```
```python
import contextlib


def ignore_failing_call():
    with contextlib.suppress(RuntimeError):
        """We still don't care about failing"""
        might_fail_but_I_dont_care()
```
````

---

# The "server"

<br><hr><br>

<v-clicks depth="2">

- I actually wrote a whole server to generate random
  books, just to drop the usage due to time limitations
- But still: We can look into some of the last "batteries included"
  1. A pure python server (means: very simple and unmighty Flask/FastAPI)
  2. Argument parsing (not as beautiful as typer, but easy to work with)
  3. partials of functions/methods (basically lambdas in pythonic)
  4. Caching

</v-clicks>
