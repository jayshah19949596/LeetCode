"""
311. Sparse Matrix Multiplication [MEDIUM]
https://leetcode.com/problems/sparse-matrix-multiplication/

### 1. Question:
----------------------------
Given two sparse matrices mat1 of size m x k and mat2 of size k x n,
return the result of mat1 x mat2. You may assume that multiplication is always possible.

2. Solution:
----------------------------
https://leetcode.com/problems/sparse-matrix-multiplication/editorial/
"""
from typing import List


class Solution:
    """
    ------------------------------------------
    APPROACH 1: Naive Iteration
    ------------------------------------------
    Time: O(M*K*N)
        M, number of rows in mat1
        K, number of columns in mat1
        N, number of columns in mat2
        ans, matrix of size M*N
    Space: O(1)
    """
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))] # Product matrix.
        for row_idx in range(len(mat1)):
            for ele_idx in range(len(mat1[row_idx])):
                if mat1[row_idx][ele_idx] == 0: continue
                for col_idx in range(len(mat2[ele_idx])):
                    ans[row_idx][col_idx] += mat1[row_idx][ele_idx]*mat2[ele_idx][col_idx]
        return ans


class Solution:
    """
    ------------------------------------------
    APPROACH 2: List of Lists
    ------------------------------------------
    Time: O(M*K*N)
        M, number of rows in mat1
        K, number of columns in mat1
        N, number of columns in mat2
        ans, matrix of size M*N
    Space: O(M*K+K*N)
    """
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix

        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        # Store the non-zero values of each matrix.
        A, B = compress_matrix(mat1), compress_matrix(mat2)

        ans = [[0] * n for _ in range(m)]
        for mat1_row in range(m):
            # Iterate on all current 'row' non-zero elements of mat1.
            for element1, mat1_col in A[mat1_row]:
                # Multiply and add all non-zero elements of mat2
                # where the row is equal to col of current element of mat1.
                for element2, mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col] += element1 * element2
        return ans
