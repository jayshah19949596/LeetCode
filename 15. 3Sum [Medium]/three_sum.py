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


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = target = 0
        results = []
        nums.sort()
        while i < len(nums):
            left, right = i + 1, len(nums) - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                if triplet_sum == target:
                    results.append([nums[i], nums[left], nums[right]])
                    left, right = left+1, right-1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif triplet_sum < target:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif triplet_sum > target:
                    right -= 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return results