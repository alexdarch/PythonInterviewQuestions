# Implementing an LRU cache

1. Explain how a decorator works in python.
1. What is 'import time' and how does this relate to decorators in python?
1. What is the difference in behaviour between the two stacked decorators below?
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
1. Can you explain what an lru_cache is and how it works in general (this is not a language specific concept)?
1. Fill in the implementation details of lru_cache.py


Run `pytest` to run all of the tests
Run `python q1_run.py` to run a test script

