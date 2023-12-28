"""
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

### 1. Question Explanation:
----------------------------
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

#### Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
       word = "ABCCED"
Output: true

### 2. Solution Explanation:
----------------------------
Approach: DFS with Backtracking

Step 1). At the beginning, first we check if we reach the bottom case of the recursion, where the word to be matched is empty, i.e. we have already found the match for each prefix of the word.
Step 2). We then check if the current state is invalid, either the position of the cell is out of the boundary of the board or the letter in the current cell does not match with the first letter of the word.
Step 3). If the current step is valid, we then start the exploration of backtracking with the strategy of DFS. First, we mark the current cell as visited, e.g. any non-alphabetic letter will do. Then we iterate through the four possible directions, namely up, right, down and left. The order of the directions can be altered, to one's preference.
Step 4). At the end of the exploration, we revert the cell back to its original state. Finally we return the result of the exploration

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N*3^L), where 'N' is the number of cells in the board and 'L' is the length of the word to be matched.
Space Complexity: O(L), where 'L' is the length of the word to be matched.
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if self.can_find(word, 0, board, r, c):
                    return True
        return False

    def can_find(self, word, i, board, r, c):

        if i >= len(word):  # nothing more of word to find
            return True

        if not 0 <= r <= len(board) - 1 or not 0 <= c <= len(board[0]) - 1:  # outside board
            return False

        if word[i] != board[r][c]:  # no match letter
            return False

        board[r][c] = '*'  # set this position so cannot be used again

        if (self.can_find(word, i + 1, board, r + 1, c) or self.can_find(word, i + 1, board, r - 1, c) or
                self.can_find(word, i + 1, board, r, c + 1) or self.can_find(word, i + 1, board, r, c - 1)):
            return True

        board[r][c] = word[i]  # if False, reset position to letter

        return False
