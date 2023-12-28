"""
118. Pascal's Triangle [EASY]
https://leetcode.com/problems/pascals-triangle/

### 1. Question Explanation:
----------------------------
Given numRows, generate the first numRows of Pascal's triangle.

### 2. Solution Explanation:
----------------------------
Next row is sum of consecutive pairs of items from previous row

### 3. Complexity Analysis:
----------------------------.
Time - O(N**2)
Space - O(N**2)
"""
from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0:
            return []

        pascal = [[1]]

        for i in range(1, num_rows):
            pascal.append([1])
            for num1, num2 in zip(pascal[-2][:-1], pascal[-2][1:]):
                pascal[-1].append(num1 + num2)
            pascal[-1].append(1)

        return pascal