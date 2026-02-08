from typing import List
from collections import defaultdict, deque

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build graph and degree array
        graph = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # 1) Peel leaves to find cycle nodes
        removed = set()   # removed OR scheduled-to-be-removed
        q = deque()

        for node in range(n):
            if degree[node] == 1:
                q.append(node)
                removed.add(node)

        while q:
            cur = q.popleft()
            for nei in graph[cur]:
                if nei in removed:
                    continue
                degree[nei] -= 1
                if degree[nei] == 1:
                    removed.add(nei)
                    q.append(nei)

        # 2) Multi-source BFS from cycle nodes to compute distance
        dist = [-1] * n
        bfs = deque()

        for node in range(n):
            if node not in removed:      # cycle node
                dist[node] = 0
                bfs.append((node, 0))    # track distance in deque

        while bfs:
            cur, d = bfs.popleft()
            for nei in graph[cur]:
                if dist[nei] != -1:
                    continue
                dist[nei] = d + 1
                bfs.append((nei, d + 1))

        return dist
