from collections import namedtuple


# Better
Person = namedtuple("Person", ("name", "age"))


people = [Person("Alice", 34), Person("Bob", 17)]


# Usage
old_enough = [p for p in people if p.age >= 18]

# still works
old_enough = [p for p in people if p[1] >= 18]
