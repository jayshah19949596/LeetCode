"""
https://leetcode.com/problems/product-of-array-except-self/

### 1. Question Explanation:
----------------------------
A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
 - BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
 - BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.


#### Example 1:
Input: mat = [[0,0],
              [1,1]]
Output: 0

#### Example 2:
Input: mat = [[0,0],
              [0,1]]
Output: 1

#### Example 3:
Input: mat = [[0,0],
              [0,0]]
Output: -1
"""
from typing import List


class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       pass
   def dimensions(self) -> List:
       pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        return self.binary_search_each_row_approach(binaryMatrix)

    def binary_search_each_row_approach(self, binaryMatrix):
        """
        Time complexity : O(N*LogM)
        Space complexity: O(1)
        """
        global_left_most_one = float("inf")
        no_of_rows, no_of_cols = binaryMatrix.dimensions()

        for i in range(no_of_rows):
            left_most_one = self.binary_search(binaryMatrix, i, min(no_of_cols, global_left_most_one))
            global_left_most_one = min(global_left_most_one, left_most_one)

        if global_left_most_one == float("inf"):
            return -1
        else:
            return global_left_most_one

    def binary_search(self, binaryMatrix, row_idx, no_of_cols):
        left, right = 0, no_of_cols
        found_one = False

        while left < right:
            middle = (left + right) // 2
            if binaryMatrix.get(row_idx, middle) == 1:
                found_one = True
                right = middle
            else:
                left = middle + 1

        if found_one:
            return right
        else:
            return float("inf")