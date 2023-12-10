"""
https://leetcode.com/problems/diagonal-traverse/
### 1. Question Explanation:
----------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

### 2. Solution Explanation:
Taken from leetcode editorial: https://leetcode.com/problems/diagonal-traverse/editorial/

### 3. Complexity Analysis:
----------------------------
Time - O(N.M)
Space - O(1)
"""
from typing import List


class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]: return []  # Check for an empty matrix
        N, M = len(matrix), len(matrix[0])  #  The dimensions of the matrix
        row, column = 0, 0  # Indices that will help us progress through the matrix, one element at a time.
        direction = 1  # Variable to track what direction we are processing the current diagonal
        result = []  # Final result array that will contain all the elements of the matrix

        while row < N and column < M:

            result.append(matrix[row][column]) # First and foremost, add the current element to the result matrix.

            # Move along in the current diagonal depending upon
            # the current direction.[i, j] -> [i - 1, j + 1] if
            # going up and [i, j] -> [i + 1][j - 1] if going down.
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)

            # Checking if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head.
            if new_row < 0 or new_row == N or new_column < 0 or new_column == M:

                # If the current diagonal was going in the upwards
                # direction.
                if direction:
                    # For an upwards going diagonal having [i, j] as its tail
                    # If [i, j + 1] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i + 1, j] becomes the next head
                    row += (column == M - 1)
                    column += (column < M - 1)
                else:
                    # For a downwards going diagonal having [i, j] as its tail
                    # if [i + 1, j] is within bounds, then it becomes
                    # the next head. Otherwise, the element directly below
                    # i.e. the element [i, j + 1] becomes the next head
                    column += (row == N - 1)
                    row += (row < N - 1)

                direction = 1 - direction # Flip the direction
            else:
                row = new_row
                column = new_column

        return result
