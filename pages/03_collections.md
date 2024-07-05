---
layout: center
---

# collections

---
layout: center
---

## collections.Counter

````md magic-move

```python
from random import randint


numbers = [random(0, 10) for _ in range(100)]

count_dict = {}
for n in numbers:
    if n in count_dict:
        count_dict[n] += 1
    else:
        count_dict[n] = 1
```

```python
from random import randint
from collections import defaultdict


numbers = [random(0, 10) for _ in range(100)]

count_dict = defaultdict(int)
for n in numbers:
    count_dict[n] += 1
```

```python
from random import randint


numbers = [random(0, 10) for _ in range(100)]

count_dict = Counter(numbers)
```

````

---
layout: center
---

## collections.ChainMap


````md magic-move

```python
default_config = {'theme': 'light', 'show_sidebar': True}
user_config = {'theme': 'dark'}
environment_config = {'show_sidebar': False, 'debug': True}
```

```python
import pandas as pd


default_config = {'theme': 'light', 'show_sidebar': True}
user_config = {'theme': 'dark'}
environment_config = {'show_sidebar': False, 'debug': True}

# Conversion to DataFrames
default_df = pd.DataFrame([default_config])
user_df = pd.DataFrame([user_config])
environment_df = pd.DataFrame([environment_config])

combined_df = pd.concat([default_df, user_df, environment_df], ignore_index=True).ffill().iloc[-1]
```

```python
import pandas as pd


default_config = {'theme': 'light', 'show_sidebar': True}
user_config = {'theme': 'dark'}
environment_config = {'show_sidebar': False, 'debug': True}

# Conversion to DataFrames
default_df = pd.DataFrame([default_config])
user_df = pd.DataFrame([user_config])
environment_df = pd.DataFrame([environment_config])

combined_df = pd.concat([default_df, user_df, environment_df], ignore_index=True).ffill().iloc[-1]

config = combined_df.to_dict()

print(config)
```

```python
default_config = {'theme': 'light', 'show_sidebar': True}
user_config = {'theme': 'dark'}
environment_config = {'show_sidebar': False, 'debug': True}

config = default_config | user_config | environment_config

print(config)
```

```python
from collections import ChainMap


default_config = {'theme': 'light', 'show_sidebar': True}
user_config = {'theme': 'dark'}
environment_config = {'show_sidebar': False, 'debug': True}

config = ChainMap(environment_config, user_config, default_config)

print(dict(config))
```

````


