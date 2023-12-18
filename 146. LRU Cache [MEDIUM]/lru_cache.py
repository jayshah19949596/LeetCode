class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class DLL(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_node_at_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev.next = node

    def update_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert_node_at_tail(node)

    def remove_node_at_head(self):
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        removed_key = node.key
        del node
        return removed_key


class LRUCache(object):
    def __init__(self, capacity):
        self.mapping = {}
        self.capacity = capacity
        self.dll = DLL()

    def get(self, key):
        if key not in self.mapping:
            return -1
        self.dll.update_node(self.mapping[key])
        return self.mapping[key].val

    def put(self, key, value):
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self.mapping[key] = node
            self.dll.update_node(self.mapping[key])
        else:
            if len(self.mapping) == self.capacity:
                removed_key = self.dll.remove_node_at_head()
                del self.mapping[removed_key]
            self.mapping[key] = Node(key, value)
            self.dll.insert_node_at_tail(self.mapping[key])
