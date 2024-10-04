from typing import List
import heapq
import math


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        total_moves = self.dijkstras_search(grid)
        if total_moves == float("inf"):
            return -1
        else:
            return total_moves

    def dijkstras_search(self, grid):
        n, m = len(grid)-1, len(grid[0])-1
        if grid[0][0] == 1 or grid[-1][-1] == 1: return float("inf")

        neighboring_rows = [0, 1, -1, 0, -1, 1, -1, 1]
        neighboring_cols = [1, 0, 0, -1, -1, 1, 1, -1]
        queue = [ [1, 0, 0] ]
        visited = set()

        while queue:
            moves, cur_row, cur_col = heapq.heappop(queue)

            if cur_row == len(grid) - 1 and cur_col == len(grid[0]) - 1:
                # No need to keep track of Min Moves. The First destination found already has moves.
                return moves

            if (cur_row, cur_col) in visited: continue
            visited.add((cur_row, cur_col))

            for neighbor_row, neighbor_col in zip(neighboring_rows, neighboring_cols):
                next_row, next_col = cur_row + neighbor_row, cur_col + neighbor_col
                if next_row >= 0 and next_row < len(grid) and next_col >= 0 and next_col < len(grid[0]) and \
                        grid[next_row][next_col] == 0:
                    heapq.heappush(queue, [moves+1, cur_row + neighbor_row, cur_col + neighbor_col])
        return float("inf")