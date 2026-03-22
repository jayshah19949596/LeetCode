class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(mat)
        start_col, end_col = 0, len(mat[0])
        results = []
        while start_row<end_row and start_col<end_col:
            for col in range(start_col, end_col):
                results.append(mat[start_row][col])
            start_row += 1

            for row in range(start_row, end_row):
                results.append(mat[row][end_col-1])
            end_col -= 1

            if end_row>start_row:
                for col in range(end_col, start_col, -1):
                    results.append(mat[end_row-1][col-1])
                end_row -= 1

            if end_col>start_col:
                for row in range(end_row, start_row, -1):
                    results.append(mat[row-1][start_col])
                start_col += 1

        return results
