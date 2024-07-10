---
layout: center
---

# Miscellaneous

<br> <hr> <br>

_(this might not make it, due to time restrictions)_

---

## Mixin for ordering objects

<br> <hr> <br>

<v-clicks>

- Imagine we have our own object containing data we need
- It should be sortable (e.g. the books by year!)
- But taking care of all the magic dunder methods:
  `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`

</v-clicks>

---
layout: two-cols
hideIntoc: true
---

## Order objects

<br> <br>

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

    def __eq__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year == other_year
```
```python
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __eq__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year == other_year

    def __lt__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year < other_year
```
```python
from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __eq__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year == other_year

    def __lt__(self, other: 'Book') -> bool:
        own_year = extract_year(self.year)
        other_year = extract_year(other.year)
        return own_year < other_year
```
````

::right::

<v-clicks at=1>

- Add `__eq__` to check if the object is considered equal
- Add `__lt__` to check if it is true lower (not equal)
- Add `total_ordering` to just fill the other dunder_methods:
  - `__le__`
  - `__ge__`
  - `__gt__`
- Obviously we should cache the calculation ;)

</v-clicks>

---

# The "server"

<br><hr><br>

<v-clicks depth="2">

- I actually wrote a whole server to generate random
  books, just to drop the usage due to time limitations
- But still: We can look into some of the last "batteries included"
  1. A pure python server (means: very simple and unmighty Flask/FastAPI)
  2. Argument parsing (not as beautiful as typer, but easy to work with)
  3. Caching
  4. suppressing errors the right way!
  5. partials of functions/methods (basically lambdas in pythonic)

</v-clicks>
