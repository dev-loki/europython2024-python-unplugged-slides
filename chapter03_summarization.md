---
layout: center
---

# Chapter 3: Summarize and key data

<hr>

_Now the wonderful librarian wants us to get some data to get to know in which dimensions we're working here?_

---
layout: center
---

### Creating an Index

We want to have list of words in all the titles.

<hr>

<v-click>

Very simple example Example

- The: 123
- a: 42
- magician: 99

</v-click>

---

### Count Words

<hr>

````md magic-move
```python
def most_common_words_in_title(books: Iterable[Book]) -> dict:
    word_counter = {}
```

```python
def most_common_words_in_title(books: Iterable[Book]) -> dict:
    word_counter = {}

    for book in books:
        for word in book['title'].split():
            if word in word_counter:
                word_counter[word] += 1
```

```python
def most_common_words_in_title(books: Iterable[Book]) -> dict:
    """
    REPLACE
    """
    word_counter = {}

    for book in books:
        for word in book['title'].split():
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
```

```python
from collections import defaultdict


def most_common_words_in_title(books: Iterable[Book]) -> dict:
    """
    Import and use dictionary
    """
    word_counter = defaultdict(int)

    for book in books:
        for word in book['title'].split():
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
```

```python
from collections import defaultdict


def most_common_words_in_title(books: Iterable[Book]) -> dict:
    """
    Much more concise :)
    """
    word_counter = defaultdict(int)

    for book in books:
        for word in book['title'].split():
            word_counter[word] += 1
```

````

---
layout: center
---

_but now the librarian updated the assignment..._


<v-click>

_So glad customers always know what they want in the first iteration :)_

</v-click>

---
layout: center
---

````md magic-move
```python
from collections import defaultdict


def most_common_words_in_title(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    for book in books:
        for word in book['title'].split():
            word_counter[word] += 1
```

```python {4}
from collections import defaultdict


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    for book in books:
        for word in book['title'].split():
            word_counter[word] += 1
```

```python {7-13}
from collections import defaultdict


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    for book in books:
        for word in book['title'].split():
            word_counter[word] += 1
        for word in book['author'].split():
            word_counter[word] += 1
        for word in book['excerpt'].split():
            word_counter[word] += 1
```

```python {9-13|15-16}
from collections import defaultdict
from itertools import chain


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    for book in books:
        all_words = chain(
            book['title'].split(),
            book['author'].split(),
            book['excerpt'].split(),
        )

        for word in all_words:
            word_counter += 1
```

```python {8-15}
from collections import defaultdict
from itertools import chain


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    book_word_generator = (
        chain(
            book['title'].split(),
            book['author'].split(),
            book['excerpt'].split(),
        )
        for word in all_words
    )
```

```python {17}
from collections import defaultdict
from itertools import chain


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    book_word_generator = (
        chain(
            book['title'].split(),
            book['author'].split(),
            book['excerpt'].split(),
        )
        for word in all_words
    )

    word_generator = chain.from_iterable(book_word_generator)
```

```python {17-18}
from collections import defaultdict, Counter
from itertools import chain


def most_common_words_in_data(books: Iterable[Book]) -> dict:
    word_counter = defaultdict(int)

    book_word_generator = (
        chain(
            book['title'].split(),
            book['author'].split(),
            book['excerpt'].split(),
        )
        for word in all_words
    )

    word_generator = chain.from_iterable(book_word_generator)
    return Counter(word_generator)
```

````

---
layout: center
hideInToc: true
---

## Let's add some more data:

<br> <hr> <br>

