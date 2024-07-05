---
layout: center
---

# First little helpers

---
layout: center
---

# Non-dev related

```sh
python -m http.server
```

- Actual usable small http server
- Great for just sharing files
- Can also be used for local hosting for SPA (no HMR though)

---
layout: center
---

# Useful Containers

We'll use some containers which have advantages over "normal"
  dict and lists/tuples

<Toc mode="onlyCurrentTree" />

---
layout: center
---

## typing.TypedDict

<<< @/snippets/example_typing_typeddict.py {4-7|10-13|all}

Especially useful for WebResponses and Editor completions.

---
layout: center
---

## typing.NamedTuple

````md magic-move

```python
# Bad
people = [("Alice", 34), ("Bob", 31)]

# Usage
old_enough = [p for p in people if p[1] >= 18]
```

```python
from collections import namedtuple

# Better
Person = namedtuple("Person", ("name", "age"))

people = [Person("Alice", 34), Person("Bob", 17)]

old_enough = [p for p in people if p.age >= 18]
```

```python
from typing import NamedTuple

# Good
class Person(NamedTuple):
    name: str
    age: float

people = [Person("Alice", 34), Person("Bob", 17)]

# Usage
old_enough = [p for p in people if p.age >= 18]
```

```python
from typing import NamedTuple

# Good
class Person(NamedTuple):
    name: str
    age: float

people = [Person("Alice", 34), Person("Bob", 17)]

# Still works
old_enough = [p for p in people if p[1] >= 18]
```

````

