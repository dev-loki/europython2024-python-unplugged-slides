import asyncio
from collections import deque
from collections.abc import AsyncIterator
from typing import AsyncGenerator, Any


async def atee[T](
    async_gen: AsyncGenerator[T, Any], n: int
) -> tuple[AsyncGenerator[T, None], ...]:
    queues = [asyncio.Queue() for _ in range(n)]
    # Deques to hold the references to the queues
    deques = [deque() for _ in range(n)]

    async def source():
        async for item in async_gen:
            for q in queues:
                await q.put(item)
        for q in queues:
            await q.put(None)  # Sentinel to indicate the end of the generator

    async def gen(q, dq):
        while True:
            if dq:
                yield dq.popleft()
            else:
                item = await q.get()
                if item is None:
                    break
                dq.append(item)
                yield dq.popleft()

    asyncio.create_task(source())

    return tuple(gen(q, dq) for q, dq in zip(queues, deques))


# Example usage
async def example_async_gen() -> AsyncGenerator[int, None]:
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i


async def main():
    async_gen = example_async_gen()
    tee_gens = await atee(async_gen, 2)

    async def print_gen(gen, name):
        async for item in gen:
            print(f"{name}: {item}")

    await asyncio.gather(print_gen(tee_gens[0], "gen1"), print_gen(tee_gens[1], "gen2"))


asyncio.run(main())
