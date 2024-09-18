"""
90. Subsets II [MEDIUM]
https://leetcode.com/problems/subsets-ii/description/

### 1. Question Explanation:
----------------------------
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
""""

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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set([])
        nums.sort()
        def recurse(arr, inter_arr, idx, n):
            subsets.add(tuple(inter_arr[:]))
            for i in range(idx, n):
                inter_arr.append(arr[i])
                recurse(arr, inter_arr, i+1, n)
                inter_arr.pop()
        recurse(nums, [], 0, len(nums))
        return list(subsets)


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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()

        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset+[num])
            subsets = new_subsets+subsets

        result, seen = [], set([])
        for subset in subsets:
            subset_tuple = tuple(subset)
            if subset_tuple not in seen:
                seen.add(subset_tuple)
                result.append(subset_tuple)
        return result