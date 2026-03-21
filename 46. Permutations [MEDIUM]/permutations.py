"""
46. Permutations [MEDIUM]
https://leetcode.com/problems/permutations/
Given a collection of distinct numbers, return all possible permutations.

For each number, insert it at all possible
places in all existing permutations.
Alternatively recursively swap every index
with every greater index (and itself).
Time - O(n^2 * n!).  n! results, each of with has n elements
added, each addition taking O(n) time for list slicing
Space - O(n *n!)
"""
from typing import List


class Solution2(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            new_permutations = []
            for perm in permutations:
                for i in range(0, len(perm) + 1):
                    new_permutations.append(perm[:i] + [num] + perm[i:])
            permutations = new_permutations

        return permutations


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ryt = len(nums) - 1
        permutations = []

        def recurse_permute(lft):
            if lft == ryt:
                permutations.append(nums[:])
                return
            for idx in range(lft, ryt + 1):
                nums[lft], nums[idx] = nums[idx], nums[lft]
                recurse_permute(lft + 1)
                nums[lft], nums[idx] = nums[idx], nums[lft]

        recurse_permute(0)
        return permutations
