"""
https://leetcode.com/problems/move-zeroes

### 1. Question Explanation:
----------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

### 2. Solution Explanation:
Have two pointers "anchor_idx" and "moving_idx"
moving_idx will help us do a linear search. So it will keep on incrementing itself.
anchor_idx will always anchor itself and not increment if current iterating element is 0.
anchor_idx will

### 3. Complexity Analysis:
----------------------------
Time Complexity - O(N)
Space Complexity - O(1)
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        moving_idx = anchor_idx = 0
        for moving_idx in range(len(nums)):
            if nums[moving_idx] == 0: continue
            nums[anchor_idx] = nums[moving_idx]
            anchor_idx += 1
        for i in range(anchor_idx, len(nums)):
            nums[i] = 0
