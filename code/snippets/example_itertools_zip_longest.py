import itertools


def round_robin(*generators):
    # Use itertools.zip_longest to combine the generators
    # Fill value with None to handle different lengths
    for values in itertools.zip_longest(*generators, fillvalue=None):
        for value in values:
            if value is not None:
                yield value


# Example usage:
def gen(lst):
    for item in lst:
        yield item


A = gen([1, 2])
B = gen([3])
C = gen([4, 5, 6])
D = gen([7, 8, 9])
E = gen([10, 11, 12, 13])
F = gen([14, 15])

combined_generator = round_robin(A, B, C, D, E, F)

# Print elements from the combined generator
for item in combined_generator:
    print(item)
