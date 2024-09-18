"""
90. Subsets II [MEDIUM]
https://leetcode.com/problems/subsets-ii/description/

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
        def recurse(arr, inter_arr, idx, n):
            subsets.append(inter_arr[:])
            for i in range(idx, n):
                inter_arr.append(arr[i])
                recurse(arr, inter_arr, i+1, n)
                inter_arr.pop()
        recurse(nums, [], 0, len(nums))
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