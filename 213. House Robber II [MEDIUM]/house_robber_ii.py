"""
213. House Robber II [MEDIUM]
https://leetcode.com/problems/house-robber-ii/

### 1. Question:
----------------------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#### Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

#### Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

### 2. Solution:
----------------------------
As per 198 except consider the greater of 2 cases - allow
robbing the first house but no the last, allow robbing the
last house but not the first.

### 3. Complexity Analysis:
----------------------------
Time - O(n)
Space - O(1)
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)    # 1 house has no neighbours

        max_loot_so_far = cur_house_max_loot_so_far = prev_house_max_loot_so_far = 0
        # start robbing from second house till last but DON'T rob first house
        for i in range(1, len(nums)):
            num = nums[i]
            max_loot_so_far = max(cur_house_max_loot_so_far, prev_house_max_loot_so_far + nums[i])
            prev_house_max_loot_so_far = cur_house_max_loot_so_far
            cur_house_max_loot_so_far = max_loot_so_far

        max_loot_so_far2 = cur_house_max_loot_so_far = prev_house_max_loot_so_far = 0
        # start robbing from first house till second last house but DON'T rob last house
        for i in range(0, len(nums)-1):
            num = nums[i]
            max_loot_so_far2 = max(cur_house_max_loot_so_far, prev_house_max_loot_so_far + nums[i])
            prev_house_max_loot_so_far = cur_house_max_loot_so_far
            cur_house_max_loot_so_far = max_loot_so_far2

        return max(max_loot_so_far, max_loot_so_far2)
