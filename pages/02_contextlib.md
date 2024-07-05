---
layout: center
---

# contextlib

---
layout: center
---

## Bad

````md magic-move

```python
try:
    call_some_service_but_its_irrelevant_if_it_fails()
except:
    pass
```

```python
from contextlib import suppress


with suppress(HTTPError):
    call_some_service_but_its_irrelevant_if_it_fails()
```

````

---
layout: center
---


## contextlib.contextmanager

````md magic-move

```python
import os, uuid, contextlib
from contextlib import contextmanager


@contextmanager
def temp_file():
    file = open(f"{uuid.uuid4()}.tmp", "w")
    try:
        yield file
    finally:
        file.close()
        os.unlink(file.name)


with temp_file() as tmp:
    tmp.write(b"Temporary data")
    tmp.seek(0)
    print(tmp.read())
```

```python
from tempfile import NamedTemporaryFile


with NamedTemporaryFile() as tf:
    tf.write("Hello World")
    tf.seek(0)
    print(tf.read())
```

```python
from tempfile import NamedTemporaryFile


with NamedTemporaryFile(delete_on_close=False) as tf:
    tf.write("Hello World")
    tf.close()

    with open(tf, 'r') as f:
        print(f.read())
```

````

