"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from
this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""


class CacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # used for constant lookups
        self.cache_map = {}
        self.capacity = capacity
        self.oldest = CacheNode(-1, None)
        self.latest = CacheNode(-1, None)
        self.oldest.prev = self.latest
        self.latest.next = self.oldest

    def insert(self, new_node):
        # the new inserted node should become the latest used node
        temp = self.latest.next
        new_node.next = temp
        new_node.prev = self.latest
        self.latest.next = new_node
        temp.prev = new_node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache_map:
            found_node = self.cache_map[key]
            res = found_node.val
            del self.cache_map[key]

            # if the queried key is found, it should become the latest used position
            self.remove(found_node)
            self.insert(found_node)
            self.cache_map[key] = self.latest.next

            return res
        return -1

    def put(self, key: int, value: int) -> None:
        # if key is found, remove it
        if key in self.cache_map:
            found_key = self.cache_map[key]
            del self.cache_map[key]
            self.remove(found_key)

        # if capacity is maxed out, remove least used key
        if len(self.cache_map) >= self.capacity:
            del self.cache_map[self.oldest.prev.key]
            self.remove(self.oldest.prev)

        # insert key in the latest used position
        self.insert(CacheNode(key, value))
        self.cache_map[key] = self.latest.next
