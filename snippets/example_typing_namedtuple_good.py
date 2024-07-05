from typing import NamedTuple


# Good
class Person(NamedTuple):
    name: str
    age: float


people = [Person("Alice", 34), Person("Bob", 17)]


# Usage
old_enough = [p for p in people if p.age >= 18]

# still works
old_enough = [p for p in people if p[1] >= 18]
