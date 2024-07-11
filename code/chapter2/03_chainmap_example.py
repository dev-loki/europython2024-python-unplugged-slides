from pprint import pprint
from collections import ChainMap
from typing import Any


# This Mapping object might be even fetched from
# oversees on the fly!
global_config = {
    "g_some_key": "asdf",
    "g_different": "xxx",
    "g_answer_to_life_aso": 42,
}

local_config = {
    "l_name": "Experiment A",
    "g_answer_to_life_aso": "fourty_two",
}

specific_config = {
    "s_args": (1, 2, 3, 4),
}

# Imagine all those configs ARE Huge. Or some kind of gigantic
# lookup table

# This will result in a new config - even larger!
combined_dict = global_config | local_config | specific_config

print("combined_dict")
pprint(combined_dict)

combined_chainmap: ChainMap[str, Any] = ChainMap(
    specific_config, local_config, global_config
)

print("\ncombined_chainmap")
pprint(combined_chainmap)

print("\ncombined_chainmap['g_answer_to_life_aso']")
pprint(combined_chainmap["g_answer_to_life_aso"])

print("\ncombined_chainmap['s_args']")
pprint(combined_chainmap["s_args"])

print("\ncombined_chainmap['g_some_key']")
pprint(combined_chainmap["g_some_key"])
