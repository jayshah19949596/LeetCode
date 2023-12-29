"""
39. Combination Sum [MEDIUM]
https://leetcode.com/problems/word-break-ii/

### 1. Question Explanation:
----------------------------
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#### Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

#### Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

#### Example 3:
Input: candidates = [2], target = 1
Output: []

### 2. Complexity Analysis:
----------------------------
Let N be the number of candidates, T be the target value, and M be the minimal value among the candidates.

Time Complexity: O(N^(T/M+1))
Space Complexity: O(N^(T/M))
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def recurse_dfs(rec_target, combination, idx):

            if rec_target == 0:
                results.append(combination)
                return

            if rec_target < 0: return

            for i in range(idx, len(candidates)):
                candidate = candidates[i]
                recurse_dfs(rec_target - candidate, combination + [candidate],
                            i)  # give the current number another chance

        recurse_dfs(target, [], 0)
        return results