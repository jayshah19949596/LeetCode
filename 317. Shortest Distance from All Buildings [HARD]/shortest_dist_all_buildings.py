
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Directions for moving right, down, up, left
        
        # A grid to accumulate the total distance from all buildings to each empty space
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = math.inf
            queue = deque()  # BFS queue for current building's BFS
            queue.append([row, col, 0])  # [current row, current column, current distance]
            
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                
                # Try moving in all four directions
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    
                    # Check if the new position is valid (within bounds and is an empty space)
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                        # Update the total distance for the empty space
                        total_sum[next_row][next_col] += curr_step + 1
                        # Keep track of the minimum distance
                        min_distance = min(min_distance, total_sum[next_row][next_col])
                        # Mark the cell as visited by decrementing the value to avoid revisiting
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])
            
            return min_distance

                
        count = 0  # A counter for the number of buildings encountered
        building_distance=math.inf
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Perform BFS from this building to calculate shortest distance to all empty spaces
                    building_distance = bfs(row, col, count)
                    # Increment the building counter
                    count += 1
                    if building_distance == math.inf:
                        return -1 # If some empty space cannot reach all buildings, return -1
        
        return building_distance
