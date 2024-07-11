from itertools import chain


my_list = [
    [1, 2, 3],
    [3, 5, 7],
]
print(f"{my_list=}")

# Will result in a generator ...
flattened = chain.from_iterable(my_list)
print(f"{flattened=}")

# So we might want to consume it
flattened_list = list(flattened)
print(f"{flattened_list=}")

# Output:
# my_list=[[1, 2, 3], [3, 5, 7]]
# flattened=<itertools.chain object at 0x71340c502980>
# flattened_list=[1, 2, 3, 3, 5, 7]
