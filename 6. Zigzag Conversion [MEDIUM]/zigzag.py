class Solution(object):
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        row, direction = 0, -1
        zigzag = [[] for i in range(num_rows)]

        for i in range(len(s)):

            if row == 0 or row == num_rows - 1:
                direction = -1 * direction
            zigzag[row].append(s[i])
            row = row + direction

        results = []
        for row in zigzag:
            for char in row:
                results.append(char)
        return "".join(results)
