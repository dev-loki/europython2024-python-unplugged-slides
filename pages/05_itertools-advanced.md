# itertools: lets mine deeper

---
layout: center
---

## itertools.count/cycle/repeat

````md magic-move

```python
def request_get(url: str, offset: int = 0) -> dict:
    return {"url": url, "offset": offset, "data": []}
```

```python {5-6}
def request_get(url: str, offset: int = 0) -> dict:
    return {"url": url, "offset": offset, "data": []}


response = request_get("https://...")
print(response['data'])
```

```python {5-12|5,11|7,10}
def request_get(url: str, offset: int = 0) -> dict:
    return {"url": url, "offset": offset, "data": []}


response = request_get("https://...")

offset = 0
while data := response['data']:
    print(data)
    offset += 25
    response = request_get("https://...", offset)
```

```python {5-6,8,13-14}
def request_get(url: str, offset: int = 0) -> dict:
    return {"url": url, "offset": offset, "data": []}


url = "https://..."
page_size = 25

response = request_get(url)

offset = 0
while data := response['data']:
    print(data)
    offset += page_size
    response = request_get(url, offset)
```

```python {1,11-17|9-11|11-12|4-17}
from itertools import count


def request_get(url: str, offset: int = 0) -> dict:
    return {"url": url, "offset": offset, "data": []}


url = "https://..."
page_size = 25

for offset in count(start=0, step=page_size):
    response = request_get(url, offset)

    if not response['data']:
        break

    print(response['data'])
```

````

---
layout: center
---

### itertools.count

<v-clicks>

- is a generator (lazy evaluated)
- Counts to infinity like `enumerate`
- Allows steps like `range`
- signature: `count(start=0, step=5.1)`

</v-clicks>

---
layout: center
---

## itertools.islice

---
layout: center
---

## itertools.pairwise

---
layout: center
---

## itertools.starmap

---
layout: center
---

## itertools.singledispatch + variations

