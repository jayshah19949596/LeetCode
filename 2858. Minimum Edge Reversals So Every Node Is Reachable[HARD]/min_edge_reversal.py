from typing import List
import sys
sys.setrecursionlimit(1_000_000)

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency: (neighbor, cost)
        # For directed u->v:
        #   u->v has cost 0, v->u has cost 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        ans = [0] * n

        # 1) Compute reversals needed when root is 0
        def dfs_count(cur: int, parent: int) -> int:
            total = 0
            for nxt, cost in graph[cur]:
                if nxt == parent: continue
                total += cost + dfs_count(nxt, cur)
            return total

        ans[0] = dfs_count(0, -1)

        # 2) Reroot: derive ans for all nodes using parent answer
        def dfs_reroot(cur: int, parent: int) -> None:
            for nxt, cost in graph[cur]:
                if nxt == parent:
                    continue
                # Moving root from cur to nxt:
                # cost==0 means edge is cur->nxt originally => becomes "wrong" by 1
                # cost==1 means edge is nxt->cur originally => becomes "right" by 1 (so -1)
                if cost == 0: ans[nxt] = ans[cur] + 1
                else: ans[nxt] = ans[cur] - 1
                dfs_reroot(nxt, cur)

        dfs_reroot(0, -1)
        return ans
