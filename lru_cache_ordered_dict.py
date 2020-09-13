from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key) -> int:
        if key not  in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


cache = LRUCache(2)
print(cache.cache)
cache.put('A', 1)
print(cache.cache)
cache.put('B', 2)
print(cache.cache)
cache.get('A')
cache.put('C', 3)
print(cache.cache)
cache.get('C')
print(cache.cache)
cache.put('D', 4)
print(cache.cache)
cache.get('A')
print(cache.cache)
cache.put('E', 5)



