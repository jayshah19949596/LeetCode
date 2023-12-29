"""
53. Maximum Subarray [MEDIUM]
https://leetcode.com/problems/maximum-subarray/

### 1. Question Explanation:
----------------------------
Given an integer array nums, find the subarray with the largest sum, and return its sum

### 2. Solution Explanation:
----------------------------
Kadane’s Algorithm
The idea of Kadane’s algorithm is to maintain a variable 'max_ending' that stores the maximum sum contiguous subarray ending at current index.
Variable 'max_so_far' stores the maximum sum of contiguous subarray found so far,
Everytime there is a positive-sum value in 'max_ending' compare it with 'max_so_far' and update 'max_so_far' if it is greater than 'max_so_far'.


### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N).
Space Complexity: O(1).
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending = nums[0]
        for i in range(1, len(nums)):
            max_ending = max(max_ending+nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending)
        return max_so_far