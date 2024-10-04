"""
https://leetcode.com/problems/continuous-subarray-sum/

Given a list of non-negative numbers and a target integer
k, write a function to check if the array has a continuous
subarray of size at least 2 that sums up to the multiple
of k, that is, sums up to n*k where n is also an integer.

Subarray is difference between prefix sums a and b.
a - b = nk; (a - b) % k = 0; hence a%k - b%k = 0.
Store prefix sums % k in dictionary.
prefix sums % k is zero.

Time - O(n)
Space - O(n)
"""
from typing import List


class Solution:
    # Explanation: https://www.youtube.com/watch?v=OKcrLfR-8mE&t=397s
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum, hash_map = 0, {0: 0}  # key is prefix sum mod k, value is index in nums

        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum % k not in hash_map:  # if the remainder s % k occurs for the first time
                hash_map[prefix_sum % k] = i + 1
            else:
                # The remainder reoccurs means we added a sum to prefix which is divisible by k
                # if the subarray size is at least two
                if i + 1 - hash_map[prefix_sum % k] >= 2: return True
        return False

    def brute_force(self, nums: List[int], k: int) -> bool:
        results = []
        for i in range(0, len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                if j - i + 1 >= 2 and summ % k == 0: return True

        return False