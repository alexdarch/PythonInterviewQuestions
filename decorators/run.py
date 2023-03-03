import answer as a

@a.lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(5))
