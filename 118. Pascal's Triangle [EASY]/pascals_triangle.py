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
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return [] # Handle edge case
        
        res = [[1]]
        for row in range(1, numRows):
            no_of_ele = row + 1
            cur_row = [1]
            # Use the previous row in res to calculate middle elements
            for j in range(no_of_ele - 2):
                cur_row.append(res[-1][j] + res[-1][j+1])
            cur_row.append(1)
            res.append(cur_row) 
            
        return res
        
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
