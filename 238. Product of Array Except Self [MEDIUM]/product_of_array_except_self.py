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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        left_prod = 1
        # Build prefix products
        for i in range(n):
            res.append(left_prod)
            left_prod *= nums[i]

        right_prod = 1
        # Traverse from right to left to build suffix product
        for i in range(n - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]  ## right product for next iteration

        return res
