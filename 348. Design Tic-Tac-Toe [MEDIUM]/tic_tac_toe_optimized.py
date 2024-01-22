"""
348. Design Tic-Tac-Toe [MEDIUM]
https://leetcode.com/problems/design-tic-tac-toe

### 1. Question Explanation:
----------------------------
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

###  Complexity Analysis:
----------------------------
Time Complexity: O(1)
Space Complexity: O(N)
"""
from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row_count = defaultdict(int)
        self.col_count = defaultdict(int)
        self.diagonal_count = defaultdict(int)
        self.anti_diagonal_count = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        self.row_count[(row, player)] += 1
        self.col_count[(col, player)] += 1

        if row == col:
            self.diagonal_count[player] += 1
        if col == self.n - row - 1:
            self.anti_diagonal_count[player] += 1

        if (self.row_count[(row, player)] == n or self.col_count[(col, player)] == n
        or self.diagonal_count[player] == n or self.anti_diagonal_count[player] == n):
            return player
        return 0

