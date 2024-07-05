import time
import threading
from queue import Queue
from typing import Iterable, Tuple, TypeVar

T = TypeVar("T")


def threadsafe_tee(iterable: Iterable[T], n: int = 2) -> Tuple[Iterable[T], ...]:
    """
    Return n independent threadsafe iterators from a single iterable.
    """
    # one queue per "n"
    queues = tuple(Queue() for _ in range(n))

    # Sentinel object to signal the end of the iterator
    sentinel = object()

    def feed_queues() -> None:
        for item in iterable:
            for q in queues:
                q.put(item)

        for q in queues:
            q.put(sentinel)

    def generator(my_queue):
        while True:
            item = my_queue.get()
            if item is sentinel:
                # quite busy this waiting...
                break

            yield item

    threading.Thread(target=feed_queues, daemon=True).start()
    return tuple(generator(q) for q in queues)


def example_usage() -> None:
    def slow_range(n):
        for i in range(n):
            time.sleep(0.1)
            yield i

    # Create two threadsafe iterators
    it1, it2 = threadsafe_tee(slow_range(5))

    # Use the iterators in different threads
    def consume(it, name):
        for item in it:
            print(f"{name}: {item}")

    t1 = threading.Thread(target=consume, args=(it1, "Thread 1"))
    t2 = threading.Thread(target=consume, args=(it2, "Thread 2"))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    example_usage()
