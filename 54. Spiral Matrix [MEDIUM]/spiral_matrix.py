class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []
        
        start_row, end_row = 0, len(mat) - 1
        start_col, end_col = 0, len(mat[0]) - 1
        results = []
        
        while start_row <= end_row and start_col <= end_col:
            for col in range(start_col, end_col + 1):
                results.append(mat[start_row][col])
            start_row += 1

            for row in range(start_row, end_row + 1):
                results.append(mat[row][end_col])
            end_col -= 1

            if start_row <= end_row:
                for col in range(end_col, start_col - 1, -1):
                    results.append(mat[end_row][col])
                end_row -= 1

            if start_col <= end_col:
                for row in range(end_row, start_row - 1, -1):
                    results.append(mat[row][start_col])
                start_col += 1

        return results
