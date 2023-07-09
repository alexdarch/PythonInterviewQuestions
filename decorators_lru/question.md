# Python Decorators

## Pop Quiz

1. Explain how a decorator works in python.
1. What is 'import time' and how does this relate to decorators in python?
1. What is the difference in behaviour between the two stacked decorators below?
1. What are function 'side effects'?

```python
@clock
@functools.lru_cache()
def my_func():
    pass

@functools.lru_cache()
@clock
def my_func():b
    pass
```

## Implementing an LRU decorator

Run `pytest decorators_lru` to run all of the tests
Run `python ./decorators_lru/run.py` to run a test script
Edit the solution.py file and run.py files only

### Problem statement

An LRU cache, meaning "least recently used" cache can be used on pure functions, without side effects, to store a mapping of inputs to calculated outputs. In order to not consume huge amounts of memory, only the last N input-output pairs are stored.

For this question, you must devise a way of implementing the lru cache. It will require both a dictionary and another data structure to store the ordering of the inputs. 

The N you should use for this question is 50.

You should also keep the name lru_cache for your data structure, otherwise the tests wont work. Additionally __contains__ and __len__ special methods are used in the tests to check that the cache is working correctly, don't change these.

In solution.py you should be presented with the code below (Note that @functools.wraps is there for general housekeeping of decorators and is good practice, you can effectively ignore this).

You job is the implement a simple version of python's `lru_cache` decorator. This decorator should take no arguments, unlike the standard library one (i.e. called with `lru_cache` rather than `lru_cache(arg1, arg2)`) and should be within at most 5x slower than the standard library function when running the tests. The model answer is 1.6x slower, whereas the baseline functions without this decorator will often be 1000s of times slower.

```python
import functools

def lru_cache(func):
    class LruCache:
        cache_length = 50

        def __init__(self):
            self.cache = {}
            # TODO: add your extra data structure
        
        def __contains__(self, item):
            return item in self.cache
        
        def __len__(self):
            return len(self.cache)

        # TODO: add extra functions/helper methods
        
    lru_cache = LruCache()
    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal lru_cache 

        # TODO: implement lru cache checking

    return inner
```

### Hints

1. A good naive implementation of this algorithm would store a hash of the inputs in a dictionary with the value being outputs and return these, however, this is not optimal as there is no record of which index to drop when you reach the Nth new input. You should attempt to implement this first, and then improve upon your answer.
1. Tuple's are hashable and can therefore be used as entries to the cacheing dictionary. You can get a tuple of kwargs using `tuple(sorted(kwargs.items()))`
1. The inner function should have minimal code, the majority of the logic should live in the LruCache class.
