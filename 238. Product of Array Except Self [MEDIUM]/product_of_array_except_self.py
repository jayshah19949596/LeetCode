"""
https://leetcode.com/problems/product-of-array-except-self/

### 1. Question Explanation:
----------------------------
Given an array of n integers where n > 1, nums, return
an array output such that output[i] is equal to the
product of all the elements of nums except nums[i].

#### Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

#### Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

##2. Solution Explanation:
----------------------------
Iterate from left to right, calculating the product of all numbers to the left.
Iterate from right to left, multiplying each result by the product of all numbers to the right.
If any one value is zero then result is all zeros apart from that entry.

##3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List


class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        for i in range(len(nums) - 1):
            products.append(products[-1] * nums[i])

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products
