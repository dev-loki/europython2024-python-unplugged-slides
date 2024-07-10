def batched(some_list: list, size: int = 2) -> list[tuple]:
    batches = []

    for i in range(0, len(some_list), size):
        batch = some_list[i : i + size]
        if batch:
            batches.append(batch)

    return batches
