"""
41. First Missing Positive [HARD]
https://leetcode.com/problems/first-missing-positive/

### 1. Question Explanation:
----------------------------
Given an unsorted integer array, find the first missing positive integer.
e.g. given [1,2,0] return 3, and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

### 2. Solution:
----------------------------
If an element of nums is a positive integer that could
appear in nums (1 to len(nums) inclusive) and is not in
correct place (nums[i] = i+1) then swap.

### 3. Complexity Analysis:
----------------------------
Time - O(n)
Space - O(1)
"""
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            while (nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]):
                swap(nums, i, nums[i] - 1)

        for i in range(len(nums)):
            if (nums[i] != i + 1):
                return i + 1

        return len(nums) + 1
