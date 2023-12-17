"""
https://leetcode.com/problems/search-a-2d-matrix

### 1. Question Explanation:
----------------------------
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer "target", return "true" if "target" is in "matrix" or false otherwise.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        return self.optimized_binary_search_approach(matrix, target)
        # return self.binary_search_approach(matrix, target)
        # return self.two_pointer_approach(matrix, target)

    def optimized_binary_search_approach(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(Log(N*M))
        Space: O(1)
        """
        no_of_rows, no_of_cols = len(matrix), len(matrix[0])

        # binary search
        left, right = 0, no_of_rows * no_of_cols - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // no_of_cols][pivot_idx % no_of_cols]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

    def binary_search_approach(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(N*Log(M))
        Space: O(1)
        """
        rows, cols = len(mat), len(mat[0])
        # set indexes for bottom left element
        i, j = rows - 1, 0
        while (i < rows and i >= 0):
            if (mat[i][j] == target):
                return True
            elif (mat[i][j] > target):
                i -= 1
            else:
                break

        return bin_search(i, mat, target)

    def two_pointer_approach(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(N*M)
        Space: O(1)
        """
        i, j = 0, len(matrix[0]) - 1

        while (i < len(matrix) and j >= 0):
            if (matrix[i][j] == target): return True

            if (matrix[i][j] > target):
                j -= 1
            else:
                i += 1

        return False


def bin_search(row, mat, x):
    left, ryt = 0, len(mat[row]) - 1

    while left <= ryt:

        mid = (left + ryt) // 2

        if mat[row][mid] == x:
            return True
        elif mat[row][mid] > x:
            ryt = mid - 1
        elif mat[row][mid] < x:
            left = mid + 1

    return False
