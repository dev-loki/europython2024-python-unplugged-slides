---
layout: center
---

# itertools: the basics

---
layout: center
---

## itertools.chain + chain.from_iterable

````md magic-move

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
```

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

assert nested_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
import pandas as pd


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = pd.Series(nested_list).explode().tolist()

print(flattened_list)
```

```python
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = [item for sublist in nested_list for item in sublist]

print(flattened_list)
```

```python
from itertools import chain


nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = list(chain.from_iterable(nested_list))

print(flattened_list)
```

````

--- 
layout: center
---

## itertools.groupby

````md magic-move

```python
data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]
```

```python {9-14}
data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]

grouped_data = {}
for entry in data:
    category = entry['category']

    if category not in grouped_data:
        grouped_data[category] = []

    grouped_data[category].append(entry['item'])

print(grouped_data)
```

```python {12-14}
from collections import defaultdict


data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]

grouped_data = defaultdict(list)
for entry in data:
    grouped_data[entry['category']].append(entry['item'])

print(grouped_data)
```

```python
import itertools


data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]
```

```python {12-16}
import itertools


data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]

group_fun = lambda x: x['category']

# Group only works with subsequent keys
# -> Sorting mandatory
data.sort(key=group_fun)
grouped_data = itertools.groupby(data, key=group_fun)
```

```python {18-21}
import itertools


data = [
    {'category': 'fruit', 'item': 'apple'},
    {'category': 'vegetable', 'item': 'carrot'},
    {'category': 'fruit', 'item': 'banana'},
    {'category': 'vegetable', 'item': 'spinach'},
    {'category': 'fruit', 'item': 'cherry'}
]

group_fun = lambda x: x['category']

# We NEED sorting before that
data.sort(key=group_fun)
grouped_data = itertools.groupby(data, key=group_fun)

for group, objects in grouped_data:
    print(group, end=": ")
    for obj in objects:
        print(obj['item'], end=", ")
```

````

--- 
layout: center
---

## itertools.batched <3

````md magic-move

```python
logs = [
    "2023-01-01 10:00:00 ERROR Something went wrong",
    "2023-01-01 10:05:00 INFO User logged in",
    "2023-01-01 10:10:00 WARN Disk space low",
    "2023-01-01 10:15:00 ERROR Failed to save file",
    "2023-01-01 10:20:00 INFO File uploaded",
    "2023-01-01 10:25:00 WARN High memory usage",
    "2023-01-01 10:30:00 INFO User logged out",
    "2023-01-01 10:35:00 ERROR Database connection lost",
    "2023-01-01 10:40:00 INFO Backup completed",
    # ... far longer and each entry super detailed
]
```

```python {14|15|17-21|15}
logs = [
    "2023-01-01 10:00:00 ERROR Something went wrong",
    "2023-01-01 10:05:00 INFO User logged in",
    "2023-01-01 10:10:00 WARN Disk space low",
    "2023-01-01 10:15:00 ERROR Failed to save file",
    "2023-01-01 10:20:00 INFO File uploaded",
    "2023-01-01 10:25:00 WARN High memory usage",
    "2023-01-01 10:30:00 INFO User logged out",
    "2023-01-01 10:35:00 ERROR Database connection lost",
    "2023-01-01 10:40:00 INFO Backup completed",
]


BATCH_SIZE = 3
batches = [logs[i:i + BATCH_SIZE] for i in range(0, len(logs), BATCH_SIZE)]

for batch in batches:
    print("Processing batch:")
    for log in batch:
        print(log)
    print("Batch processed\n")
```

```python
batches = [
    logs[i:i + BATCH_SIZE]
    for i in range(0, len(logs), BATCH_SIZE)
]
```

```python {14-21|15}
from itertools import batched  # python3.12


logs = [
    "2023-01-01 10:00:00 ERROR Something went wrong",
    "2023-01-01 10:05:00 INFO User logged in",
    "2023-01-01 10:10:00 WARN Disk space low",
    "2023-01-01 10:15:00 ERROR Failed to save file",
    "2023-01-01 10:20:00 INFO File uploaded",
    "2023-01-01 10:25:00 WARN High memory usage",
    "2023-01-01 10:30:00 INFO User logged out",
    "2023-01-01 10:35:00 ERROR Database connection lost",
    "2023-01-01 10:40:00 INFO Backup completed",
]


BATCH_SIZE = 3

for batch in batched(logs, BATCH_SIZE):
    print("Processing batch:")
    for log in batch:
        print(log)
    print("Batch processed\n")
```

```python
from itertools import islice


def batched(iterable, n):
    it = iter(iterable)
    while True:
        batch = list(islice(it, n))
        if not batch:
            break
        yield batch            
```

```python
from typing import Iterator
from itertools import islice


def batched(iterable: Iterator, n: int) -> Iterator[list]:
    it = iter(iterable)
    while True:
        batch = list(islice(it, n))
        if not batch:
            break
        yield batch            
```

```python
from typing import TypeVar, Iterator
from itertools import islice


T = TypeVar('T')


def batched(iterable: Iterator[T], n: int) -> Iterator[list[T]]:
    it = iter(iterable)
    while True:
        batch = list(islice(it, n))
        if not batch:
            break
        yield batch            
```

````

---
layout: center
---

## itertools.islice

<v-clicks>

- Basically like slice <br>`my_list[a : b : c] == my_list[slice(start=a, step=b, stop=c)]`)
- But works for all `Iterables` as well <br> `Iterable`: supports `__iter__() -> Iterator`
- Doesn't support negative values though!

</v-clicks>
