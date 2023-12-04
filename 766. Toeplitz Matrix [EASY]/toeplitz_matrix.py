"""
https://leetcode.com/problems/valid-palindrome-ii/description/

### 1. Question Explanation:
----------------------------
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(M*N)
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row > 0 and col > 0 and matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True
