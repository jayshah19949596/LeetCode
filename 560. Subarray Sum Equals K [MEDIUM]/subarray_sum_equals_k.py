"""
https://leetcode.com/problems/subarray-sum-equals-k

### 1. Question Explanation:
----------------------------
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

#### Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

#### Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

### 2. Solution Explanation:
----------------------------
Store counts of prefix sums in dictionary. Iterate over
#array, updating running_sum and incrementing result if
running_sum == k. Lookup prefix value that makes a subararry of sum k.


### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N)
Space Complexity: O(N)
"""
from collections import defaultdict
from typing import List


class Solution(object):
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        sums = defaultdict(int) # key is prefix sum, value is count of number of prefixes
        running_sum = 0

        for num in nums:

            running_sum += num

            if running_sum == k:
                total += 1
            if running_sum - k in sums:
                total += sums[running_sum - k]

            sums[running_sum] += 1

        return total
