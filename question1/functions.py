import lru_cache

@lru_cache.lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)