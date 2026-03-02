"""
====================================================================
Approach:1 - BFS. A minrot optimization will be bidirectional BFS.
====================================================================
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



"""
=======================
Approach:2 - A*
=======================
"""
import heapq
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        if start in dead or target in dead:
            return -1
        if target == start:
            return 0

        def h(s: str) -> int:
            # admissible heuristic: sum of circular distances per digit
            total = 0
            for a, b in zip(s, target):
                da = ord(a) - ord('0')
                db = ord(b) - ord('0')
                diff = abs(da - db)
                total += min(diff, 10 - diff)
            return total

        def neighbors(s: str):
            for i in range(4):
                d = ord(s[i]) - ord('0')
                up = (d + 1) % 10
                down = (d - 1) % 10
                yield s[:i] + chr(up + ord('0')) + s[i+1:]
                yield s[:i] + chr(down + ord('0')) + s[i+1:]

        # (f = g + h, g, state)
        pq = [(h(start), 0, start)]
        best_g = {start: 0}  # shortest known distance to each state

        while pq:
            f, g, cur = heapq.heappop(pq)

            # stale entry check
            if g != best_g.get(cur, float("inf")):
                continue

            if cur == target:
                return g

            for nxt in neighbors(cur):
                if nxt in dead:
                    continue
                ng = g + 1
                if ng < best_g.get(nxt, float("inf")):
                    best_g[nxt] = ng
                    heapq.heappush(pq, (ng + h(nxt), ng, nxt))

        return -1
