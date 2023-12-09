"""
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
        target = 0
        nums.sort()
        results = []
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]

                if triplet_sum == target:
                    results.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[k] == nums[k + 1] and k > j:
                        k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif triplet_sum < target:
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif triplet_sum > target:
                    k -= 1
                    while nums[k] == nums[k + 1] and k > j:
                        k -= 1

            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return results