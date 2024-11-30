'''
Complexity Analysis
    1. Time Complexity: O((R*C)^2)), where R, CR,C is the number of rows and columns in board.
                       We need O(R*C) to scan the board, and we might crush only 3 candies repeatedly.
    2. Space Complexity: O(1) additional complexity, as we edit the board in place.
'''


class Solution(object):
    def candyCrush(self, board):
        rows, cols = len(board), len(board[0])
        todo = False
        # Tracking candies needed to be crushed on same row
        for row in range(rows):
            for col in range(cols-2):
                if abs(board[row][col]) == abs(board[row][col+1]) == abs(board[row][col+2]) != 0:
                    # negative values are to be crushed
                    board[row][col] = board[row][col+1] = board[row][col+2] = -abs(board[row][col])
                    todo = True
        # Tracking candies needed to be crushed on same col
        for row in range(rows-2):
            for col in range(cols):
                # negative values are to be crushed
                if abs(board[row][col]) == abs(board[row+1][col]) == abs(board[row+2][col]) != 0:
                    board[row][col] = board[row+1][col] = board[row+2][col] = -abs(board[row][col])
                    todo = True
        for row in range(rows):
            print(board[row])
        
        # Vertical sliding window where "write_row" is write head
        # Crushing from first column
        for col in range(cols):
            write_row = rows-1
            # Crushing from last row
            for row in range(rows-1, -1, -1):
                if board[row][col] > 0:
                    board[write_row][col] = board[row][col]
                    write_row -= 1
            for row in range(write_row, -1, -1):  # Filling the other row in the column with 0
                board[row][col] = 0
        
        return self.candyCrush(board) if todo else board
