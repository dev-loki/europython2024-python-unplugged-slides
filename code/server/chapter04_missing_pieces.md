---
layout: center
---

# Some missing pieces out of context

---
layout: center
---

# Very simple iterators

---
layout: center
---

````md magic-move

```python
from itertools import count


endless_numbers = (c for c in count(start=42, step=13))

for number in islice(endless_numbers, stop=999):
    print(number)
```

```python {4-5}
from itertools import cycle


people = ("Alice", "Bob", "...")
decision_gen = cycle(("Yes", "No"))









```

```python {7-11}
from itertools import cycle


people = ("Alice", "Bob", "...")
decision_gen = cycle(("Yes", "No"))

bouncer_queue = (
    name
    for name, decision in zip(people, decision_gen)
    if decision == "Yes"
)



```

```python {13-14}
from itertools import cycle


people = ("Alice", "Bob", "...")
decision_gen = cycle(("Yes", "No"))

bouncer_queue = (
    name
    for name, decision in zip(people, decision_gen)
    if decision == "Yes"
)

for persson in bouncer_queue:
    print("Come in, have fun!")
```

```python {1,5}
from itertools import repeat


people = ("Alice", "Bob", "...")
decision_gen = reapeat("Yes")

bouncer_queue = (
    name
    for name, decision in zip(people, decision_gen)
    if decision == "Yes"
)

for persson in bouncer_queue:
    print("Come in, have fun!")
```

````

---
layout: center
---

In this case ending the `zip` whenever there are no more `people`
is fine, <v-click>but sometimes we do not want to end at the shortest iterator,
but for the longest.</v-click>

````md magic-move

```python



telescopes = ["Hubble", "James Webb", "Keck"]
celestial_objects = ["Mars", "Andromeda Galaxy", "Betelgeuse", "Crab Nebula"]










```

```python {1,7}
from itertools import zip_longest


telescopes = ["Hubble", "James Webb", "Keck"]
celestial_objects = ["Mars", "Andromeda Galaxy", "Betelgeuse", "Crab Nebula"]

print("Tonight's Observation Schedule:")








```

```python {8-9}
from itertools import zip_longest


telescopes = ["Hubble", "James Webb", "Keck"]
celestial_objects = ["Mars", "Andromeda Galaxy", "Betelgeuse", "Crab Nebula"]

print("Tonight's Observation Schedule:")
for telescope, target in zip_longest(telescopes, celestial_objects, fillvalue=None):
    print(f"{telescope} will be observing {target}.")






```

```python {8-12}
from itertools import zip_longest


telescopes = ["Hubble", "James Webb", "Keck"]
celestial_objects = ["Mars", "Andromeda Galaxy", "Betelgeuse", "Crab Nebula"]

print("Tonight's Observation Schedule:")
for telescope, target in zip_longest(telescopes, celestial_objects, fillvalue=None):
    if target:
        print(f"{telescope} will be observing {target}.")
    else:
        print(f"No telescope available for {target}. Maybe next time!")



```

```python {9-15}
from itertools import zip_longest


telescopes = ["Hubble", "James Webb", "Keck"]
celestial_objects = ["Mars", "Andromeda Galaxy", "Betelgeuse", "Crab Nebula"]

print("Tonight's Observation Schedule:")
for telescope, target in zip_longest(telescopes, celestial_objects, fillvalue=None):
    match telescope, target:
        case None, _:
            print(f"No telescope available for {target}. Maybe next time!")
        case _, None:
            print(f"{telescope} is taking a break tonight.")
        case telescope, target:
            print(f"{telescope} will be observing {target}.")
```

````

---
layout: center
---

# Radioactive "Pythonium"

````md magic-move

```python 



INITIAL_AMOUNT = 1000
DECAY_RATE = 0.9
TIME_STEPS = 20












```

```python {1,9,10}
from itertools import accumulate, repeat


INITIAL_AMOUNT = 1000
DECAY_RATE = 0.9
TIME_STEPS = 20


def decay(amount: float, _) -> float:
    return amount * DECAY_RATE








```

```python {9,10,13}
from itertools import accumulate, repeat


INITIAL_AMOUNT = 1000
DECAY_RATE = 0.9
TIME_STEPS = 20


def decay(amount: float, _) -> float:
    return amount * DECAY_RATE


decay_sequence = accumulate(repeat(INITIAL_AMOUNT, TIME_STEPS), decay)





```

```python {13,15-18|all}
from itertools import accumulate, repeat


INITIAL_AMOUNT = 1000
DECAY_RATE = 0.9
TIME_STEPS = 20


def decay(amount: float, _) -> float:
    return amount * DECAY_RATE


decay_sequence = accumulate(repeat(INITIAL_AMOUNT, TIME_STEPS), decay)

print(
    "Radioactive decay over time steps:", 
    "\n - ".join(map(str, decay_sequence))
)
```

````

---
layout: center
---

# combination of large libraries

<v-clicks>

- Let's imagine, that we get multiple large library sets and want to search them by order
- Most important: **the desk at the entrance - the most commonly searched books**
- Second: The local library
- Third: The aethers library

</v-clicks>

---
layout: center
---

````md magic-move

```python
entrance_index = dict(...)
local_index = dict(...)
aether_index = dict(...)
```

```python
entrance_index = dict(
    "Some Author": [Book,...],
    "Some title": [Book, ...],
    ...
)
local_index = dict(...)
aether_index = dict(...)
```

```python
entrance_index = dict(...)
local_index = dict(...)
aether_index = dict(...)
```

```python
from collections import ChainMap


entrance_index = dict(...)
local_index = dict(...)
aether_index = dict(...)


search_lib_db = ChainMap(entrance_index, local_library, aether_index)
```

```python
from collections import ChainMap


entrance_index = dict(...)
local_index = dict(...)
aether_index = dict(...)


search_lib_db = ChainMap(entrance_index, local_index, aether_index)

customer_request = "Umph McNeil"
if found_book := seach_lib_db.get(customer_request):
    print("Oooomph. *giving book to customer*")
else:
    print("Oomph! *orang utan shrugging*")
```

````
