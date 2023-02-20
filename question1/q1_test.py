import functions as f
import functools

# Another identical implementation without any decorators on it

def base_fibonacci(n):
    if n < 2:
        return n
    return base_fibonacci(n-2) + base_fibonacci(n-1)

@functools.lru_cache()
def fast_fibonacci(n):
    if n < 2:
        return n
    return base_fibonacci(n-2) + base_fibonacci(n-1)

def test_baseline(benchmark):
    func = lambda : base_fibonacci(20)
    result = benchmark(func)
    assert result == 6765

def test_optimal(benchmark):
    func = lambda : fast_fibonacci(20)  # using the functools.lru_cache decorator without the @ syntax sugar
    result = benchmark(func)
    assert result == 6765

# This is the only test you can change. Try to get it as close to test_optimal as possible
def test_lru(benchmark):
    func = lambda : f.fibonacci(20)
    result = benchmark(func)
    assert result == 6765