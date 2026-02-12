from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        cur_level = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    cur_level.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while cur_level:
            nxt_level = deque()

            for cur_row, cur_col in cur_level:
                for dr, dc in directions:
                    nr, nc = cur_row + dr, cur_col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        nxt_level.append((nr, nc))

            # Only a "minute" passes if something actually rotted this round
            if nxt_level:
                minutes += 1
            cur_level = nxt_level

        if fresh == 0: return minutes
        return -1
