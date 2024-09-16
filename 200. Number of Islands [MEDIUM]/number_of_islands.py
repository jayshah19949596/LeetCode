"""
200. Number of Islands [MEDIUM]
https://leetcode.com/problems/number-of-islands

### 1. Question:
----------------------------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
class Solution:
    def __init__(self):
        self.neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.visited = set([])

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    self.group_neighors((r, c), rows, cols, grid)
                    num_islands += 1
        return num_islands

    def group_neighors(self, node, rows, cols, grid):
        self.visited.add(node)
        r, c = node
        for nr, nc in self.neighbors:
            if rows > r+nr >= 0 and  cols> c+nc >= 0:
                if grid[r+nr][c+nc] == "1" and (r+nr, c+nc) not in self.visited:
                    self.group_neighors((r+nr, c+nc), rows, cols, grid)

class Solution:
    def __init__(self):
        self.neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]


    def create_sets(self, grid):
        self.parent, self.rank = {}, {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.parent[(r, c)] = (r, c)
                self.rank[(r, c)] = 0

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
            # below line applies compression for faster next search of parent!!!
            self.parent[node] = self.parent[self.parent[node]]
        return node

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] +=1

    def numIslands(self, grid: List[List[str]]) -> int:
        self.create_sets(grid)
        rows, cols = len(grid), len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.group_neighors((r, c), rows, cols, grid)

        num_islands = set([])
        for node in self.parent:
            if grid[node[0]][node[1]] == "1":
                parent_node = self.find(node)
                num_islands.add(parent_node)
        return len(num_islands)

    def group_neighors(self, node, rows, cols, grid):
        r, c = node
        for nr, nc in self.neighbors:
            if rows > r+nr >= 0 and  cols> c+nc >= 0:
                if grid[r+nr][c+nc] == "1" and (r+nr, c+nc):
                    self.union(node, (r+nr, c+nc))
