"""
15. 3Sum [Medium]
https://leetcode.com/problems/3sum

### 1. Question Explanation:
----------------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

### 2. Solution Explanation:
----------------------------
Approach: Sorting with Two Pointers

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N^2)
Space Complexity: O(N)
"""
from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0: left += 1
                elif total > 0: right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
