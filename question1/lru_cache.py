import functools

def lru_cache(func):
    class Node:
        def __init__(self, value):
            self.prev = None
            self.next = None
            self.value = value
        def __repr__(self):
            return self.value

    class DoublyLinkedList:
        def __init__(self):
            self.head = Node(None) # The head of the list represents the most recently used value, the tail is the least recently used
            self.tail = Node(None)
            self.head.prev = self.tail
            self.tail.next = self.head
            self.length = 0

        def move_to_head(self, node):
            node.prev.next, node.next.prev = node.next, node.prev # connect the two surrounding nodes
            self.insert_at_head(node)

        def insert_at_head(self, node):
            second_head = self.head.prev

            second_head.next = node
            node.prev = second_head
            node.next = self.head
            self.head.prev = node

            self.length += 1
            if self.length >= 128:
                to_remove = self.tail.next
                self.tail.next = to_remove.next
                to_remove.next.prev = self.tail
                del to_remove

        def __repr__(self):
            x = self.tail.next
            nodes = []
            while x.value is not None:
                nodes.append(x.value)
            return ', '.join(nodes)
            
    cache = dict()
    lst = DoublyLinkedList()

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal cache, lst

        key = args + tuple(sorted(kwargs.items()))

        if key in cache:
            (ans, node) = cache[key]
            lst.move_to_head(node)
            return ans

        # Otherwise see if we can add it to the cache/queue
        ans = func(*args, **kwargs)
        lst.insert_at_head(Node(ans))
        cache[key] = (ans, lst.head.prev)
        return ans

    return inner