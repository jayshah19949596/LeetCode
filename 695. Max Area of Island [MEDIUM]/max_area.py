class Solution(object):
    def __init__(self):
        self.visited = set([])
        self.n_r = [ 0, 0, -1, 1]
        self.n_c = [-1, 1,  0, 0]
        self.n_count = 4
         
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in self.visited:
                    self.visited.add((r, c))
                    area = [1]
                    self.dfs(r, c, grid, area)
                    max_area = max(max_area, area[0])
        return max_area
                    
        
    def dfs(self, r, c, grid, area):
        for i in range(self.n_count):
            n_r, n_c = self.n_r[i], self.n_c[i]
            if (r+n_r, c+n_c) not in self.visited:
                if r+n_r>=0 and r+n_r<len(grid) and c+n_c>=0 and c+n_c<len(grid[0]): 
                    if grid[r+n_r][c+n_c] == 1:
                        self.visited.add((r+n_r, c+n_c))
                        area[0] += 1
                        self.dfs(r+n_r, c+n_c, grid, area)        