<v-clicks>

 - min lent year (We all know this `min(x for x in thing)` - trivial)
 - max lent year (`max(x for x in thing)` - trivial)
 - family which lent the most (little bit more interesting)
 - largest book shelve in the library (let's see)

</v-clicks>

---
layout: center
---

````md magic-move
```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    books_by_family_name = {}

    for book in books:
        if not book['lent_by']:
            continue
```
```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    books_by_family_name = {}

    for book in books:
        if not book['lent_by']:
            continue

        names_split = book['lent_by'].split()
        family_name = names_split[1]
```
```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    books_by_family_name = {}

    for book in books:
        if not book['lent_by']:
            continue

        _, family = book['lent_by'].split(maxsplit=2)
```
```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    books_by_family = {}

    for book in books:
        if not book['lent_by']:
            continue

        _, family = book['lent_by'].split(maxsplit=2)
        if family not in books_by_family_name:
            books_by_family[family] = 1
        else:
            books_by_family[family] += 1
```
```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    books_by_family_name = {}

    for book in books:
        if not book['lent_by']:
            continue

        _, family = book['lent_by'].split(maxsplit=2)
        if family not in books_by_family:
            books_by_family[family] = 1
        else:
            books_by_family[family] += 1

    family = max(
        books_by_family.items(), 
        key=books_by_family.get,
    )
    return family, books_by_family[family]
```

```python
def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    """Again: defaultdict is a sensible choice"""
    books_by_family = defaultdict(int)

    for book in books:
        if not book['lent_by']:
            continue

        _, family = book['lent_by'].split(maxsplit=2)
        books_by_family[family] += 1

    family = max(
        books_by_family.items(), 
        key=books_by_family.get,
    )
    return family, books_by_family[family]
```
```python {12-16}
"""
Let's see how we could do it with groupby
"""
from itertools import groupby


def family_name(book: Book) -> str:
    """Let's create a functio for this"""
    return book['lent_by'].split()[1]


def family_lent_the_most(books: Iterable[Book]) -> tuple[str, int]:
    """... and check for the largest size"""
    lent_books = (b for b in books if b['lent_by'])
    books_by_family_name = groupby(lent_books, key=family_name)

    family = max(
        books_by_family_name,
        key=books_by_family_name.get,
    )

    return family, len(books_by_family_name[family])
```
```python {12-16}
from itertools import groupby


def family_name(book: Book) -> str:
    return book['lent_by'].split()[1]


class BiggestLender(NamedTuple):
    family: str
    lent_books: int


def family_lent_the_most(books: Iterable[Book]) -> BiggestLender:
    lent_books = (b for b in books if b['lent_by'])
    books_by_family_name = groupby(lent_books, key=family_name)
    
    family = max(
        books_by_family_name,
        key=books_by_family_name.get,
    )

    return BiggestLender(family, len(books_by_family_name['family']))
```
````

---
layout: center
---

## But the librarian changed requirements again... 

<br><hr><br>
:/ 

_"ookh! ookh! (I want youthe total lenders, unique family names and amount of unlent_books)_

---
layout: center
---

````md magic-move
```python
"""
Our 3 extractions methods:
"""
def total_unique_lenders(books: Iterable[Book]) -> int: ... 

def unique_families(books: Iterable[Book]) -> set[str]: ... 

def unlent_books_count(books: Iterable[Book]) -> int: ...
```
```python {10-13}
"""
And we have here the Statistics object:
- Again a Namedtuple, as it is nice to access and small in footprint
"""
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> set[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...


class Statistics(NamedTuple):
    unique_lenders: int
    families: set[str]
    unlent_books: int
```

```python {12-17}
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> set[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...


class Statistics(NamedTuple):
    unique_lenders: int
    families: list[str]
    unlent_books: int


def gather_statistics(books: Iterable[Book]) -> Statistics:
    """
    Let's naively just call those functions. Sequentially!
    -> What happens with the generator?
    """
    return Statistics(
        unique_lenders=total_unique_lenders(books),
        families=unique_families(books),
        unlent_books=unlent_books_count(books),
    )
```
```python {12-16}
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> set[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...


class Statistics(NamedTuple): ...


def gather_statistics(books: Iterable[Book]) -> Statistics:
    """This would solve that, right?"""
    all_books = list(books)

    return Statistics(
        unique_lenders=total_unique_lenders(all_books),
        families=unique_families(all_books),
        unlent_books=unlent_books_count(all_books),
    )
```
````

---
layout: image-right
image: reduced-tea.jpg
---

## Reduced Tee

<br> <hr> <br>

Two tools which might help us:

<v-clicks>

1. `itertools.reduce`
2. `itertools.tee`

</v-clicks>

<v-click>

<b>Let's start with reduce!</b>

</v-click>

---
layout: center
---

### Solving this with reduce

<hr>

````md magic-move
```python
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> list[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...

class Statistics(NamedTuple): ...


@dataclasses.dataclass(slots=True)
class StatisticsAccumulator:
    """
    First step: Adding some structure to accumulate our values
    Needs to be something mutable!
    """
    lenders: set[str] = set()
    families: set[str] = set()
    unlend: int = 0

def gather_statistics(books: Iterable[Book]) -> Statistics:
    all_books = list(books)

    return Statistics(
        unique_lenders=total_unique_lenders(all_books),
        families=unique_families(all_books),
        unlent_books=unlent_books_count(all_books),
    )
```
```python
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> list[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...

class Statistics(NamedTuple): ...

@dataclasses.dataclass
class StatisticsAccumulator:
    lenders: set[str] = set()
    families: set[str] = set()
    unlent: int = 0


def statistics_reducer(
    acc: StatisticsAccumulator,
    book: Book,
) -> StatisticsAccumulator:
    if book['lent_by']:
        acc.lenders.add(book['lent_by'])
        acc.families.add(family_name(book))
    else:
        acc.unlent += 1

    return acc

def gather_statistics(books: Iterable[Book]) -> Statistics:
    ...
```

```python
def total_unique_lenders(books: Iterable[Book]) -> int: ... 
def unique_families(books: Iterable[Book]) -> list[str]: ... 
def unlent_books_count(books: Iterable[Book]) -> int: ...

class Statistics(NamedTuple): ...

@dataclasses.dataclass
class StatisticsAccumulator: ...


def statistics_reducer(
    acc: StatisticsAccumulator,
    book: Book,
) -> StatisticsAccumulator: ...

def gather_statistics(books: Iterable[Book]) -> Statistics:
    accumulated_stats = reduce(statistics_reducer, books, StatisticsAccumulator())

    return Statistics(
        unique_lenders = len(accumulated_stats.lenders),
        families = len(accumulated_stats.families),
        unlent_books = accumulated_stats.unlent,
    )
```
````

---
layout: image-right
image: tee-tea-python.jpg
backgroundSize: contain
---

### How about tee?

<br><hr><br>

_Maybe our computation is not CPU bound, but IO bound?_

---
layout: image-right
image: tee-tea-python.jpg
backgroundSize: contain
---

<hr><br>

````md magic-move
```python {1-5|11-18}
"""
We still have these - will hide them completely in the next slide
"""
def unique_lenders(...): ...
def unique_families(...): ...
def unlent_books_count(...): ...
class Statistics(NamedTuple): ...


def gather_statistics(
    books: Iterable[Book]
) -> Statistics:
    """And we still call them one after another:"""
    all_books = list(books)

    return Statistics(
        unique_lenders=unique_lenders(all_books),
        families=unique_families(all_books),
        unlent_books=unlent_books_count(all_books),
    )
```
```python {1,2}
"""First step again: Importing"""
from itertools import tee


def gather_statistics(
    books: Iterable[Book]
) -> Statistics:
    all_books = list(books)

    return Statistics(
        unique_lenders=unique_lenders(all_books),
        families=unique_families(all_books),
        unlent_books=unlent_books_count(all_books),
    )
```
```python {9,10|9,10,13-16}
from itertools import tee


def gather_statistics(
    books: Iterable[Book]
) -> Statistics:
    all_books = list(books)

    """Now we create 3 "references" of the generator"""
    books_1, books_2, books_3 = tee(books, n=3)

    return Statistics(
        """And use those here"""
        unique_lenders=unique_lenders(books_1),
        families=unique_families(books_2),
        unlent_books=unlent_books_count(books_3),
    )
```
````

---
layout: image-right
image: tee-tea-python.jpg
backgroundSize: contain
---

### Tee caveats

<br><hr><br>

<v-clicks depth="2">

1. You don't want to consume the source generator
    - It will move forward without the `tees` to catch up!
2. `tee` is not thread safe: it might cause `RuntimeError` if used in a threading/async environment!
    - Not standard vanilla python, but for easy `async` and threading usage: `asyncstdlib`
    - I have a vanilla python implementation with `Queue` and `deque` in my repository
3. If the 3 generators advance in very different speed:
    - A lot of space is used to cache the values the other iterators did not get to (yet)
4. We could build our own threadsafe tee? -> code example using `queue.Queue` in the repository

</v-clicks>
