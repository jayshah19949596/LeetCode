"""
78. Subsets [MEDIUM]
https://leetcode.com/problems/subsets

### 1. Question Explanation:
----------------------------
Given an integer array nums of unique elements, return all possible
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order

#### Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#### Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

"""
==========================
APPROACH-1: Recursion
==========================

### 1. Complexity Analysis:
----------------------------
Time: O(n⋅2**n)
Space: O(n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def recurse(inter_arr, idx):
            subsets.append(inter_arr[:])
            for i in range(idx, len(nums)):
                inter_arr.append(nums[i])
                recurse(inter_arr, i+1)
                inter_arr.pop()
        recurse([], 0)
        return subsets

"""
==========================
APPROACH-2: Iterative
==========================

### 1. Complexity Analysis:
----------------------------
Time: O(n⋅2**n)
Space: O(n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset+[num])
            subsets = new_subsets+subsets
        return subsets
