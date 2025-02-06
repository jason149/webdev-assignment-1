#fib.py

import time
from functools import lru_cache

def timer(func):
    def wrapper(n):
        start = time.perf_counter()
        result = func(n)
        end = time.perf_counter()
        print(f"Finished in {end - start:.8f}s: f({n}) -> {result}")
        return result
    return wrapper


@lru_cache
@timer

def fib(n: int) -> int:

    arr = [0, 1, 1]

    for i in range(n - 2):
        arr.append(arr[-1] + arr[-2])

    return(arr[n])


if __name__ == "__main__":
    for i in range(101):
        fib(i)