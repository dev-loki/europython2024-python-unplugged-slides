import collections, random, string

number_list = random.choices(string.ascii_lowercase, k=20)

# Really Bad
counter: dict[str, int] = {}
for n in number_list:
    if n in counter:
        counter[n] += 1
    else:
        counter[n] = 1


# Bad
counter = collections.defaultdict(int)
for n in number_list:
    counter[n] += 1
print(f"{counter["a"]=}\n{sum(counter.values())=}")


# Better
counter = collections.Counter(number_list)
print(f"{counter["a"]=}\n{sum(counter.values())=}")
