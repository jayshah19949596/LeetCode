"""
41. First Missing Positive [HARD]
https://leetcode.com/problems/first-missing-positive/

### 1. Question Explanation:
----------------------------
Given an unsorted integer array, find the first missing positive integer.
e.g. given [1,2,0] return 3, and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.

### 2. Solution:
----------------------------
If an element of nums is a positive integer that could
appear in nums (1 to len(nums) inclusive) and is not in
correct place (nums[i] = i+1) then swap.

### 3. Complexity Analysis:
----------------------------
Time - O(n)
Space - O(1)
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            """
            =====================================
            Don't move from current index to next index UNTILL 
            all valid values in current index are moved to their valid index. 
            Current index should always be filled with it's right index or with invalid value. 
            =====================================
            """
            correct_idx = nums[i] - 1 # Correct index of the current value is nums[i] - 1
            # nums[i] != nums[correct_idx] condition is to ignore swapping if the duplicate element is in it's correct index
            if (0 < nums[i] <= n and nums[i] != nums[correct_idx]):  
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i] # Swap the current value to it index
                
            else:
                i += 1

        for i in range(n):
            if (nums[i]-1 != i):
                return i+1

        return n+1
