"""
163. Missing Ranges [EASY]
https://leetcode.com/problems/missing-ranges/

### 1. Question:
----------------------------
Given a sorted integer array where elements are in the inclusive range [lower, upper], return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

### 2. Solution:
----------------------------
Track the last number seen.  If num == last_seen+2 then last_seen+1 is the start and end of a missing range.
If num > last_seen+2 then inclusive range last_seen+1 to num-1 is missing.  Update last_seen.
Do nothing if num is last_seen or last_seen+1 since nothing is missing.

### 3. Complexity Analysis:
----------------------------
Time - O(N)
Space - O(N)
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        prev_seen_num = lower-1
        nums.append(upper+1)
        results = []
        for i, num in enumerate(nums):
            if prev_seen_num+1 != num:
                results.append([prev_seen_num+1, num-1])
            prev_seen_num = num
        return results
