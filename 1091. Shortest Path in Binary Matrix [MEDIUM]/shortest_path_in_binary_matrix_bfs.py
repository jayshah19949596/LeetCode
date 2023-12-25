"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

### 1. Question Explanation:
----------------------------
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

### 2. Complexity Analysis:
----------------------------
Time Complexity - O(V+E)
Space Complexity - O(V)
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        total_moves = self.bread_first_search(grid)
        if total_moves == float("inf"):return -1
        else: return total_moves

    def bread_first_search(self, grid):
        min_moves = float("inf")
        if grid[0][0] == 1 or grid[-1][-1] == 1: return min_moves

        neighboring_rows = [0, 1, -1, 0, -1, 1, -1, 1]
        neighboring_cols = [1, 0, 0, -1, -1, 1, 1, -1]
        queue = deque([[0, 0, 1]])
        visited = set()

        while queue:
            cur_row, cur_col, moves = queue.popleft()

            if cur_row == len(grid) - 1 and cur_col == len(grid[0]) - 1:
                min_moves = min(min_moves, moves)
                continue
            if (cur_row, cur_col) in visited: continue
            visited.add((cur_row, cur_col))

            for neighbor_row, neighbor_col in zip(neighboring_rows, neighboring_cols):
                next_row, next_col = cur_row + neighbor_row, cur_col + neighbor_col
                if next_row >= 0 and next_row < len(grid) and next_col >= 0 and next_col < len(grid[0]) and \
                        grid[next_row][next_col] == 0:
                    queue.append([cur_row + neighbor_row, cur_col + neighbor_col, moves + 1])

        return min_moves
