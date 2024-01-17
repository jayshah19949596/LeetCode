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
        def recurse_permute(arr, lft, ryt):
            if lft == ryt:
                nonlocal permutations
                permutations.append(arr[:])
                return
            for idx in range(lft, ryt + 1):
                arr[lft], arr[idx] = arr[idx], arr[lft]
                recurse_permute(arr, lft + 1, ryt)
                arr[lft], arr[idx] = arr[idx], arr[lft]
        permutations = []
        recurse_permute(nums, 0, len(nums) - 1)
        return permutations


