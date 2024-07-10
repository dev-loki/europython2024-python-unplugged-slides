# are only generated when requested
from itertools import batched


first_hundred = range(1, 101)

# doesn't do any work yet
triples = batched(first_hundred, 3)

# consumes the batched generator, as
# well as the first_hundred generator!
print("Triples one after another")
for triple in triples:
    print(triple)

# Instead we could do this:
all_triples = list(triples)
print(f"\nThis is an empty list:\n{all_triples=}")
# (but here triples is already consumed!)

# What we could do:
all_triples = list(batched(range(1, 101), 3))
print(f"\nNow they are here again:\n{all_triples=}")
