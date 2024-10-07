class Solution(object):
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        row, direction = 0, -1
        table = [[] for i in range(num_rows)]

        for i in range(len(s)):

            if row == 0 or row == num_rows - 1:
                direction = -1 * direction
            table[row].append(s[i])
            row = row + direction

        return "".join([char for row in table for char in row])
