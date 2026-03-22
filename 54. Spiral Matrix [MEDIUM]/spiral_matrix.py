class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(matrix)
        start_col, end_col = 0, len(matrix[0])
        results = []
        while start_row<end_row and start_col<end_col:
            for i in range(start_col, end_col):
                results.append(matrix[start_row][i])
            start_row += 1
            
            for i in range(start_row, end_row):
                results.append(matrix[i][end_col-1])
            end_col -= 1
            
            if end_row>start_row:
                for i in range(end_col, start_col, -1):
                    results.append(matrix[end_row-1][i-1])
                end_row -= 1
            
            if end_col>start_col:
                for i in range(end_row, start_row, -1):
                    results.append(matrix[i-1][start_col])
                start_col += 1
        return results
            
