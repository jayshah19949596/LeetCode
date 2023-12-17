"""
https://leetcode.com/problems/target-sum

### 1. Question Explanation:
----------------------------
You are given an integer array "nums" and an integer "target".
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

#### Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

#### Example 2:
Input: nums = [1], target = 1
Output: 1
"""
from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # return self.iterative_brute_force_dfs(nums, target)
        return self.recurse_dfs(nums, 0, target, 0, defaultdict(int))

    def recurse_dfs(self, nums, idx, target, results, memo):
        """
        Time complexity: O(t*n). The memo array of size O(t*n) has been filled just once.
        Here, "t" refers to the sum of the nums array and "n" refers to the length of the nums array.
        Space complexity: O(t*n). The depth of recursion tree can go up to nnn.
        The memo array contains t*n elements.
        """
        if (idx, target) in memo:
            return memo[(idx, target)]

        if idx == len(nums):
            if target == 0: results += 1
            memo[(idx, target)] = results
            return results

        minus_return = self.recurse_dfs(nums, idx+1, target-nums[idx], results)
        plus_return = self.recurse_dfs(nums, idx+1, target+nums[idx], results)

        memo[(idx, target)] = plus_return+minus_return
        return plus_return+minus_return

    def iterativebrute_force_dfs(self, nums, target):
        signs, results = ["+", "-"], [[]]
        for num in nums:
            sub_results = []
            for sign in signs:
                for result in results:
                    if sign == "+": sub_results.append(result+[num])
                    else: sub_results.append(result+[-num])
            results = sub_results

        answer = 0
        for result in results:
            summ = sum(result)
            if summ == target:
                answer += 1

        return answer