"""
=============================
Approach-1: Brute Force BFS
=============================
"""
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:  # If start is an obstacle, no path exists
            return 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0)]  # Right and Down movements
        queue = deque([(0, 0)])  # Start BFS from the top-left cell
        paths = {(0, 0): 1}  # Dictionary to store unique paths to each cell
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:  # Valid non-obstacle cell
                    if (nx, ny) not in paths:
                        queue.append((nx, ny))  # Add the new cell to the queue
                    # Update the number of ways to reach (nx, ny)
                    paths[(nx, ny)] = paths.get((nx, ny), 0) + paths[(x, y)]
        return paths.get((m-1, n-1), 0)  # Return paths to bottom-right corner


"""
============================================
Approach-2: Bottom-up Dynamic Programming
============================================
"""
class Solution:
    def uniquePathsWithObstacles(self, A):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        paths = [[0]*len(A[0]) for i in A]

        # initializing the left corner if no obstacle there
        if A[0][0] == 0:
            paths[0][0] = 1

        # initializing first column of the 2D matrix
        for i in range(1, len(A)):
            if A[i][0] == 0:  # If not obstacle
                paths[i][0] = paths[i-1][0]

        # initializing first row of the 2D matrix
        for j in range(1, len(A[0])):
            if A[0][j] == 0:  # If not obstacle
                paths[0][j] = paths[0][j-1]

        for i in range(1, len(A)):
            for j in range(1, len(A[0])):

            # If current cell is not obstacle
                if A[i][j] == 0:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # returning the corner value of the matrix
        return paths[-1][-1]
 
