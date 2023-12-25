
"""
============================
APPROACH-1: Brute Force DFS
===========================
"""
class Solution(object):
    def largestIsland(self, grid):
        max_area = 0
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.iterative_dfs(grid, r, c, rows, cols)
                else:
                    grid[r][c] = 1
                    area = self.iterative_dfs(grid, r, c, rows, cols)
                    grid[r][c] = 0
                max_area = max(max_area, area)
        return max_area

    def iterative_dfs(self, grid, r, c, rows, cols):
        area = 1
        visited = set([(r, c)])
        neighbor_rows = [0, 1, 0, -1]
        neighbor_cols = [1, 0, -1, 0]
        stack = [(r, c)]

        while stack:
            cur_r, cur_c = stack.pop()
            for nr, nc in zip(neighbor_rows, neighbor_cols):
                new_r, new_c = cur_r + nr, cur_c + nc
                if rows >= new_r >= 0 and cols >= new_c >= 0 and grid[new_r][new_c] == 1:
                    if (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        area += 1
                        stack.append((new_r, new_c))

        return area


"""
============================
APPROACH-2: Component Sizes
============================
"""
class Solution(object):
    def get_neighbors(self):
        neighbor_rows = [0, 1, 0, -1]
        neighbor_cols = [1, 0, -1, 0]
        return zip(neighbor_rows, neighbor_cols)

    def largestIsland(self, grid):
        area_map = {}
        max_area = 0
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if (r, c) not in area_map:
                        self.iterative_dfs(grid, r, c, rows, cols, area_map)
                        max_area = max(max_area, area_map[(r, c)][1])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visisted, area = set([]), 1
                    for nr, nc in self.get_neighbors():
                        if (r + nr, c + nc) in area_map:
                            island_id, island_area = area_map[(r + nr, c + nc)]
                            if island_id not in visisted:
                                visisted.add(island_id)
                                area += island_area
                    max_area = max(max_area, area)

        return max_area

    def iterative_dfs(self, grid, r, c, rows, cols, area_map):
        area = 1
        visited = set([(r, c)])
        neighbor_rows = [0, 1, 0, -1]
        neighbor_cols = [1, 0, -1, 0]
        stack = [(r, c)]

        while stack:
            cur_r, cur_c = stack.pop()
            for nr, nc in self.get_neighbors():
                new_r, new_c = cur_r + nr, cur_c + nc
                if rows >= new_r >= 0 and cols >= new_c >= 0 and grid[new_r][new_c] == 1:
                    if (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        area += 1
                        stack.append((new_r, new_c))

        island_id = len(area_map) + 1
        for row, col in visited:
            area_map[(row, col)] = [island_id, area]
        return area