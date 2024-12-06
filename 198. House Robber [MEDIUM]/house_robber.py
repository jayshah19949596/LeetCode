"""
198. House Robber [MEDIUM]
https://leetcode.com/problems/house-robber/

### 1. Question:
----------------------------
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected.
Security systems will automatically contact the police if two adjacent houses were broken into on the same night.

#### Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

#### Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

### 2. Solution:
----------------------------
1. Subproblem: 'F(i)' as the maximum amount of money tha can be robbed upto house 'i'
2. Recursive Formulation:
    - 'F(i)=max( F(i-1), F(i-2) + money in house[i] )'
    - It means at each house, either skip it and take maximum amount robbed from the previous house,
    Or rob the current house and add the amount in that house to the maximum robbed from two houses before.
"""
from typing import List

class Solution:
    """
    ------------------------------------------------
    APPROACH 1: Bottom-up Recursion with Brute Force
    ------------------------------------------------
    Time: O(2^N)
    Space: O(N)
    """
    def rob(self, houses: List[int]) -> int:
        
        def recurse(idx):
            if idx>=len(houses): return 0
            keep_cur_rob = houses[idx]+recurse(idx + 2)
            skip_cur_rob = recurse(idx + 1)
            return max(keep_cur_rob, skip_cur_rob)
        
        return recurse(0)

class Solution:
    """
    ------------------------------------------------
    APPROACH 2:  Bottom-up Recursion with Memoization
    ------------------------------------------------
    Time: O(N)
    Space: O(N)
    """
    def rob(self, houses: List[int]) -> int:
        memo = {}
        def recurse(idx):
            if idx in memo: return memo[idx]
            if idx>=len(houses): return 0

            keep_cur_rob = houses[idx] + recurse(idx + 2)
            skip_cur_rob = recurse(idx + 1)
            memo[idx] = max(keep_cur_rob, skip_cur_rob)
            return memo[idx]
        
        return recurse(0)



class Solution:
    """
    ------------------------------------------------
    APPROACH 3: Space Optimized Dynamic Programming
    ------------------------------------------------
    Time: O(N)
    Space: O(1)
    """
    def rob(self, houses: List[int]) -> int:        
        max_rob_so_far = 0
        max_rob_till_prev_idx = 0
        max_rob_till_before_prev_idx = 0

        for i in range(0, len(houses)):
            take_cur_rob = max_rob_till_before_prev_idx + houses[i]
            skip_cur_rob = max_rob_till_prev_idx
            max_rob_so_far = max(take_cur_rob, skip_cur_rob)
            max_rob_till_before_prev_idx = max_rob_till_prev_idx
            max_rob_till_prev_idx = max_rob_so_far

        return max_rob_so_far
