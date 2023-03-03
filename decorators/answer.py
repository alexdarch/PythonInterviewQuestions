import functools

def lru_cache(func):
    class Node:
        def __init__(self, key, value):
            self.prev = None
            self.next = None
            self.key = key
            self.value = value
        def __repr__(self):
            return f"[{self.key}, {self.value}]"
    

    class LruCache:
        cache_length = 50

        def __init__(self):
            self.head = Node(None, None) # The head of the list represents the most recently used value, the tail is the least recently used
            self.tail = Node(None, None)
            self.head.prev = self.tail
            self.tail.next = self.head

            self.cache = {} # mapping of keys to nodes

        def __getitem__(self, item):
            return self.cache[item].value
        
        def __contains__(self, item):
            return item in self.cache
        
        def __len__(self):
            return len(self.cache)

        def move_to_head(self, key):
            node = self.cache[key]
            node.prev.next, node.next.prev = node.next, node.prev # connect the two surrounding nodes
            self.insert_at_head(node.key, node.value)

        def insert_at_head(self, key, ans):
            # insert into linked list
            node = self.cache[key] if key in self.cache else Node(key, ans)
            second_head = self.head.prev
            second_head.next = node
            node.prev = second_head
            node.next = self.head
            self.head.prev = node

            # insert into dict
            self.cache[key] = lru_cache.head.prev
            if len(self.cache) > self.cache_length:
                self.delete_least_recently_used()

        def delete_least_recently_used(self):

            to_remove = self.tail.next
            self.tail.next = to_remove.next
            to_remove.next.prev = self.tail
            key = to_remove.key
            del self.cache[key]
            del to_remove

        def __repr__(self):
            x = self.tail.next
            nodes = []
            while x.value is not None:
                nodes.append([x.key, x.value])
                x = x.next
            return ', '.join(str(x) for x in nodes)
        
    lru_cache = LruCache()
    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal lru_cache

        key = args + tuple(sorted(kwargs.items()))

        if key in lru_cache:
            lru_cache.move_to_head(key)
            return lru_cache[key]

        # Otherwise see if we can add it to the cache/queue
        ans = func(*args, **kwargs)
        lru_cache.insert_at_head(key, ans)
        return ans

    return inner