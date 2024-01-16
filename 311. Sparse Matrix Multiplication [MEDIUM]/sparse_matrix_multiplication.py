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
Any element with index (row1, col1) of mat1 is multiplied with all the elements of col1th row of mat2
"""
from typing import List
from collections import defaultdict


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
    APPROACH 2: Matrix compression with HashMap
    ------------------------------------------
    Time: O(M*K*N)
    Space: O(M*K+K*N)
    """
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        m1, m2 = defaultdict(dict), defaultdict(dict)

        # compress matrix
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0: m1[i][j] = mat1[i][j]

        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0: m2[j][i] = mat2[i][j]

        ans = [[0] * n for _ in range(m)]

        # dot product
        for i, pairs1 in m1.items():
            for j, pairs2 in m2.items():
                for k, val1 in pairs1.items():
                    val2 = pairs2.get(k, 0)
                    ans[i][j] += val1 * val2
        return ans
