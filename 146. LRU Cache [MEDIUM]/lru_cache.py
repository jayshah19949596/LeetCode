class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.nxt = self.latest
        self.latest.prv = self.oldest
        
    def insert(self, node):
        prv_node, nxt_node = self.latest.prv, self.latest
        prv_node.nxt = nxt_node.prv = node
        node.nxt = nxt_node
        node.prv = prv_node

    def remove(self, node):
        prv_node, nxt_node = node.prv, node.nxt
        prv_node.nxt = nxt_node
        nxt_node.prv = prv_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru_node = self.oldest.nxt
            self.remove(lru_node)
            del self.cache[lru_node.key]
