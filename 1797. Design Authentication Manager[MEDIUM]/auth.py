# ====================================================================
# Solution 1: Sub-Optimized countUnexpiredTokens with only HashMap
# ====================================================================

"""
countUnexpiredTokens:
   Time: O(n)
   Amortized Time: O(n)
   Space: O(n)
"""
from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token_to_ttl = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_to_ttl[tokenId] = currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_to_ttl and self.token_to_ttl[tokenId] > currentTime:
            self.token_to_ttl[tokenId] = currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        token_to_del, unexpired_count = [], 0
        for token in self.token_to_ttl:
            if self.token_to_ttl[token] <= currentTime:
                token_to_del.append(token)
                continue
            unexpired_count += 1
        for token in token_to_del:
            del self.token_to_ttl[token]
        return unexpired_count


# ===================================================
# Solution 2: Optimized countUnexpiredTokens with DLL
# ===================================================

"""
countUnexpiredTokens:
   Time: O(n)
   Amortized Time: O(1)
   Space: O(n)
"""
class Node:
    def __init__(self, tokenId, expiry):
        self.tokenId = tokenId
        self.expiry = expiry
        self.prev = None
        self.next = None


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.map = {}          # tokenId -> Node
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1

    def _append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.count += 1

    def generate(self, tokenId: str, currentTime: int) -> None:
        expiry = currentTime + self.ttl
        node = Node(tokenId, expiry)
        self.map[tokenId] = node
        self._append(node)
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.map:
            return

        node = self.map[tokenId]
        if node.expiry <= currentTime:
            return

        # remove old node
        self._remove(node)
        # append renewed node
        node.expiry = currentTime + self.ttl
        self._append(node)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.head.next != self.tail and self.head.next.expiry <= currentTime:
            node = self.head.next
            self._remove(node)
            del self.map[node.tokenId]

        return self.count
