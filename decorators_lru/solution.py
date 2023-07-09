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