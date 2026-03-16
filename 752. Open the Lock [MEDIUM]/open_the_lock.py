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
=============================================
Approach:2 - Bidirectional BFS with Set
=============================================
"""

from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(arr):
            neighbor_list = []
            for i in range(4):
                num = arr[i]

                arr[i] = str((int(num) + 1) % 10)
                neighbor_list.append("".join(arr))

                arr[i] = str((int(num) - 1) % 10)
                neighbor_list.append("".join(arr))

                arr[i] = num
            return neighbor_list

        start = "0000"
        dead_set = set(deadends)

        if start == target:
            return 0
        if start in dead_set or target in dead_set:
            return -1

        begin_set = set([start])
        end_set = set([target])
        visited = set([start, target])
        steps = 0

        while begin_set and end_set:
            # always expand the smaller frontier
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()
            steps += 1

            for cur_node in begin_set:
                for child_node in neighbors(list(cur_node)):
                    if child_node in dead_set:
                        continue

                    if child_node in end_set:
                        return steps

                    if child_node in visited:
                        continue

                    visited.add(child_node)
                    next_level.add(child_node)

            begin_set = next_level

        return -1

"""
=================================================
Approach:3 - Bidirectional BFS with Queue
=================================================
"""

from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(arr):
            res = []
            for i in range(4):
                num = arr[i]

                arr[i] = str((int(num) + 1) % 10)
                res.append("".join(arr))

                arr[i] = str((int(num) - 1) % 10)
                res.append("".join(arr))

                arr[i] = num
            return res

        start = "0000"
        dead_set = set(deadends)

        if start == target:
            return 0
        if start in dead_set or target in dead_set:
            return -1

        # two BFS queues
        q1 = deque([start])
        q2 = deque([target])

        # distance maps
        dist1 = {start: 0}
        dist2 = {target: 0}

        while q1 and q2:

            # expand the smaller queue for efficiency
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                dist1, dist2 = dist2, dist1

            for _ in range(len(q1)):
                cur = q1.popleft()

                for nxt in neighbors(list(cur)):
                    if nxt in dead_set:
                        continue

                    if nxt in dist1:
                        continue

                    # searches meet
                    if nxt in dist2:
                        return dist1[cur] + 1 + dist2[nxt]

                    dist1[nxt] = dist1[cur] + 1
                    q1.append(nxt)

        return -1

"""
=======================
Approach:4 - A*

Because the state space is small, edges are uniform, and the target is known, bidirectional BFS typically outperforms A*. 
A* helps when the heuristic is extremely strong or the state space is very large.

For unweighted, reversible problems with known target and moderate depth, bidirectional BFS usually provides the best practical performance. 
A* becomes superior when the heuristic is highly informative or the search space is extremely large.
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
