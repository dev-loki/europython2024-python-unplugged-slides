import operator, typing


class Person(typing.NamedTuple):
    # alt: collections.namedtuple("NAME", "name1,name2")
    name: str
    age: int


data = [
    Person("Jeanne", 25),
    Person("Jane", 22),
    Person("Dave", 30),
]

sorted_lambda = sorted(data, key=lambda x: x.age)

sorted_itemgetter = sorted(data, key=operator.itemgetter("age"))

# notes: namedtuple vs dataclass: namedtuples are smaller
# & faster especially for large numbers of values
