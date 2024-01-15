"""
311. Sparse Matrix Multiplication [MEDIUM]
https://leetcode.com/problems/sparse-matrix-multiplication/

### 1. Question:
----------------------------
Given two sparse matrices mat1 of size m x k and mat2 of size k x n,
return the result of mat1 x mat2. You may assume that multiplication is always possible.
"""
from typing import List


class Solution:
    """
    ------------------------------------------
    APPROACH 1: Naive Iteration
    ------------------------------------------
    Time: O(M*K*N)
    Space: O(1)
    """
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]  # Product matrix.

        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                # If current element of mat1 is non-zero then iterate over all columns of mat2.
                if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        ans[row_index][col_index] += row_element * col_element

        return ans