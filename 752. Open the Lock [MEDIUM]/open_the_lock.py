"""
Approach:1 - BFS
"""
from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead:
            return -1
        if target == start:
            return 0

        def neighbors(s: str):
            res = []
            arr = list(s)
            for i in range(4):
                d = int(arr[i])

                # turn up
                arr[i] = str((d + 1) % 10)
                res.append("".join(arr))

                # turn down
                arr[i] = str((d - 1) % 10)
                res.append("".join(arr))

                # restore
                arr[i] = str(d)
            return res

        q = deque([(start, 0)])
        seen = {start}

        while q:
            cur, dist = q.popleft()
            for nxt in neighbors(cur):
                if nxt in dead or nxt in seen:
                    continue
                if nxt == target:
                    return dist + 1
                seen.add(nxt)
                q.append((nxt, dist + 1))

        return -1
