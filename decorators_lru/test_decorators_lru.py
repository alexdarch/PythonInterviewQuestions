import functools
import solution as s
import os
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@s.lru_cache
def lru_fibonacci(n):
    return fibonacci(n)

@functools.lru_cache()
def functools_fibonacci(n):
    return fibonacci(n)

########################################### Benchmark tests ##########################################
def test_baseline(benchmark):
    print(os.environ['TEST'])
    func = lambda : fibonacci(20)
    result = benchmark(func)
    assert result == 6765

def test_functools(benchmark):
    func = lambda : functools_fibonacci(20)
    result = benchmark(func)
    assert result == 6765

def test_lru(benchmark):
    func = lambda : lru_fibonacci(20)
    result = benchmark(func)
    assert result == 6765

########################################### Functionality tests #############################################

def test_correctness():
    
    assert lru_fibonacci(5) == 5
    assert lru_fibonacci(10) == 55
    assert lru_fibonacci(15) == 610
    
def test_multi_arguments():
    # Test with multiple arguments and keyword arguments
    @s.lru_cache
    def add(a, b, c=None):
        return a + b + (c or 0)
    
    assert add(1, 2) == 3
    assert add(2, 3, 4) == 9
    assert add(1, 2, c=3) == 6

def test_caching():

    @s.lru_cache
    def square(a):
        return a * a
    
    for i in range(75):
        square(i) # This should add 50 items to the cache

    cache_idx = square.__code__.co_freevars.index('lru_cache')
    lru_cache = square.__closure__[cache_idx].cell_contents
    
    for i in range(0, 25):
        assert (i, ) not in lru_cache
    for i in range(25, 75):
        assert (i,) in lru_cache
    assert len(lru_cache) == 50
