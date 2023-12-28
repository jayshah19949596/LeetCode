"""
152. Maximum Product Subarray [MEDIUM]
https://leetcode.com/problems/maximum-product-subarray/

### 1. Question Explanation:
----------------------------
Find the contiguous subarray within an array (containing
at least one number) which has the largest product.

### 2. Solution Explanation:
----------------------------
Calculate the most positive and most negative
subarray products ending at each element.
Either the element alone or multiplied by
previous most positive or most negative.

### 3. Complexity Analysis:
----------------------------
Time - O(n)
Space - O(1)
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_product = float('-inf')
        most_neg, most_pos = 1, 1

        for num in nums:
            most_pos, most_neg = max(num, most_pos * num, most_neg * num), min(num, most_pos * num, most_neg * num)
            largest_product = max(largest_product, most_pos, most_neg)

        return largest_product